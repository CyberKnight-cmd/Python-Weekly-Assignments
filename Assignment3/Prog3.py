a,b,c = map(float,input("Enter a number : ").split(','))
if(a<b and a<c):
    print(a,"is the smallest")
if(b<a and b<c):
    print(b,"is the smallest")
else:
    print(c,"is the smallest")