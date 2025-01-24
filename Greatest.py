def display(x):
    print(f"Max is {x}")

def maxi(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c

def get_input():
    a=int(input("Enter num1: "))
    b=int(input("Enter num2: "))
    c=int(input("Enter num3: "))
    return (a,b,c)

def main():
    (a,b,c)=get_input()
    x=maxi(a,b,c)
    display(x)
main()