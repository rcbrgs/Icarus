from django.conf.urls import url

from . import models
from . import views

urlpatterns = [
    url ( r"^$", views.index, name = "index" ),
    url ( r"^(?P<table_name>[\w]+)/*$", views.table_index, name = "table_index" ),
    url ( r"^(?P<table_name>[\w]+)/(?P<record_id>[0-9]+)/*$", views.record_view, name = "record_view" ),
    url ( r"^(?P<table_name>[\w]+)/(?P<record_id>-[0-9]+)/*$", views.invalid_record_view, name = "invalid_record_view" ),
    url ( r"^(?P<table_name>manual_classification)/add/*$", views.add_record_manual_classification, name = "add_record_manual_classification" ),
    url ( r"^(?P<table_name>sample)/add/*$", views.add_record_sample, name = "add_record_sample" ),
    ]
