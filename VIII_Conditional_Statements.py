# Program - 1:
age = 21

if(age >= 18):
    print("Can vote & Apply for licences") # indentation (proper spacing) -> after the if/else in next line after 4 space we wrote program called indentation
    
else:
    print("Can't vote & can't Apply for licences")

print("------------------------------------------------------------")

# Program - 2:
light = "green"

if(light == "red"):
    print("stop")

elif(light == "green"):
    print("go")
    
elif(light == "yellow"):
    print("look")

else:
    print("Light is broken/not working.")
    
print("End of code")

print("--------------------------------------------------------")

# program - 3:
num = 5

if(num > 2):
    print("greater than 2")
elif(num > 4):
    print("greater than 4")
if(num > 3):
    print("greater than 3")
    
print("-----------------------------------------------------------")

# program - 4:

# marks = int(input("Enter the Marks of Student : "))

# if(marks >= 90):
#     print("Grade = A")

# elif(marks >= 80):
#     print("Grade = B")
    
# elif(marks >= 70):
#     print("Grade = C")

# else:
#     print("Grade = D")
    
print("-------------------------------------------------------")

# nesting or nested if else
age = int(input("Enter the Age: "))

if(age >= 18):
    if(age >= 80):
        print("Can not drive")
    
    else:
        print("Can drive")
        
else:
    print("Can not drive")