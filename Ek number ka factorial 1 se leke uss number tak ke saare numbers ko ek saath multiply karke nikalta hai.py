#Ek number ka factorial 1 se leke uss number tak ke saare numbers ko ek 
# saath multiply karke nikalta hai.
num=int(input("enter number"))
i=1
fact=1
while i <=num:
    fact=fact*i
    i+=1
print(fact)