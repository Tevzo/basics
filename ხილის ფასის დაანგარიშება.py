

fruit = {}

while True:
     if len(fruit) == 0:
         helper = {}
         name = str (input ("enter fruit name: "))
         kg = float (input ("enter fruit weight: "))
         price = float (input ("enter fruit price: "))
         helper["kg"] = kg
         helper["price"] = price
         fruit[name] = helper
     else:
         print("this is your cart", fruit)
         ques = input("add more? yes/no: ")
         if ques == "yes":
             helper = {}
             name = input ("enter fruit name: ")
             kg = input ("enter fruit weight: ")
             price = input ("enter fruit price: ")
             helper["kg"] = kg
             helper["price"] = price
             fruit[name] = helper
         else:
            break
result = 0
for key,value in fruit.items():
    kg = int(value["kg"])
    price = int(value["price"])
    result += kg*price
    print(key, "your amount", kg*price, "GEL")
print ("you have to pay", result, "GEL")
