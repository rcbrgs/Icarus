from django.contrib import admin
from .models import ( ACL,
                      Algorithm,
                      Classification,
                      Donation,
                      File,
                      Image,
                      Institution,
                      Landmarks,
                      Manual_classification,
                      Procrustes,
                      Result,
                      Sample,
                      Sample_image_wing,
                      Sample_input,
                      User,
                      User_type )                      

# Register your models here.

admin.site.register ( ACL )
admin.site.register ( Algorithm )
admin.site.register ( Classification )
admin.site.register ( Donation )
admin.site.register ( File )
admin.site.register ( Image )
admin.site.register ( Institution )
admin.site.register ( Landmarks )
admin.site.register ( Manual_classification )
admin.site.register ( Procrustes )
admin.site.register ( Result )
admin.site.register ( Sample )
admin.site.register ( Sample_image_wing )
admin.site.register ( Sample_input )
admin.site.register ( User )
admin.site.register ( User_type )
