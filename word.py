
#import math

#a = 5.65


#print( math.floor(a) )

#import math

#print( math.pi)
#Calculator
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Back.GREEN )
print( Fore.BLACK)

what = input( "What? (+, -): " )

print( Back.CYAN)

a = float( input("put first: ") )
b = float( input("put second: ") )

print( Back.YELLOW)

if what == "+":
	c = a + b
	print("equals: " + str(c))

elif what == "-":
	c = a - b
	print("equals: " + str(c))
else: 
	print("wrong")

input()