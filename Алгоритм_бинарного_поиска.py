import time 
a=[i for i in range(1,1000000)]
k=687345
def search(a,k):
    for i in range(len(a)):
        if a[i]==k:
            return i
    return -1 
timen=time.time()
print(search(a, k))
print(time.time()-timen)

def speed_search(a,k):
    right=a[len(a)-1]
    left=a[0]
    while right>left+1:
        middle=(left+right)//2
        if a[middle]<k:
            left=middle
        else:
            right=middle
    return a[left]
time1=time.time()
print(speed_search(a, k))
print(time.time()-time1)
    