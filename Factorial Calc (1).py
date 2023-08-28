#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[25]:


## calc. factorial of n through loop

n=int(input("Enter the number"))
x=1
v=0
if n>-1:
    for i in range(1,n):
        x*=n
        n=n-1
    print(x)
else:
    if n%2==0:
        v=abs(n)
        for i in range(1,v):
            x*=v
            v=v-1
        print(x)
    else:
        z=abs(n)
        for i in range(1,z):
            x*=z
            z=z-1
        print(-1*x)


# In[24]:


## works only for positive integers


# In[ ]:




