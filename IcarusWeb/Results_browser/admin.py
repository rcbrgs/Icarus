from django.contrib import admin
from .models import Algorithm, Classification, Result, Sample_input

# Register your models here.

admin.site.register ( Algorithm )
admin.site.register ( Classification )
admin.site.register ( Result )
admin.site.register ( Sample_input )
