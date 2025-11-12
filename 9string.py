fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])  # automatic bhabe 0 bosaiya nibe
print (fruit[:])   # automatic bhabe 0 ar length bosabe 
# print(fruit[0:-3]) eitare [0: lenght -3 ] dhorbe
# print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3]) # doesnt make sence ,cuz length -1 --> 4 and length -3 -->2 so [4:2] 
print(fruit[-3:-1]) #[2:4]

# Quick Quiz:
# nm = "Harry"
print(fruit[-4:-2])
# @codewithharry
