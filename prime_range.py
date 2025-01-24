import math
def is_prime(n):
    flag=True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            flag=False
            break
    return flag

def main():
    num=int(input("Enter the end number"))
    count=0
    for i in range(2,num):
        check=is_prime(i)
        if check==True:
            print(f"{i} is prime number")
main()