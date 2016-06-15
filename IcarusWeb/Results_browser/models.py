from django.db import models

# Create your models here.

class User_type ( models.Model ):
    name = models.CharField ( max_length = 255 )

class Institution ( models.Model ):
    name = models.CharField ( max_length = 255 )
    
class User ( models.Model ):
    # must be before ACL
    # must be after User_type
    # must be after Institution
    name = models.CharField ( max_length = 255 )
    login = models.CharField ( max_length = 255 )
    password = models.CharField ( max_length = 255 )
    telephone = models.CharField ( max_length = 255 )
    institution_id = models.ForeignKey ( Institution )
    user_type_id = models.ForeignKey ( User_type )

class ACL ( models.Model ):
    # must be after User
    read_permission = models.BooleanField ( )
    write_permission = models.BooleanField ( )
    users_list = models.ManyToManyField ( User )

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

class Donation ( models.Model ):
    date = models.DateField ( )
    number_of_structures = models.IntegerField ( )
    donating_institution_id = models.ForeignKey ( Institution )
    donor_user_id = models.ForeignKey ( User )
    
class File ( models.Model ):
    host = models.CharField ( max_length = 255 )
    path = models.CharField ( max_length = 255 )
    ACL_id = models.ForeignKey ( ACL )
    
class Image ( models.Model ):
    image_height = models.IntegerField ( )
    image_width = models.IntegerField ( )

class Procrustes ( models.Model ):
    # must be before Landmarks
    rotation_angle = models.FloatField ( )
    planar_scaling_factor = models.FloatField ( )
    
class Landmarks ( models.Model ):
    # must be after Procrustes
    sequence_number = models.IntegerField ( )
    horizontal_coordinates = models.FloatField ( )
    vertical_coordinates = models.FloatField ( )
    procrustes_id = models.ForeignKey ( Procrustes )

class Manual_classification ( models.Model ):
    user_id = models.ForeignKey ( User )
    classification_id = models.ForeignKey ( Classification )
    
class Sample_image_wing ( models.Model ):
    # must be before Sample_input
    image_id = models.ForeignKey ( Image, null = True, blank = False )
    #sample_wing_id = models.ForeignKey ( Sample_wing, null = True, blank = False )
    landmarks_id = models.ForeignKey ( Landmarks, null = True, blank = True )
    #file_id = models.ForeignKey ( File, null = True, blank = False )

class Sample_input ( models.Model ):
    # Must be before Result.
    sample_type = models.CharField ( max_length = 255 )
    sample_image_wing_id = models.ForeignKey ( Sample_image_wing, null = True, blank = True )
    #sample_sound_wingbeat_id = models.ForeignKey ( Sample_sound_wingbeat, null = True, blank = True )
    
class Result ( models.Model ):
    # Must be interpreted after Classification.
    sample_input_id = models.ForeignKey ( Sample_input )
    algorithm_id = models.ForeignKey ( Algorithm )
    classification_id = models.ForeignKey ( Classification )

class Sample ( models.Model ):
    butantan_registry = models.CharField ( max_length = 255 )
    is_female_compatible = models.BooleanField ( )
    is_male_compatible = models.BooleanField ( )
    LECZ_registry = models.CharField ( max_length = 255 )
    #notes_file_id = models.ForeignKey (  )
    collector_user_id = models.ForeignKey ( User )
    donation_id = models.ForeignKey ( Donation )
    manual_classification_id = models.ForeignKey ( Manual_classification )
#    #mosquitolab_id = models.ForeignKey (  )
#    #gene_bank_registry_id = models.ForeignKey (  )
#    #phytophysiognomy_id = models.ForeignKey (  )
#    #collect_id = models.ForeignKey (  )
#    #storage_id = models.ForeignKey (  )

