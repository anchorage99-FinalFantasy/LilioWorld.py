print (" \n This is Lilo world of Learning Python \n")

print (f" First order of business is to learn Python programming language, "  
       f"Plus what is your name? \n")

name = input (" Please enter your name: ")
print (f" Hello {name}, welcome to the Lilo world of Learning Python! \n")

print (f" The first lesson we are going to do is,"
       f" working on a weather converting program \n")

print ("Now make me a weather converter that will convert Fahrenheit to Celsius.\n")

fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print (f" The temperature in Celsius is: {celsius:.2f} \n")