import django
from .models import Manual_classification, Sample

class ManualClassificationForm ( django.forms.ModelForm ):
    class Meta:
        model = Manual_classification
        exclude = [ "id" ]

class SampleForm ( django.forms.ModelForm ):
    class Meta:
        model = Sample
        exclude = [ "id" ]
