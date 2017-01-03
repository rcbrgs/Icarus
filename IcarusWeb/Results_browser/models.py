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

class Area_type ( models.Model ):
    name = models.CharField ( max_length = 255 )
    
class Algorithm ( models.Model ):
    # Must be before Result.
    name = models.CharField ( max_length = 255 )
    version_git_commit = models.CharField ( max_length = 255 )

class Classification ( models.Model ):
    # Must be interpreted before Result.
    genus = models.CharField ( max_length = 30 )
    subgenus = models.CharField ( max_length = 30 )
    species = models.CharField ( max_length = 30 )
    subspecies = models.CharField ( max_length = 30 )
    family = models.CharField ( max_length = 30 )
    subfamily = models.CharField ( max_length = 30 )

class Collection_type ( models.Model ):
    specimen_stage = models.CharField ( max_length = 25 )
    method = models.CharField ( max_length = 255 )

class Climate_information ( models.Model ):
    temperature = models.FloatField ( )
    wind = models.FloatField ( )
    air_relative_humidity = models.FloatField ( )
    pluviosity = models.FloatField ( )
    date = models.DateField ( )
    time = models.DateTimeField ( )
    
class Political_location ( models.Model ):
    country = models.CharField ( max_length = 100 )
    state = models.CharField ( max_length = 100 )
    city = models.CharField ( max_length = 100 )
    
class Location ( models.Model ):
    name = models.CharField ( max_length = 255 )
    latitude = models.FloatField ( )
    longitude = models.FloatField ( )
    datum = models.CharField ( max_length = 100 )
    altitude = models.FloatField ( )
    political_location_id = models.ForeignKey ( Political_location )
    area_type_id = models.ForeignKey ( Area_type )
    
class Publication ( models.Model ):
    journal_name = models.CharField ( max_length = 255 )
    journal_page_number = models.IntegerField ( )
    journal_volume = models.CharField ( max_length = 10 )
    article_title = models.CharField ( max_length = 255 )
    url = models.CharField ( max_length = 255 )
    author_name = models.CharField ( max_length = 100 )
    year = models.DateField ( )
    doi = models.CharField ( max_length = 255 )
    
class Collect ( models.Model ):
    date = models.DateField ( )
    location_id = models.ForeignKey ( Location )
    code = models.CharField ( max_length = 255 )
    climate_information_id = models.ForeignKey ( Climate_information )
    collection_type_id = models.ForeignKey ( Collection_type )
    publication_id = models.ForeignKey ( Publication )
    
class Donation ( models.Model ):
    date = models.DateField ( )
    number_of_structures = models.IntegerField ( )
    institution_id = models.ForeignKey ( Institution )
    user_id = models.ForeignKey ( User )
    
class File ( models.Model ):
    host = models.CharField ( max_length = 255 )
    path = models.CharField ( max_length = 255 )
    ACL_id = models.ForeignKey ( ACL )

class Gene_bank_registry ( models.Model ):
    identifier = models.CharField ( max_length = 100 )
    url = models.CharField ( max_length = 255 )
    name = models.CharField ( max_length = 50 )
    
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

class Mosquitolab ( models.Model ):
    page_number = models.IntegerField ( )
    book_code = models.CharField ( max_length = 3 )
    code = models.CharField ( max_length = 255 )

class Phytophysiognomy ( models.Model ):
    name = models.CharField ( max_length = 100 )
    description = models.CharField ( max_length = 255 )

class Sample_image_wing ( models.Model ):
    # must be before Sample_input
    image_id = models.ForeignKey ( Image, null = True, blank = False )
    #sample_wing_id = models.ForeignKey ( Sample_wing, null = True, blank = False )
    landmarks_id = models.ForeignKey ( Landmarks, null = True, blank = True )
    file_id = models.ForeignKey ( File, null = True, blank = False )

class Storage ( models.Model ):
    date_start = models.DateField ( )
    date_end = models.DateField ( )
    inventory_code = models.CharField ( max_length = 255, null = True )
    location_id = models.ForeignKey ( Location )
    storage_medium = models.CharField ( max_length = 100 )
    
class Sample ( models.Model ):
    butantan_registry = models.CharField ( max_length = 20 )
    is_female_compatible = models.BooleanField ( )
    is_male_compatible = models.BooleanField ( )
    LECZ_registry = models.CharField ( max_length = 20 )
    #notes_file_id = models.ForeignKey (  )
    user_id = models.ForeignKey ( User )
    donation_id = models.ForeignKey ( Donation )
    manual_classification_id = models.ForeignKey ( Manual_classification, null = True )
    mosquitolab_id = models.ForeignKey ( Mosquitolab, null = True )
    gene_bank_registry_id = models.ForeignKey ( Gene_bank_registry, null = True )
    phytophysiognomy_id = models.ForeignKey ( Phytophysiognomy, null = True )
    collect_id = models.ForeignKey ( Collect, null = True )
    storage_id = models.ForeignKey ( Storage, null = True )

class Sample_group ( models.Model ):
    classification_id = models.ForeignKey ( Classification )
    sample_id = models.ForeignKey ( Sample )

class Sound ( models.Model ):
    sampling_rate = models.FloatField ( )
    encoding = models.CharField ( max_length = 255 )
    
class Sample_sound_wingbeat ( models.Model ):
    file_id = models.ForeignKey ( File )
    sample_id = models.ForeignKey ( Sample )
    sound_id = models.ForeignKey ( Sound )

class Sample_input ( models.Model ):
    # Must be before Result.
    sample_type = models.CharField ( max_length = 255 )
    sample_image_wing_id = models.ForeignKey ( Sample_image_wing, null = True, blank = True )
    sample_sound_wingbeat_id = models.ForeignKey ( Sample_sound_wingbeat, null = True, blank = True )

class Result ( models.Model ):
    # Must be interpreted after Classification.
    sample_input_id = models.ForeignKey ( Sample_input )
    algorithm_id = models.ForeignKey ( Algorithm )
    classification_id = models.ForeignKey ( Classification )
    
class Sample_wing ( models.Model ):
    sample_id = models.ForeignKey ( Sample )
    is_left_compatible = models.BooleanField ( )
    is_right_compatible = models.BooleanField ( )
    is_internal_compatible = models.BooleanField ( )
    is_external_compatible = models.BooleanField ( )
    
