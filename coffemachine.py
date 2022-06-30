
# coffe vending machine code - Leticia Smith Aldama

def selection_type_of_coffe():
    global TypeCoffe
    if option == 1:
        TypeCoffe = coffe1
        print("The price is ..", TypeCoffe["price"])
    if option == 2:
        TypeCoffe = coffe2
        print("The price is ..", TypeCoffe["price"])
    if option!= 1 and option!= 2:
        print("Choose correctly your option of Coffe")

def askMoney():
    global money
    print("\nType of Money accepted --> $100 or $200 ")
    money = int(input("\n Pay for your product -->$ "))
    print("\n--------------------------------")
    while (money<TypeCoffe["price"]):
        money=int(input("Use $100 or $200"))
    if (money == 100 or money == 200):
        CoffePreparation()
        RestofMoneyDeliver()
    else:
        askMoney()

def RestofMoneyDeliver():
    rest_Money = money - TypeCoffe["price"]
    print("\nThe rest of the money is: ", rest_Money, "$")
    print("\nPlease take the rest of your money back")

def CoffePreparation():
    print("\nYour coffe is being prepared..")
    print()
    print("Please wait a moment...")
    print("\nYour Coffe is Ready! =D\n")
    print("\n-----------------------------------------\n")

def addCoffeList(indice):
    count=indice+1
    coffeList.insert(indice,count)


# starting

coffe1 = {"type":"Cappuccino", "price":60}
coffe2 = {"type" :"Moka","price":80}
coffeList = []
indice = 0
answer = "yes"
while answer == "yes":
    #menu with the types of coffe
    print("\n\n - - - -MENU- - - -\n\n\n")
    print("Type of Coffe 1  \n\n", coffe1["type"], " - - -> The Price is: ", coffe1["price"])
    print("\nType of Coffe 2  \n\n" , coffe2["type"], " - - -> The Price is: ", coffe2["price"])
    print("\n-----------------------------------")
    option = int(input("\n\nChoose your option of Coffe: "))
    if option == 1:
        TypeCoffe = coffe1
        askMoney()
        addCoffeList(indice)
        indice=indice+1
        print("\nIf you want more cups of coffe, write yes")
        print("\nIf you want to finish the process press any key...")
        answer=str(input(""))
    if option == 2:
        TypeCoffe=coffe2
        askMoney()
        addCoffeList(indice)
        indice=indice+1
        print("\nIf you want more cups of coffe, write yes")
        print("\nIf you want to finish the process press any key...")
        answer=str(input(""))
    if option!=1 and option!=2:
        print("\nWrite correctly your option again")

    print("\nThe Coffees boughts are: ", coffeList)
    print("\n * * * * Thanks and Fuck you * * * * ")


