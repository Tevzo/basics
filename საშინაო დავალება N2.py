#1
x = int(input("input number:"  ))
y = int(input("input number:"  ))

result_1 = int( x/y )
result_2 = ( y%x )


print (result_1)
print (result_2)


#2

x = int(input("input number:"))
y = int(input("input number:"))
z = int(input("input number:"))

result_1 = (x*y*z)
result_2 = (x+y+z)

print (result_1)
print (result_2)

#4
number = input("enter number:")

result = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])

print (result)


#5
result = 0
for i in range(len(number)):
    result = result + int(number[i])

print (result)
