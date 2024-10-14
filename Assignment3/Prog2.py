a,b,c = map(float,input("Enter a number : ").split(','))
if(a>b and a>c):
    print(a,"is the greatest")
if(b>a and b>c):
    print(b,"is the greatest")
else:
    print(c,"is the greatest")