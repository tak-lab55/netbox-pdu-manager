from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (
    # PDU URLs
    path('pdus/', views.PDUListView.as_view(), name='pdu_list'),
    path('pdus/add/', views.PDUEditView.as_view(), name='pdu_add'),
    path('pdus/import/', views.PDUBulkImportView.as_view(), name='pdu_import'),
    path('pdus/edit/', views.PDUBulkEditView.as_view(), name='pdu_bulk_edit'),
    path('pdus/delete/', views.PDUBulkDeleteView.as_view(), name='pdu_bulk_delete'),
    path('pdus/<int:pk>/', views.PDUView.as_view(), name='pdu'),
    path('pdus/<int:pk>/edit/', views.PDUEditView.as_view(), name='pdu_edit'),
    path('pdus/<int:pk>/delete/', views.PDUDeleteView.as_view(), name='pdu_delete'),
    path('pdus/<int:pk>/changelog/', ObjectChangeLogView.as_view(),
         name='pdu_changelog', kwargs={'model': models.PDU}),

    # Outlet URLs
    path('outlets/', views.OutletListView.as_view(), name='outlet_list'),
    path('outlets/add/', views.OutletEditView.as_view(), name='outlet_add'),
    path('outlets/import/', views.OutletBulkImportView.as_view(), name='outlet_import'),
    path('outlets/edit/', views.OutletBulkEditView.as_view(), name='outlet_bulk_edit'),
    path('outlets/delete/', views.OutletBulkDeleteView.as_view(), name='outlet_bulk_delete'),
    path('outlets/<int:pk>/', views.OutletView.as_view(), name='outlet'),
    path('outlets/<int:pk>/edit/', views.OutletEditView.as_view(), name='outlet_edit'),
    path('outlets/<int:pk>/delete/', views.OutletDeleteView.as_view(), name='outlet_delete'),
    path('outlets/<int:pk>/changelog/', ObjectChangeLogView.as_view(),
         name='outlet_changelog', kwargs={'model': models.Outlet}),
)
