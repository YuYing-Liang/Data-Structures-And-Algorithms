#5 weekly assignments in one file, combining python files into one program
from mult import mult
from exponentiate import exponentiate
from factorial import factorial
from bsqrt import bsqrt
from gcd import gcd

fcnChosen = input("Enter either the letters m,e,f,b or g to access the function, if you would like to quit, enter q:")

while True:
	char = fcnChosen.lower()
	if char == "q":
		break;
	elif char == "m":
		#assuming user enters integers
		a = int( input("Enter in a numeric value:"))
		b = int( input("Enter in a second numeric value:"))
		print("The product is: " + str(mult(a,b)))
	elif char == "e":
		#assuming user enters integers
		b = int( input("Enter a base:"))
		p = int( input("Enter an exponent:"))
		print("The power is: " + str(exponentiate(b,p)))
	elif char == "f":
		#assuming user enters integers
		num = int( input("Enter a number:"))
		print("The factorial is: " + str(factorial(num)))
	elif char == "b":
		#assuming user enters integers
		num = int( input("Enter a number:"))
		accuracy = int( input("Enter the amount of decimal places:"))
		sqrt = bsqrt(num, accuracy)
		if sqrt >= 0:
			print("The square root is: " + str(sqrt))
		else:
			print("Unable to compute square")
	elif char == "g":
		#assuming user enters integers
		x = int( input("Enter an integer:"))
		y = int( input("Enter another integer:"))
		print("The greatest common denominator of these two numbers is: " + str(gcd(x,y)))
	else:
		print("Invalid input")	
	fcnChosen = input("Enter another character to perform a function:")

print("Thank you for using!")
	
			
				

	


