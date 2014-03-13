__author__ = 'amertis'
from django.db import models





class OpeniContext(models.Model):
    # id is missing because it is the default
    time_created = models.DateTimeField(null=True)
    time_edited = models.DateTimeField(null=True)
    time_deleted = models.DateTimeField(null=True)
    duration_time_started = models.DateTimeField(null=True)
    duration_time_ended = models.DateTimeField(null=True)
#     #use floats?
#     #the docs say location includes: coordinates,physical address, free-form location name
    location_latitude = models.FloatField(null=True)
    location_longitude = models.FloatField(null=True)
    location_height = models.FloatField(null=True)
#
    address_street = models.TextField(null=True)
    address_number = models.TextField(null=True)
    address_apartment = models.TextField(null=True)
    address_city = models.TextField(null=True)
    address_locality = models.TextField(null=True)
    address_country = models.TextField(null=True)
    address_zip = models.TextField(null=True)
#
#     #use floats?
#     #this is list?
#     # Location Visits separate table
#     location_visits_latitude = models.CharField(max_length=10,null=True)
#     location_visits_longitude = models.CharField(max_length=10,null=True)
#     location_visits_height = models.CharField(max_length=10,null=True)
#     #todo:what is this
#     location_visits_visit = models.IntegerField(null=True)
#     location_visits_comment = models.CharField(max_length=500,null=True)
#
#     #use floats?
    current_location_latitude = models.FloatField(null=True)
    current_location_longitude = models.FloatField(null=True)
    current_location_height = models.FloatField(null=True)
#     #use date
    current_location_time = models.DateTimeField(null=True)
    rating = models.FloatField(null=True)
#     #privacy
#     #examples
#     # list of friend lists with list of friends....
#     friends_ids = models.CharField(max_length=1000,null=True)
#     friends_name = models.CharField(max_length=1000,null=True)
#     friends_type = models.CharField(max_length=1000,null=True)
#
#     friend_id = models.CharField(max_length=100,null=True)
#     friend_object_type = models.CharField(max_length=100,null=True)
#     friend_url = models.CharField(max_length=200,null=True)
#     friend_service = models.CharField(max_length=100,null=True)
#     friend_to_id = models.CharField(max_length=100,null=True)
#
#     friend_time_friend_added = models.DateTimeField(max_length=100,null=True)
#     #whatisit?
#     #object id
#     # type of strings....
#     friend_target_id = models.CharField(max_length=100,null=True)
#     #happy,sad
    mood = models.TextField(null=True)
#     #3G,LTE
    device_wireless_network_type = models.TextField(null=True)
#     #good,bad,excellent
    device_wireless_channel_quality = models.TextField(null=True)
#     #...
    device_accelerometers = models.TextField(null=True)
#     #.... length of cell id... up to 30
    device_cell_log = models.TextField(null=True)
#     # sms recipients phones list up to 30
    device_sms_log = models.TextField(null=True)
#     # sms phonecalls  list up to 30 comma separated
    device_call_log = models.TextField(null=True)
#
#     # a csv of openI appIds (up to 30) ---
    device_running_applications = models.TextField(null=True)
#
#     # installed openI apps
    device_installed_applications = models.TextField(null=True)
#     # tov
    device_screen_state = models.TextField(null=True)
#     # low,medium,full
    device_battery_status = models.TextField(null=True)
#
#     #red,'#fbfbfb' from W3C
    application_background_color = models.TextField(null=True)
#
    application_format = models.TextField(null=True)
    application_font = models.TextField(null=True)
    application_color = models.TextField(null=True)
    application_background = models.TextField(null=True)
    application_text = models.TextField(null=True)
    application_box = models.TextField(null=True)
    application_classification = models.TextField(null=True)
    application_text_copy = models.TextField(null=True)
#
#
    personalization_age_range = models.TextField(null=True)
#     # 3iso
    personalization_country = models.TextField(null=True)
    personalization_postal_code = models.TextField(null=True)
    personalization_region = models.TextField(null=True)
    personalization_town = models.TextField(null=True)
#     #remove
    personalization_geofencing = models.TextField(null=True)
#     #to remove....
    personalization_bearer = models.TextField(null=True)
#     #string...two values
    personalization_roaming = models.TextField(null=True)
#     #string... two values
    personalization_opt_out = models.TextField(null=True)
#
    personalization_carrier = models.TextField(null=True)
#     #Tablet,Smartphone,PDA
    personalization_handset = models.TextField(null=True)
#     #remove
    personalization_user_ids = models.TextField(null=True)
#     #UDID,an UUID
    personalization_device_id = models.TextField(null=True)
#
    personalization_application_id = models.TextField(null=True)
#     #Samsung S4
    personalization_device_type = models.TextField(null=True)
#     #Android,IOS, Windows Mobile
    personalization_device_os = models.TextField(null=True)
#     #Any male ,
    personalization_gender = models.TextField(null=True)
    personalization_has_children = models.TextField(null=True)
#     #
    personalization_ethnicity = models.TextField(null=True)
#
    personalization_income = models.TextField(null=True)
#     #Any, Exactly 1 Exactly 2 Exactly 3 Exactly 4, 2 or fewer, 2 or more, 3 or more, 4 or more , 5 or more
    personalization_household_size = models.TextField(null=True)
    personalization_education = models.TextField(null=True)
    personalization_interests = models.TextField(null=True)
#     #Any, Those who received, Those who interacted with For Past Campaigns, Those who interacted with For Launched Campaigns
    personalization_customer_tag = models.TextField(null=True)
#     #Greek,English iso code
    personalization_users_language = models.TextField(null=True)


class Group(models.Model):
    group_id = models.TextField(null=True)
    group_name = models.TextField(null=True)
    group_type = models.TextField(null=True)
    context = models.ForeignKey(OpeniContext)

class Person(models.Model):
    person_id = models.TextField(null=True)
    person_object_type = models.TextField(null=True)
    person_url = models.TextField(null=True)
    person_service = models.TextField(null=True)
    person_to_id = models.TextField(null=True)
    person_time_person_added = models.DateTimeField(null=True)
    person_target_id = models.TextField(null=True)
    group = models.ForeignKey(Group)

class LocationVisit(models.Model):
    location_visits_latitude = models.FloatField(null=True)
    location_visits_longitude = models.FloatField(null=True)
    location_visits_height = models.FloatField(null=True)
    location_visits_visit = models.IntegerField(null=True)
    location_visits_comment = models.TextField(null=True)
    context = models.ForeignKey(OpeniContext)