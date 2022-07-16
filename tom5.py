def binarySearch(list1,Key):
    low=0
    high=len(list1)-1
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if Key==list1[mid]:
            found=True
        elif Key>list1[mid]:
            low=mid+1
        else:
            high=mid-1
    if found == True:
        print("element is found")
    else:
        print("element is found")
list1=eval(input("Enter elements of list:"))
list1.sort()
print("sorted array:",list1)
Key=int(input("Enter the Key:"))
count=list1.count(Key)
print("occurance of Key is:",count)
binarySearch(list1,Key)
