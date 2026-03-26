

def add(a,b):
    return a+b
def sub(a,b):
    return a - b 
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
while True:
  try:
    a = int(input("enter the first number"))
    b = int(input("enter the second number"))
    break
  except ValueError :
       print("you have enter wrong type")
       
    
    # b = int(input("enter the second number"))
operation = {
        1:add,
        2 :sub,
        3 :mult,
        4 : div
    }

while True :
    print("\n"+"_"*40)
    print("   choice   ")
    print("_"*40)
    print("1 is add")
    print("2 is sub")
    print("3 si mult")
    print("4 is div")
    print("5 exit")
    try:
        choice = int(input("enteryour choice"))
        if choice == 5 :
            print("Exit")
            break
        elif  choice in operation:
            print("Result",operation[choice](a,b))
        else:
            print("invalid number")
            
    except ValueError :
        print("only number")
    

    