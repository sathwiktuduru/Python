def display(avg):
    print(f"Average is {avg}")

def input_s():
    # length=int(input("Enter the length"))
    # width=int(input("Enter the Width"))
    # return (length,width)
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    return (a,b,c,d)

def calculate(a,b,c,d):
    # area=length*width
    # return area
    avg=(a+b+c+d)/4
    return avg
def Main():
    # (length,width)=input_s()
    # area=calculate(length,width)
    (a,b,c,d)=input_s()
    avg=calculate(a,b,c,d)
    display(avg)    
    
Main()