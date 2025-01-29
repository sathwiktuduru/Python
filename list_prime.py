import math
def is_prime(n):
    flag=True
    # for i in range(2,int(math.sqrt(n)+1)):
    i=2
    while(i<int(math.sqrt(n)+1)):
        if n%i==0:
            flag=False
            break
        i=i+1
    return flag

def main():
    num=int(input("Enter the end number"))
    count=0
    l1=[]
    for i in range(2,num):
        check=is_prime(i)
        if check==True:
            l1.append(i)
    print(l1)
main()



