#reverse each word of a string
x = input("enter string: ")
y= ""
i=len(x)-1
while i>=0:
    y+= x[i]
    i-=1
    print(y)
