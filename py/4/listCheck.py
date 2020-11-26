# ................. programm is written in python ...................

# creating an empty list.. 
lst = [] 
  
# asking for the number of elements in list (length of list)
length = int(input("Enter number of elements : ")) 
  

# taking input and appending to the list one by on
for i in range(0, length): 
    element = int(input()) 
    lst.append(element) # adding the element 


# choosing the max element in the list
max = max(lst)
# choosing the min element in the list
min = min(lst)


# printing the result..
if((length > 1) & ((max-min) == 5) ):
    print("True")
else:
    print("False")

      