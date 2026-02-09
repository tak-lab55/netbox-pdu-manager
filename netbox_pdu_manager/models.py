from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

from .choices import PDUTypeChoices, OutletStatusChoices, PhaseChoices


class PDU(NetBoxModel):
    """
    PDU (Power Distribution Unit) model
    Manages Raritan PDUs with comprehensive attributes
    """
    # Basic Information
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="PDU identifier name"
    )
    manufacturer = models.CharField(
        max_length=100,
        default='Raritan',
        help_text="Manufacturer name"
    )
    model = models.CharField(
        max_length=100,
        help_text="Model name (e.g., PX3-5000)"
    )
    serial_number = models.CharField(
        max_length=100,
        blank=True,
        help_text="Serial number"
    )
    pdu_type = models.CharField(
        max_length=50,
        choices=PDUTypeChoices,
        default=PDUTypeChoices.TYPE_RARITAN_PX3,
        help_text="PDU type"
    )

    # Network Configuration
    ip_address = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='pdus',
        blank=True,
        null=True,
        help_text="Management IP address"
    )
    api_url = models.URLField(
        max_length=255,
        blank=True,
        help_text="Raritan API URL (e.g., https://pdu.example.com/)"
    )
    api_port = models.PositiveIntegerField(
        default=443,
        help_text="API port number"
    )
    api_username = models.CharField(
        max_length=100,
        blank=True,
        help_text="API authentication username"
    )
    # NOTE: In production, use NetBox Secrets
    # Phase 2 will integrate with Secrets
    api_password_ref = models.CharField(
        max_length=255,
        blank=True,
        help_text="API password reference (Secrets integration planned)"
    )

    # Physical Location
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.PROTECT,
        related_name='pdus',
        help_text="Installation site"
    )
    rack = models.ForeignKey(
        to='dcim.Rack',
        on_delete=models.PROTECT,
        related_name='pdus',
        blank=True,
        null=True,
        help_text="Installation rack"
    )
    rack_position = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text="Rack unit position"
    )

    # Power Specifications
    rated_voltage = models.PositiveIntegerField(
        help_text="Rated voltage (V)"
    )
    rated_current = models.PositiveIntegerField(
        help_text="Rated current (A)"
    )
    outlet_count = models.PositiveIntegerField(
        help_text="Total outlet count"
    )
    phase_count = models.PositiveSmallIntegerField(
        default=1,
        choices=[(1, 'Single Phase'), (3, 'Three Phase')],
        help_text="Phase count"
    )

    # Raritan-specific Fields
    api_version = models.CharField(
        max_length=20,
        blank=True,
        help_text="Raritan API version (e.g., 4.0.10)"
    )
    firmware_version = models.CharField(
        max_length=50,
        blank=True,
        help_text="Firmware version"
    )

    # Metadata
    description = models.CharField(
        max_length=200,
        blank=True
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('site', 'name')
        verbose_name = 'PDU'
        verbose_name_plural = 'PDUs'

    def __str__(self):
        return f"{self.name} ({self.site})"

    def get_absolute_url(self):
        return reverse('plugins:netbox_pdu_manager:pdu', args=[self.pk])

    def get_pdu_type_color(self):
        """Get color for PDU type badge"""
        return PDUTypeChoices.colors.get(self.pdu_type)

    @property
    def rated_power(self):
        """Calculate rated power (W)"""
        return self.rated_voltage * self.rated_current


class Outlet(NetBoxModel):
    """
    PDU outlet (port) model
    Represents individual power outlets on a PDU
    """
    # PDU Relationship
    pdu = models.ForeignKey(
        to=PDU,
        on_delete=models.CASCADE,
        related_name='outlets'
    )

    # Basic Information
    outlet_number = models.PositiveIntegerField(
        help_text="Outlet number (physical port number)"
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Outlet name (custom name)"
    )
    label = models.CharField(
        max_length=100,
        blank=True,
        help_text="Label (physical label)"
    )
    description = models.CharField(
        max_length=200,
        blank=True
    )

    # Status
    status = models.CharField(
        max_length=20,
        choices=OutletStatusChoices,
        default=OutletStatusChoices.STATUS_UNKNOWN,
        help_text="Current power status"
    )

    # Connected Device
    connected_device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.SET_NULL,
        related_name='power_sources',
        blank=True,
        null=True,
        help_text="Connected device"
    )
    connected_device_port = models.CharField(
        max_length=50,
        blank=True,
        help_text="Device-side power port name"
    )

    # Power Information (Phase 2 expansion planned)
    last_measured_voltage = models.FloatField(
        blank=True,
        null=True,
        help_text="Last measured voltage (V)"
    )
    last_measured_current = models.FloatField(
        blank=True,
        null=True,
        help_text="Last measured current (A)"
    )
    last_measured_power = models.FloatField(
        blank=True,
        null=True,
        help_text="Last measured power (W)"
    )
    last_update = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Last data update timestamp"
    )

    # Physical Layout (Optional)
    bank_number = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text="Bank number (for multi-bank PDUs)"
    )
    phase = models.CharField(
        max_length=10,
        blank=True,
        choices=PhaseChoices,
        help_text="Connected phase"
    )

    class Meta:
        ordering = ('pdu', 'outlet_number')
        unique_together = ('pdu', 'outlet_number')
        verbose_name = 'Outlet'
        verbose_name_plural = 'Outlets'

    def __str__(self):
        if self.name:
            return f"{self.pdu.name} - Port {self.outlet_number} ({self.name})"
        return f"{self.pdu.name} - Port {self.outlet_number}"

    def get_absolute_url(self):
        return reverse('plugins:netbox_pdu_manager:outlet', args=[self.pk])

    def get_status_color(self):
        """Get color for status badge"""
        return OutletStatusChoices.colors.get(self.status)

    @property
    def display_name(self):
        """Return display name"""
        return self.name or f"Port {self.outlet_number}"
