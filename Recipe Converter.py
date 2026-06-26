def gt_c():
    gm=float(input("Enter full amount of grams of the ingredient"))
    cups=float(input("enter how many cups you want to use"))
    return gm/cups

def cut_g():
    cup=float(input("How much cups u got"))
    grams=float(input("Enter the amount of grams in each cups"))
    return cup*grams



while True:
    print("Welcome to recipe converter")
    print("1.How many grams do u want in each cup")
    print("2.Total number of grams in each cup")
    print("3.tablespoon to teaspoon")
    print("4.Exit")
    opt=input("Enter your choice(1-4)")
    if opt =="1":
        result=gt_c()
        print(f"you need to put {result}g in each cup")
    elif opt=="2":
        resul=cut_g()
        print(f"The amount in all cups is {resul}g")
