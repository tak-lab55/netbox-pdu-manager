from django import forms
from dcim.models import Device, Rack, Site
from ipam.models import IPAddress
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import PDU, Outlet


class PDUForm(NetBoxModelForm):
    """Form for creating/editing PDU objects"""
    site = DynamicModelChoiceField(
        queryset=Site.objects.all()
    )
    rack = DynamicModelChoiceField(
        queryset=Rack.objects.all(),
        required=False,
        query_params={
            'site_id': '$site'
        }
    )
    ip_address = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        label='IP Address'
    )
    comments = CommentField()

    class Meta:
        model = PDU
        fields = (
            'name', 'manufacturer', 'model', 'serial_number', 'pdu_type',
            'site', 'rack', 'rack_position',
            'ip_address', 'api_url', 'api_port', 'api_username',
            'api_password_ref', 'api_version',
            'rated_voltage', 'rated_current', 'outlet_count', 'phase_count',
            'firmware_version', 'description', 'comments', 'tags'
        )
        help_texts = {
            'api_password_ref': 'Do not enter passwords directly. Use NetBox Secrets reference.',
        }


class OutletForm(NetBoxModelForm):
    """Form for creating/editing Outlet objects"""
    pdu = DynamicModelChoiceField(
        queryset=PDU.objects.all()
    )
    connected_device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False
    )

    class Meta:
        model = Outlet
        fields = (
            'pdu', 'outlet_number', 'name', 'label', 'description',
            'status', 'phase', 'bank_number',
            'connected_device', 'connected_device_port',
            'tags'
        )
