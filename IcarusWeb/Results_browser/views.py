from django.http import Http404, HttpResponse
import django
import importlib
from .models import Algorithm, Classification, Result, Sample, Sample_input, Sample_image_wing

# auxiliary methods

def get_sensible_name_from_url ( url ):
    return url [ 0 ].upper ( ) + url [ 1: ].lower ( )    

def get_table_from_table_name ( table_name ): 
    module = importlib.import_module ( "Results_browser.models" )
    return getattr ( module, table_name )

# Create your views here.

def algorithm ( request, algorithm_id ):
    try:
        algorithm_row = Algorithm.objects.get ( pk = algorithm_id )
    except Algorithm.DoesNotExist:
        raise Http404 ( "Algorithm does not exist." )
    return render ( request, "Results_browser/algorithm.html", { "algorithm": algorithm_row } )

def record_view ( request, table_name, record_id ):
    sensible_name = get_sensible_name_from_url ( table_name )
    table_module = get_table_from_table_name ( sensible_name )
    record = django.shortcuts.get_object_or_404 ( table_module, pk = record_id )
    record_values = table_module.objects.values ( id == record_id )
    return django.shortcuts.render ( request, "Results_browser/record_view.html", { "record": record, "table_name": sensible_name} )    

def table_index ( request, table_name ):
    sensible_name = get_sensible_name_from_url ( table_name )
    table_module = get_table_from_table_name ( sensible_name )
    table = table_module.objects.all ( )
    print ( "table = {}".format ( table ) )
    return render ( request, "Results_browser/table_index.html", { "table": table, "table_name": sensible_name } )

def classification ( request, classification_id ):
    try:
        classification_row = Classification.objects.get ( pk = classification_id )
    except Classification.DoesNotExist:
        raise Http404 ( "Classification does not exist." )
    return render ( request, "Results_browser/classification.html", { "classification": classification_row } )

def index ( request ):
    return render ( request, "Results_browser/index.html", { } )

def result ( request, result_id ):
    try:
        result_row = Result.objects.get ( pk = result_id )
    except Result.DoesNotExist:
        raise Http404 ( "Result does not exist." )
    return render ( request, "Results_browser/Result.html", { "Result": result_row } )

def sample ( request, sample_id ):
    try:
        sample_row = Sample.objects.get ( pk = sample_id )
    except Sample.DoesNotExist:
        raise Http404 ( "Sample does not exist." )
    return render ( request, "Results_browser/sample.html", { "sample": sample_row } )

def sample_input ( request, sample_input_id ):
    try:
        sample_input_row = Sample_input.objects.get ( pk = sample_input_id )
    except Sample_input.DoesNotExist:
        raise Http404 ( "Sample_input does not exist." )
    return render ( request, "Results_browser/Sample_input.html", { "sample_input": sample_input_row } )

def sample_image_wing ( request, sample_image_wing_id ):
    try:
        sample_image_wing_row = Sample_image_wing.objects.get ( pk = sample_image_wing_id )
    except Sample_image_wing.DoesNotExist:
        raise Http404 ( "Sample wing image does not exist." )
    return render ( request, "Results_browser/Sample_image_wing.html", { "sample_image_wing": sample_image_wing_row } )
