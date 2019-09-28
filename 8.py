a= [1,2,3,4,5]
print(*a,sep=", ")
b=input("What number do you want to delete(Head/Tail): ").upper()
if b=="HEAD":
    a.remove(a[0])
    print(*a,sep=", ")
if b=="TAIL":
    a.remove(a[4])
    print(*a,sep=", ")

