Str1 = "This is a string. \nWe are creating it in python."  # \n -> back slash n shift the String data in next line
Str2 = "This is a string. \tWe are creating it in python."  #  \t -> back slash t give the a tab space means big space between string in same line

print(Str1)
print(Str2)

print("-------------- Basic Operations --------------------------------")

# concatination  -> adding to string in same line using operators

str3 = "Chandan"
str4 = "123"
final_string = str3 + " " + str4

print(str3 + str4)
print(final_string)

# Length of String -> used for find the number of character in a string

len1 = len(str3)
len2 = len(str4)
print(len1)
print(len2)

print ("--------------------------------------------------------------")

# indexing -> it is used to access a specific character from a String, indexing starts in string from left 0--------n

str5 = "Saharsa_Engineering_college"
ch = str5[2]
print(ch)
print(str5[5])

# Slicing -> Accessing parts of a String but ending index doesn't included

str6 = "Hey brother"
print(str6[1:6]) # so here only before the ending index number excuted and printed

print(str6[1:len(str6)]) # using lenth of string we can go last of the string
print(str6[:5]) # didn't given startin value tell we start with zero and end based on given number
print(str6[2:]) # didn't given value tell we start with given value and end on last according to string value

# nigative indexing -> starts ends of string from -1 to first on string -n..

str7 = "Apple"

print(str7[-3:-1])

print("------------------ String Functions -----------------------------------")

# endswith()  -> returns true if string ends with given substring

str8 = "I am studing python from Apna college"
print(str8.endswith("ege"))
print(str8.endswith("aef"))

# capitalize()  -> It capitalize the first characters

str9 = "hey man what are you doing."
print(str9.capitalize()) # it capitalize only for one time printing
print(str9) # The origional string didn't changed

# if you want to permanantly change so you have to do this

str9 = str9.capitalize()
print(str9) # now it is permanently changed
print(str9)


# replace() -> replace old occurance of old string

str10 = "I am studying Python From Youtube"
print(str10.replace("Python", "JavaScript"))

# find() -> returns 1st index of first occur

str11 = "I am doing job in Aiosell technology in bangalore"
print(str11.find("0"))   # if the searches character/word didn't match it returns -1 as output
print(str11.find("in"))

# count()  -> count the occurance of substr

print(str11.count("in"))