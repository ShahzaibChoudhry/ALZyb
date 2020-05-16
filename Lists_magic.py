List_of_some_fruits = ['Banana', 'Apple', 'Strawbery', 'Mango', 'Pine Apple', 'Grapes']
List_of_some_vagetables = ['Onion', 'Locke', 'Ginger', 'Water Melon', 'Red Grapes']
List_of_famous_cities = ['New York', 'London','Dubai','Madina','Washington','New Dehli']
List_of_famous_countries = ['Turkey', 'China','America','United Kingdom','South Africa','Pakistan']
#print(List_of_some_vagetables[4] + " not a Vagetable")
List_of_some_fruits.append("Cherry") #.append function use for add 1 value end of the list
List_of_famous_countries.insert(2,'Russia') #.insert funtion use for add value with index number
List_of_famous_cities.extend(['Islamabad','Istanbul','Ankara','Shinghai']) #.extend function use for add more then 1 value in end of the list
List_of_famous_cities.index('Dubai') #.index function
List_of_some_fruits.copy()   #.copy function to use copy a list by reference
List_of_famous_cities.remove('New Dehli') #.remove funcyion used to remove value from list
print(List_of_famous_countries[1:7]) #slicing the edlements from the list

