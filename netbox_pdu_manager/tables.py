import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import PDU, Outlet


class PDUTable(NetBoxTable):
    """Table for displaying PDU list"""
    name = tables.Column(
        linkify=True
    )
    site = tables.Column(
        linkify=True
    )
    rack = tables.Column(
        linkify=True
    )
    pdu_type = ChoiceFieldColumn()
    ip_address = tables.Column(
        linkify=True
    )
    outlet_count_actual = tables.Column(
        verbose_name='Outlets (Configured)',
        empty_values=(),
        orderable=False
    )

    class Meta(NetBoxTable.Meta):
        model = PDU
        fields = (
            'pk', 'id', 'name', 'manufacturer', 'model', 'pdu_type',
            'site', 'rack', 'ip_address', 'outlet_count',
            'outlet_count_actual', 'rated_voltage', 'rated_current',
            'actions'
        )
        default_columns = (
            'name', 'pdu_type', 'site', 'rack', 'outlet_count_actual',
            'actions'
        )

    def render_outlet_count_actual(self, record):
        """Render actual outlet count from related outlets"""
        return record.outlets.count()


class OutletTable(NetBoxTable):
    """Table for displaying Outlet list"""
    pdu = tables.Column(
        linkify=True
    )
    outlet_number = tables.Column(
        linkify=True
    )
    name = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()
    connected_device = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = Outlet
        fields = (
            'pk', 'id', 'pdu', 'outlet_number', 'name', 'label',
            'status', 'phase', 'connected_device',
            'connected_device_port', 'last_measured_power', 'actions'
        )
        default_columns = (
            'pdu', 'outlet_number', 'name', 'status',
            'connected_device', 'actions'
        )
