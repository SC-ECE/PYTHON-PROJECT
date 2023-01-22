import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter your no. with +91:  ")
phn=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phn)
car=carrier.name_for_number(phn,"en")
reg=geocoder.description_for_number(phn,"en")
print(phn)
print(time)
print(car)
print(reg)