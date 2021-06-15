list1=[2,15,3,24,30,10,18,7]
i=0
while i<len(list1):
    if list1[i]%3==0 and list1[i]%5==0:
        list1[i]="fizzbuzz"
    elif list1[i]%3==0 and list1[i]%2==0:
        list1[i]="fizz"
    elif list1[i]%5==0:
        list1[i]="buzz"
    i+=1
print(list1)