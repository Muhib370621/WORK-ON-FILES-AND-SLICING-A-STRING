#!/usr/bin/env python
# coding: utf-8

# # PRACTICE PROBLEM 4.1:

# In[1]:


#A
s= '0123456789'
print(s[2:6])


# In[3]:


#B
s= '0123456789'
print(s[7:9])


# In[7]:


#C
s= '0123456789'
print(s[1:8])


# In[8]:


#D
s= '0123456789'
print(s[:4])


# In[9]:


#E
s= '0123456789'
print(s[7:10])


# # PRACTICE PROBLEM 4.2:

# In[11]:


#A
forecast='It will be a sunny day today'
x=forecast.count('day')
print(x)


# In[13]:


#B
forecast='It will be a sunny day today'
x=forecast.find('sunny')
print(x)


# In[14]:


#C
forecast='It will be a sunny day today'
x=forecast.replace('sunny','cloudy')
print(x)


# # PRACTICE PROBLEM 4.3:

# In[15]:


last='Smith'
first='John'
middle='Paul'
print(last,first,middle,sep='   ')


# # PRACTICE PROBLEM 4.4:

# In[9]:


def even(x):
    for i in range(2,x+1):
        if i%2==0 or i%3==0:
            print(i,end=' ')
even(16)
        


# # PRACTICE PROBLEM 4.5:

# In[5]:


first='John'
last='Doe'
street='Main Street'
number='123'
city='Anycity'
state='AS'
zipcode='09876'
var='{} {}\n{} {}\n{} \n{} {}'
print(var.format(first,last,number,street,city,state,zipcode))


# # PRACTICE PROBLEM 4.6:

# In[2]:


students=[]
students.append(['DeMoines','Jim','Sophomore',3.45])
students.append(['Pierre','Sophie','Sophomore',4.0])
students.append(['Columbus','Maria','Senior',2.5])
students.append(['Phoenix','River','Junious',2.45])
students.append(['Olympis','Edgar','Junious',3.99])
def roaster(students):
    print('Last     First      Class      Average Grade')
    for i in students:
        print('{:10}{:10}{:10}{:8.2f}'.format(i[0],i[1],i[2],i[3]))
roaster(students)

    


# # PRACTICE PROBLEM 4.7:

# In[49]:


import time
t=time.localtime(1500000000)
def strftime(x):
    print('%A, %B %d %Y',t)
time.strftime('%A, %B %d %Y',time.localtime())


# In[55]:


#B
import time
t=time.localtime(1500000000)
def strftime(x):
    print('%I:%M %p %Z on %a/%B/%d',t)
time.strftime('%I:%M %p %Z on %a/%B/%d',time.localtime())


# In[56]:


#C
import time
t=time.localtime(1500000000)
def strftime(x):
    print('I will meet you on %a %B at %I:%M %p',t)
time.strftime('I will meet you on %a %B at %I:%M %p',time.localtime())


# # PRACTICE PROBLEM 4.8:

# In[2]:


def stringcount(filename,target):
    infile=open(filename)
    content=infile.read()
    infile.close
    return content.count(target)
print(stringcount('x.txt','sunny'))


# # PRACTICE PROBLEM 4.9:

# In[6]:


def words(filename):
    infile=open(filename,'r')
    content=infile.read()
    infile.close()
    table=content.maketrans('!,.:;?',6*' ')
    content=content.translate(table)
    content=content.lower()
    return content.split()
words('4.9.txt')
    


# # PRACTICE PROBLEM 4.10:

# In[8]:


def mygrep(filename,target):
    infile=open(filename)
    for i in infile:
        if target in i:
            print(i,end='      ')
mygrep('example.txt','line')
    
    


# # PRACTICE PROBLEM 4.11:

# In[11]:


#A
print('4/0 ')
print('It is not possible beacuse the error is maths error in which non zero number cant devide by zer0')


# In[12]:


#B
print('lst[14,15,16]')
print('lst[3]')
print('The error occurs beacuse index 3 is not possible in lst its maximum index will be 2..')


# In[13]:


#C
print('x+5')
print('The error comes beacuse we have not given or defined the value of x')


# In[16]:


#D
print("'2'*'3'")
print('The error ocuurs because we dont write 2 and 3 in int sequence we use'' this tells us that sequence cant be multiplied')


# In[19]:


#E
print("int('4.5')")
print('The reason for this error is that we use int function instead of using float')


# In[ ]:




