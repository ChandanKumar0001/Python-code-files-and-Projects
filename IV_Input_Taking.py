name = input("Enter your name: ") # result of input() is always a string
age = input("Enter your age: ")# age int value converted in "24" (string) formate
# age = int(input("Enter your age: "))# # using this type casting method we convert the string input to int input
print ("Welcome: ", name)
print ("Age: ", age) 
print(type(age))      # Here the age input value is String not int so if we want any other or origional data type we have to perform type casting


print("----------------Student Details-----------------------------------")

sname = input("Enter the Student name: ")
sage = int(input("Enter the Student age: "))
smarks = float(input("Enter the Student marks: "))

print ("Welcome: ", sname)
print ("Age: ", sage)
print ("Marks: ", smarks)