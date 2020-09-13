#!/usr/bin/env python
# coding: utf-8

# In[5]:


lst=[1,1,5]
lst1=[]
l=int(input("enter the length of the list:"))
j=0
for i in range(0,1):
    lst1.append(int(input("enter the elements of the list:")))
    print()
    print("list is:",lst1)
for i in range(0,1):
        if(lst1[i]==lst[j]):
            j+=1
            i+=1
        else:
            i+=1
if (j==3):
      print("its a match")
else:
    print("its gone")
  


# In[6]:


#prime number between 1-2500 using filter
def prime (i):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            return i
primeno=filter(prime,range(1,2500+1))
print("prime no between 1-2500:")
print(list(primeno))


# In[8]:


#capatilization the statement with lambda and map
lst=["hey this is anjali","i am from odisha"]
print("the list is:")
print(lst)
result=list(map(lambda words:"".join([word.capitalize()for word in words.split()]),lst))
print("capitalized list is:")
print(result)


# In[ ]:




