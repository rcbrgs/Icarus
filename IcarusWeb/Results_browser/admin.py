from django.contrib import admin
from .models import ( ACL,
                      Algorithm,
                      Area_type,
                      Classification,
                      Climate_information,
                      Collect,
                      Collection_type,
                      Donation,
                      File,
                      Gene_bank_registry,
                      Image,
                      Institution,
                      Landmarks,
                      Location,
                      Manual_classification,
                      MosquitoLab,
                      Photophysiognomy,
                      Political_location,
                      Procrustes,
                      Publication,
                      Result,
                      Sample,
                      Sample_group,
                      Sample_image_wing,
                      Sample_input,
                      Sample_sound_wingbeat,
                      Sample_wing,
                      Sound,
                      Storage,
                      User,
                      User_type )                      

# Register your models here.

admin.site.register ( ACL )
admin.site.register ( Algorithm )
admin.site.register ( Area_type )
admin.site.register ( Classification )
admin.site.register ( Climate_information )
admin.site.register ( Collect )
admin.site.register ( Collection_type )
admin.site.register ( Donation )
admin.site.register ( File )
admin.site.register ( Gene_bank_registry )
admin.site.register ( Image )
admin.site.register ( Institution )
admin.site.register ( Landmarks )
admin.site.register ( Manual_classification )
admin.site.register ( MosquitoLab )
admin.site.register ( Photophysiognomy )
admin.site.register ( Political_location )
admin.site.register ( Procrustes )
admin.site.register ( Publication )
admin.site.register ( Result )
admin.site.register ( Sample )
admin.site.register ( Sample_group )
admin.site.register ( Sample_image_wing )
admin.site.register ( Sample_input )
admin.site.register ( Sample_sound_wingbeat )
admin.site.register ( Sample_wing )
admin.site.register ( Sound )
admin.site.register ( Storage )
admin.site.register ( User )
admin.site.register ( User_type )
