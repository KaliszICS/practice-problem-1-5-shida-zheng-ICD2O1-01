'''
    Lesson: Typecasting
    Author: Mr. Kalisz
    Date Created: Sept 23, 2024
    Date Last Modified: Sept 23, 2024
'''

#Converting data types - Typecasting

#Rules
#For type casting to always work, you need to be going from a simpler data type to a more complicated
#int -> float
#int -> String
#float -> String
#boolean -> String

#When going from a more complicated to simpler type, we need to make sure the data is valid
#String -> int, float, boolean
#float -> int

#str()
#float()
#int()


#int -> float

num = 3
#print(num + 0.0) # * 1.0, - 0.0, / 1.0
num = float(num)
#print(num + " hello") #doesn't work since num is not a string

num = str(num)
print(num + " hello")

#Typecasting creates a copy of the value in the given data type

print(float(num)) #The original variable num is still string

#String -> int, float, boolean
#print(int(num)) #String values cannot be converted to other data types if the value is not valid

#float -> int
#floats have their decimal point removed when converting to integer
num = 3.5
print(int(num))

#converting input to other data types
answer = input("What is your age: ")
answer = int(answer)

print(f"Your age + 5 is: {answer + 5}")