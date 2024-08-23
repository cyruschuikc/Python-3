### Lesson-04: Input()
## In this lesson, we will learn about the input() function.
## The input() function is used to take input from the user.
## We can use this function to input a letter, a string, integer and float.

input1 = input("") #Input "Hi"
print(type(input1),input1) #<class 'str'> Hi

input2 = input() #Input 1
print(type(input2),input2) #<class 'str'> 1

## The input() function if we not specify data type, it will be default as input string.
## So, if we want to take input as integer, we have to specify the data type as int.
input3 = int(input()) #Input 3
print(type(input3),input3) #<class 'int'> 3
## If we want to take input as float, we have to specify the data type as float.
input4 = float(input()) #Input 4.0
print(type(input4),input4) #<class 'float'> 4.0
## If we want to take input as string, we have to specify the data type as str.
input5 = str(input("")) #Input "T"
print(type(input5),input5) #<class 'str'> T

## This is the end of this lesson. Thank you for your attention. 
## If you feel interested, you can follow me. I will update content as soon as possible.
