from numpy import number
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

# Enter your phone number
Number = input("Enter your phone numer with country code : ")

# parse the detail about the phone number
phone_number = phonenumbers.parse(Number)

Timezone =  timezone.time_zones_for_number(phone_number)
print("timezone : ", Timezone)

geolocation = geocoder.description_for_number(phone_number,"en")
print("location : ", geolocation)

service = carrier.name_for_number(phone_number,"en")
print("service provider : ", service)