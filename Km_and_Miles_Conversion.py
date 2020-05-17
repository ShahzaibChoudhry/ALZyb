#Kilometers to meters conversion


user = float(input('Enter Kilometers? '))
conversion_factor = 0.621371
miles = user * conversion_factor
print('%0.02f Miles in %0.02f Kilometers'%(miles,user))

#Meters to Kilometers conversion


user = float(input('Enter Meters? '))
conversion_factor = 0.621371
miles = user / conversion_factor
print('%0.02f Kilometers in %0.02f miles'%(miles,user))
