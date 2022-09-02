#4.Write a program which accept N numbers from user and store it into List. Accept one another 
#number from user and return frequency of that number from List. 
def frequency_of_items_in_list(l): 
    d={} 
    for i in l: 
        c=l.count(i) 
        d[i]=c 
    return d 
 
n=int(input("Enter the size of your desired list:")) 
l=[];print() 
for i in range(n): 
    x=int(input(f"Enter the {i+1} element of the list:")) 
    l.append(x) 
print("The list entered by the user is",l) 
print() 
s=frequency_of_items_in_list(l) 
for k,v in s.items(): 
    print("The number",k,"appeared",v,"times in the list",l) 