from __future__ import unicode_literals

from django.db import models

# Create your models here.
from __future__ import unicode_literals

from django.db import models

class Prospect(models.Model):
#PROSPECTIVE CUSTOMER INFORMATION
  prospectfn = models.CharField(max_length=30)
  prosepectln = models.CharField(max_length=30)
  #RELATIONSHIP TO PROSPECTIVE CUSTOMER
  recipientreltoProspect_mother = models.BooleanField(default=False)
  recipientreltoProspect_father = models.BooleanField(default=False)
  recipientreltoProspect_husband = models.BooleanField(default=False)
  recipientreltoProspect_wife = models.BooleanField(default=False)
  recipientreltoProspect_grandmother = models.BooleanField(default=False)
  recipientReltoProspect_grandfather = models.BooleanField(default=False)
  recipientReltoProspect_other = models.BooleanField(default=False)
  recipientReltoProspect_myself = models.BooleanField(default=False)
  #PREFERRED GENDER
  noGenderPreference = models.BooleanField(default=False) 
  femalePreference = models.BooleanField(default=False) 
  malePreference = models.BooleanField(default=False)
  #WHEN AND WHERE DO YOU NEED CARE?
  care_county_Brooklyn = models.BooleanField(default=False)
  care_county_Bronx = models.BooleanField(default=False)
  care_county_Manahattan = models.BooleanField(default=False) 
  care_county_StatenIsland = models.BooleanField(default=False) 
  care_county_Queens = models.BooleanField(default=False)
  care_county_Westchester = models.BooleanField(default=False) 
  emergencyCoverage = models.BooleanField(default=False)
  preferredLanguage_English = models.BooleanField(default=False)
  preferredLanguage_Spanish = models.BooleanField(default=False)
  preferredLanguage_Yiddish = models.BooleanField(default=False)
  preferredLanguage_HatianCreole = models.BooleanField(default=False) 
  preferredLanguage_Russian = models.BooleanField(default=False)
  preferredLanguage_Usbek = models.BooleanField(default=False)
  #REQUESTED SCHEDULE BROAD#
  #24 HOUR CARE REQUEST?
  _24hourCare = models.BooleanField(default=False) 
  duration_one_time = models.BooleanField(default=False) 
  long_term = models.BooleanField(default=False) 
  short_term = models.BooleanField(default=False)
  #APPROXIMATE TIME OF NEED
  careNeeded_now = models.BooleanField(default=False) 
  careNeeded_this_week = models.BooleanField(default=False) 
  careNeeded_this_month = models.BooleanField(default=False) 
  careNeeded_next_month = models.BooleanField(default=False)
  careNeeded_not_sure = models.BooleanField(default=False)
  #EXTRA THINGS WE SHOULD KNOW 
  specialCareNeeds = models.TextField(max_length=300)
  #REQUESTED SCHUEDULE SPECIFIC#
  # Day of Shift Starts
  #REGULAR CARE REQUESTED
  groceriesShopping = models.BooleanField(default=False) 
  cleaningHousekeeping = models.BooleanField(default=False) 
  hospiceCare = models.BooleanField(default=False)
  transportation = models.BooleanField(default=False) 
  overNightMonitoring = models.BooleanField(default=False) 
  companionCare = models.BooleanField(default=False) 
  personalCare = models.BooleanField(default=False)
  respiteCare = models.BooleanField(default=False)
  mealPreparation = models.BooleanField(default=False)
  #SPECIALTY CARE REQUESTED
  #This care costs more money
  deepCleaning = models.BooleanField(default=False) 
  woundCare = models.BooleanField(default=False) 
  als = models.BooleanField(default=False)
  parkinsonsDisease = models.BooleanField(default=False) 
  physicalTherapy = models.BooleanField(default=False)
  copd = models.BooleanField(default=False) 
  alzheimersDementia = models.BooleanField(default=False)
  #ADDRESS OF CARE RENDERING
  addressBuilding = models.CharField(max_length=30)
  addressStreet = models.CharField(max_length=30)
  addressApartment = models.CharField(max_length=30)
  addressCity = models.CharField(max_length=30)
  addressState = models.CharField(max_length=30)
  addressZip = models.CharField(max_length=30)
  #ALREADY A CUSTOMER?

class TimeSlot(models.Model): 
  prospect = models.ForeignKey(Prospect)
  start_time = models.DateTimeField()

# #RECIPIENT OF CARE INFORMATION
# class Recipient(models.Model):
#   recipientfn=models.CharField(max_length=30)
#   recipientln=models.CharField(max_length=30)

