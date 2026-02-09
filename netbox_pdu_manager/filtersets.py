import django_filters
from django.db.models import Q
from dcim.models import Site, Rack, Device
from netbox.filtersets import NetBoxModelFilterSet

from .models import PDU, Outlet


class PDUFilterSet(NetBoxModelFilterSet):
    """FilterSet for PDU model"""
    site_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        label='Site (ID)',
    )
    site = django_filters.ModelMultipleChoiceFilter(
        field_name='site__slug',
        queryset=Site.objects.all(),
        to_field_name='slug',
        label='Site (slug)',
    )
    rack_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Rack.objects.all(),
        label='Rack (ID)',
    )
    manufacturer = django_filters.CharFilter(
        lookup_expr='icontains'
    )
    model = django_filters.CharFilter(
        lookup_expr='icontains'
    )
    pdu_type = django_filters.MultipleChoiceFilter(
        choices=lambda: PDU._meta.get_field('pdu_type').choices
    )

    class Meta:
        model = PDU
        fields = ('id', 'name', 'manufacturer', 'model', 'serial_number')

    def search(self, queryset, name, value):
        """Quick search functionality"""
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(manufacturer__icontains=value) |
            Q(model__icontains=value) |
            Q(serial_number__icontains=value) |
            Q(description__icontains=value)
        )


class OutletFilterSet(NetBoxModelFilterSet):
    """FilterSet for Outlet model"""
    pdu_id = django_filters.ModelMultipleChoiceFilter(
        queryset=PDU.objects.all(),
        label='PDU (ID)',
    )
    status = django_filters.MultipleChoiceFilter(
        choices=lambda: Outlet._meta.get_field('status').choices
    )
    connected_device_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        label='Connected Device (ID)',
    )
    has_connected_device = django_filters.BooleanFilter(
        method='filter_has_connected_device',
        label='Has connected device'
    )

    class Meta:
        model = Outlet
        fields = ('id', 'outlet_number', 'name', 'label', 'status')

    def search(self, queryset, name, value):
        """Quick search functionality"""
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(label__icontains=value) |
            Q(description__icontains=value) |
            Q(pdu__name__icontains=value)
        )

    def filter_has_connected_device(self, queryset, name, value):
        """Filter by connected device existence"""
        if value:
            return queryset.filter(connected_device__isnull=False)
        return queryset.filter(connected_device__isnull=True)
