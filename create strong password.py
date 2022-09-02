a=input("enter number")
i=0
while i<len(a):
    if len(a)<16:
        if "$" in a[i] and "8" or "2" in a[i] and "A" or "Z" in a[i]:
            print("strong password")
        i+=1
    else:
       print("weak password"