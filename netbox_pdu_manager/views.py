from django.db.models import Count
from netbox.views import generic

from . import forms, models, tables, filtersets


#
# PDU Views
#

class PDUView(generic.ObjectView):
    """PDU detail view"""
    queryset = models.PDU.objects.all()

    def get_extra_context(self, request, instance):
        # Outlet list table
        outlets_table = tables.OutletTable(
            instance.outlets.all(),
            orderable=False
        )
        outlets_table.configure(request)

        # Calculate outlet statistics
        outlet_stats = {
            'total': instance.outlets.count(),
            'on': instance.outlets.filter(status='on').count(),
            'off': instance.outlets.filter(status='off').count(),
            'unknown': instance.outlets.filter(status='unknown').count(),
            'connected': instance.outlets.filter(
                connected_device__isnull=False
            ).count(),
        }

        return {
            'outlets_table': outlets_table,
            'outlet_stats': outlet_stats,
        }


class PDUListView(generic.ObjectListView):
    """PDU list view"""
    queryset = models.PDU.objects.annotate(
        outlet_count_actual=Count('outlets')
    )
    table = tables.PDUTable
    filterset = filtersets.PDUFilterSet


class PDUEditView(generic.ObjectEditView):
    """PDU create/edit view"""
    queryset = models.PDU.objects.all()
    form = forms.PDUForm


class PDUDeleteView(generic.ObjectDeleteView):
    """PDU delete view"""
    queryset = models.PDU.objects.all()


class PDUBulkImportView(generic.BulkImportView):
    """PDU bulk import view"""
    queryset = models.PDU.objects.all()


class PDUBulkEditView(generic.BulkEditView):
    """PDU bulk edit view"""
    queryset = models.PDU.objects.all()
    filterset = filtersets.PDUFilterSet
    table = tables.PDUTable


class PDUBulkDeleteView(generic.BulkDeleteView):
    """PDU bulk delete view"""
    queryset = models.PDU.objects.all()
    filterset = filtersets.PDUFilterSet
    table = tables.PDUTable


#
# Outlet Views
#

class OutletView(generic.ObjectView):
    """Outlet detail view"""
    queryset = models.Outlet.objects.select_related(
        'pdu', 'connected_device'
    )


class OutletListView(generic.ObjectListView):
    """Outlet list view"""
    queryset = models.Outlet.objects.select_related(
        'pdu', 'connected_device'
    )
    table = tables.OutletTable
    filterset = filtersets.OutletFilterSet


class OutletEditView(generic.ObjectEditView):
    """Outlet create/edit view"""
    queryset = models.Outlet.objects.all()
    form = forms.OutletForm


class OutletDeleteView(generic.ObjectDeleteView):
    """Outlet delete view"""
    queryset = models.Outlet.objects.all()


class OutletBulkImportView(generic.BulkImportView):
    """Outlet bulk import view"""
    queryset = models.Outlet.objects.all()


class OutletBulkEditView(generic.BulkEditView):
    """Outlet bulk edit view"""
    queryset = models.Outlet.objects.all()
    filterset = filtersets.OutletFilterSet
    table = tables.OutletTable


class OutletBulkDeleteView(generic.BulkDeleteView):
    """Outlet bulk delete view"""
    queryset = models.Outlet.objects.all()
    filterset = filtersets.OutletFilterSet
    table = tables.OutletTable
