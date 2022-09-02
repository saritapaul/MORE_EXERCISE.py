#Harshad numbers aise number hote hain jo apni digits ke sum se dhang se divide hote hain.
# Dhang se divide hone ka matlab ki remainder 0 aata hai. 
# Jaise 42 ek Harshad number hai kyunki 4 + 2 = 6 aur 42 ko 6 se vidie kar ke remainder aata hai.
# def harshad_no(number):
#     i=0
#     s=str(number)
#     while i<len(s):
#         j=0
#         t=str(number)
#         b=str(t[i])
#         while j<len(b):
#             d=str(b)
#             e=0
#             c=0
#             while e<len(d):
#                 c=int(d[e]+c)
#                 e+=1
#             j+=1
#     i+=1
#     if number%c==0:
#         print("True")
#     else:
#         print("False")
# harshad_no(21)
def harshad_no(number):
    digit=list(str(number))
    i=0
    sum=0
    while i<len(digit):
        sum=int(digit[i])+sum
        a=str(digit[i])
        b=int(a)
        i+=1
    if b%sum==0:
        print("True")
    else:
        print("False")
harshad_no(42)
