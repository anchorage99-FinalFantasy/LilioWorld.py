print()
print ('Hello World')
print ('My name is Derek, \n')
age = 46
print ('I am', age, 'years old.')
year = 2026
print ('I started programming in the year', year, '\n')

print ('What year are you in?', 'Is it' , year, '\n')

year = input ('What year are you born in? ')
print (f' So the year you were born in is {year} \n')

car = input ('What kind of car do you like? ')
print (f' The kind of car you like is the  {car}  \n')


easier = input ('Is learning Python easier than learning Java?, \n')
print()

harder = input ('Is learning Python harder than learning Java?, \n')
print()

car_make = input ('What is the make of your car? ')
print()

print (f"""You are {age} years old, You were born in {year},
You like the {car}, And the make of your car is the {car_make}.
You also said that learning Python is easier than learning Java {easier}
and that learning Java is harder than learning Python {harder}. """)