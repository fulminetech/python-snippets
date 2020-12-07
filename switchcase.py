a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

def add(a, b):
    return int(a+b) 

def xyz(x):
    switcher = {
        'addition':add(a,b),
        'multiplication':a*b,
        'subtraction':a-b,
        'division':a/b
    }
    return switcher.get(x,"Oops! Invalid Option")


result=xyz('addition')
print("Result:",result)