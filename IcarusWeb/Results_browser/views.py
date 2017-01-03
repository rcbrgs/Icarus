from django.http import Http404, HttpResponse, HttpResponseRedirect
import django
from .forms import SampleForm
import importlib
from .models import Algorithm, Classification, Result, Sample, Sample_input, Sample_image_wing

# auxiliary methods

def get_sensible_name_from_url ( url ):
    return url [ 0 ].upper ( ) + url [ 1: ].lower ( )    

def get_table_from_table_name ( table_name ): 
    module = importlib.import_module ( "Results_browser.models" )
    return getattr ( module, table_name )

@django.contrib.auth.decorators.permission_required (
    "Results_browser.can_view" )
def record_view ( request, table_name, record_id ):
    sensible_name = get_sensible_name_from_url ( table_name )
    table_module = get_table_from_table_name ( sensible_name )
    record = django.shortcuts.get_object_or_404 ( table_module, pk = record_id )
    record_values = { }
    record_relatives = { }
    for field in table_module._meta.fields:
        if field.name [ -3: ] == "_id":
            try:
                record_relatives [ field.name [ :-3 ] ] = getattr ( record, field.name ).id
            except AttributeError:
                record_relatives [ field.name [ :-3 ] ] = -1
        else:
            record_values [ field.name ] = getattr ( record, field.name )
    return django.shortcuts.render ( request, "Results_browser/record_view.html", { "record": record, "table_name": sensible_name, "record_values": record_values, "record_relatives": record_relatives } )    

def invalid_record_view ( request, table_name, record_id ):
    sensible_name = get_sensible_name_from_url ( table_name )
    return django.shortcuts.render ( request, "Results_browser/invalid_record_view.html", { "table": sensible_name } )

def table_index ( request, table_name ):
    sensible_name = get_sensible_name_from_url ( table_name )
    table_module = get_table_from_table_name ( sensible_name )
    table = table_module.objects.all ( )
    print ( "table = {}".format ( table ) )
    return django.shortcuts.render ( request, "Results_browser/table_index.html", { "table": table, "table_name": sensible_name } )

def index ( request ):
    return django.shortcuts.render ( request, "Results_browser/index.html", { } )

# model forms

def add_record_manual_classification ( request, table_name ):
    if request.method == "POST":
        form = ManualClassificationForm ( request.POST )
        if form.is_valid ( ):
            return django.http.HttpResponseRedirect ( "/db" )
    form = ManualClassificationForm ( )
    sensible_name = get_sensible_name_from_url ( table_name )
    return django.shortcuts.render ( request, "Results_browser/form_general.html", { "form": form, "table": sensible_name } )

def add_record_sample ( request, table_name ):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return django.http.HttpResponseRedirect ( "/login" )
        form = SampleForm ( request.POST )
        if form.is_valid ( ):
            return django.http.HttpResponseRedirect ( "/db" )
    if not request.user.is_authenticated:
        return django.http.HttpResponseRedirect ( "/login" )
    form = SampleForm ( )
    sensible_name = get_sensible_name_from_url ( table_name )
    return django.shortcuts.render ( request, "Results_browser/form_general.html", { "form": form, "table": sensible_name } )
