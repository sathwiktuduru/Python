# list=[]
# for i in range(1,11):
#     number=int(input("Enter the number: "))
#     list.append(number)
# print("The elements in list are")
# print(list)

#Empty list
# list1=[]
# print("The List is empty: ",list1)

# #List with four items
# list2=[1, 2, 3, 4]
# print("List with 4 items: ",list2)

# #Nested list
# list3=["list1", ["list2", "list3"]]
# print("Nested list: ",list3)

# #List containing string
# list4=["Strings"]
# print("List with string: ",list4)

# #list with range
# list5=list(range(-2,3))
# print("List in range of(-2, 3): ",list5)

# #accessing element from a nested list
# list6=["x",["z", "y"], "w"]
# print("An element in nested list:",list6[1][0])


# l1=[5, 2, 1, 2, 8, 6, 3]
# sum=0
# for i in l1:
#     sum += i
# print(sum)
# l1.sort()
# print("Smallest element is: ",l1[0])
# print("Largest element is: ",l1[6])

def smallest_largest(l1):
    minn=l1[0]
    maxi=l1[0]
    for i in l1:
        if minn>i:
            minn=i
        elif maxi<i:
            maxi=i
    return (minn,maxi)

def main():
    l1=[5, 2, 1, 2, 8, 6, 3]
    (minn,maxi)=smallest_largest(l1)
    print(f"Smallest number is: {minn}, Largest number is {maxi}")
main()
