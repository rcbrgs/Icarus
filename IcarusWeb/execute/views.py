from django.http import Http404, HttpResponse
from django.shortcuts import render
from Results_browser.models import Sample

def index ( request ):
    return HttpResponse ( "This is a stub." )

def sample ( request, sample_id ):
    try:
        sample_row = Sample.objects.get ( pk = sample_id )
    except Sample.DoesNotExist:
        raise Http404 ( "Sample does not exist." )
    # call to pipeline here?'
    return render ( request, "execute/sample.html", { "sample": sample_row } )
