def find_max(l):
    m = l[0]
    for i in range(1,len(l)):
        if (l[i]>m): m = l[i]
    print("The max munber is:",m)
def find_min(l):
    m = l[0]
    for i in range(1,len(l)):
        if (l[i]<m): m = l[i]
    print("The min munber is:",m)
a = list(map(int, input().split()))
find_max(a)
find_min(a)
