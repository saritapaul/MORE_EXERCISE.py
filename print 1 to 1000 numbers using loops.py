# using loop run the code 1 to 1000, if number is divisible by 3 print "nav",if number is divisible by 
#7 print"gurukul",if number is divisible by 21 print"navvgurukul".
i=1
while i<=1000:
    if i%21==0:
        print("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
      print("gurukul")
    i+=1