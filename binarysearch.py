def binarySearch(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag=0
    count=0
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2
        if(x==mid):
            flag=1
            print("The element found at the position:"+str(mid))
            print("The no of iteration:"+str(count))
            return
        else:
           if(x<mid):
              last_pos=mid-1
           else:
               first_pos=mid+1
    print("The no does not present")
a=[]
for i in range(1001):
    a.append(i)
binarySearch(a,70)
               