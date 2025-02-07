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
    z=a
    y="a"
    b=int(input("Enter num2: "))
    if b>z:
        z=b
        y="b"
    c=int(input("Enter num3: "))
    if c>z:
        z=c
        y="c"
    # return (a,b,c)
    return y

def main():
    # (a,b,c)=get_input()
    # x=maxi(a,b,c)
    x=get_input()
    display(x)
main()