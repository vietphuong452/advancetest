a=[1,2,3,4,5]
print(*a,sep=",")
b=input("So moi: ")
a.insert(0,b)
print(*a,sep=",")