from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Result, Sample_input, Sample_image_wing

# Create your views here.

def index ( request ):
    return HttpResponse ( "This is a stub." )

def result ( request, result_id ):
    try:
        result_row = Result.objects.get ( pk = result_id )
    except Result.DoesNotExist:
        raise Http404 ( "Result does not exist." )
    return render ( request, "Results_browser/Result.html", { "Result": result_row } )

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
