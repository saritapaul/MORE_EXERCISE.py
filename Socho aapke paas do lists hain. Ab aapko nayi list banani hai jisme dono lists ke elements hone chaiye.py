#Socho aapke paas do lists hain. Ab aapko nayi list banani hai jisme dono .
# lists ke elements hone chaiye.
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
new_list=[ ]
while i<len(list1):
    if list1[i] not in list2:
        new_list.append(list1[i])
    i+=1
j=0
while j<len(list2):   
    new_list.append(list2[j])    
    j+=1    
#new_list.sort()    
print(new_list  
            