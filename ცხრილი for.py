numbers = "1234567"

result = 0
for i in numbers:
    result = (result + int(i))* (result+ int(i))
    print(result, "i", i , "numbers" ,i )

print ("saboloo",(result))
