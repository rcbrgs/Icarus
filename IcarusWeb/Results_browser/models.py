from django.db import models

# Create your models here.

class Algorithm ( models.Model ):
    
    # Must be before Result.
    name = models.CharField ( max_length = 255 )
    version_git_commit = models.CharField ( max_length = 255 )

class Classification ( models.Model ):

    # Must be interpreted before Result.
    genus = models.CharField ( max_length = 255 )
    subgenus = models.CharField ( max_length = 255 )
    species = models.CharField ( max_length = 255 )
    subspecies = models.CharField ( max_length = 255 )
    family = models.CharField ( max_length = 255 )
    subfamily = models.CharField ( max_length = 255 )

#class Sample_image_wing ( models.Model ):
    
class Sample_input ( models.Model ):

    # Must be before Result.
    sample_type = models.CharField ( max_length = 255 )
    #sample_image_wing_id = models.ForeignKey ( Sample_image_wing, null = True, blank = True )
    #sample_sound_wingbeat_id = models.ForeignKey ( Sample_sound_wingbeat, null = True, blank = True )
    
class Result ( models.Model ):

    # Must be interpreted after Classification.
    sample_input_id = models.ForeignKey ( Sample_input )
    algorithm_id = models.ForeignKey ( Algorithm )
    classification_id = models.ForeignKey ( Classification )

#class Sample ( models.Model ):
#    butantan_registry
#    LECZ_registry
#    date
#    origin
#    specimen_stage
#    is_female_compatible
#    is_male_compatible
#    #notes_file_id = models.ForeignKey (  )
#    #collector_user_id = models.ForeignKey (  )
#    #donation_id = models.ForeignKey (  )
#    #manual_classification_id = models.ForeignKey (  )
#    #mosquitolab_id = models.ForeignKey (  )
#    #gene_bank_registry_id = models.ForeignKey (  )
#    #phytophysiognomy_id = models.ForeignKey (  )
#    #collect_id = models.ForeignKey (  )
#    #storage_id = models.ForeignKey (  )
