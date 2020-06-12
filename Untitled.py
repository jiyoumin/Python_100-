#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[17]:


import turtle as t
t.shape('turtle')
t.color('blue', 'green')
t.begin_fill()
t.fd(200)
t.left(120)
t.fd(200)
t.left(120)
t.fd(200)
t.end_fill()
t.exitonclick()


# In[11]:


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# In[54]:


import turtle as t
t.shape('turtle')
t.color('blue', 'red')
t.begin_fill()
t.right(72)
t.fd(100)
t.left(72)
t.fd(100)
t.right(72)
t.fd(100)
t.left(72)
t.fd(100)
t.right(72)
t.fd(100)
t.left(72)
t.fd(100)
t.end_fill()
t.exitonclick()


# In[ ]:


import turtle as t
t.shape('turtle')
t.color('blue', 'red')
t.begin_fill()

n=int(input('몇각형??'))

for i in range(n*5):
    for i in range(n):
        t.fd(200)
        t.left(360/n)
    t.right(180/n)  
t.end_fill()
t.exitonclick()

