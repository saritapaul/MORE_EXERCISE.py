#input ka use kar ke 3 alag variables mein 3 integers ka input lein. 
# Input lene ke baad inn 3 mein se sabse bade number ko print karo.
a=int(input("enter 1 st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b and a>c:
    print("1st number is greater",a)
elif b>a and b>c:
    print("2 nd number is greater",b)
else:
    print("3rd number is greater",c)

