#!/usr/bin/env python
# coding: utf-8

# # QUESTION-4.12:

# In[1]:


#A
s='abcdefghijklmnopqrstuvwxyz'
x=s[1:4]
print(x)


# In[2]:


#B
s='abcdefghijklmnopqrstuvwxyz'
x=s[:3]
print(x)


# In[3]:


#C
s='abcdefghijklmnopqrstuvwxyz'
x=s[3:24]
print(x)


# In[5]:


#D
s='abcdefghijklmnopqrstuvwxyz'
x=s[22:25]
print(x)


# In[7]:


#E
s='abcdefghijklmnopqrstuvwxyz'
x=s[22:26]
print(x)


# # QUESTION-4.13:

# In[10]:


#A
s='abcdefghijklmnopqrstuvwxyz'
x=s[1:3]
print(x)


# In[12]:


#B
s='abcdefghijklmnopqrstuvwxyz'
x=s[:14]
print(x)


# In[15]:


#C
s='abcdefghijklmnopqrstuvwxyz'
x=s[14:26]
print(x)


# In[17]:


#D
s='abcdefghijklmnopqrstuvwxyz'
x=s[1:23]
print(x)


# # QUESTION 4.14:

# In[ ]:





# # QUESTION 4.15:

# In[12]:


#A
s='10 20 30 40 50 60'
x=s.split(' ')
print(x)


# In[13]:


#B
s='10,20,30,40,50,60'
x=s.split(',')
print(x)


# In[14]:


#C
s='10&20&30&40&50&60'
x=s.split('&')
print(x)


# In[15]:


#D
s='10-20-30-40-50-60'
x=s.split('-')
print(x)


# # QUESTION 4.16:

# In[24]:


def dictionary(a,b,c):
    d={'a':'bass','b':'salmon','c':'whitefish'}
    print('Enter first word : ',a)
    print('Enter second word : ',b)
    print('Enter third word : ',c)
    if (a and b and c) in d.values():
        print('True')
    else:
        print('False')
dictionary('bass','salmon','whitefish')


# # QUESTION 4.17:

# In[25]:


message='The secret of this message is that it is secret'
length=len(message)
count=message.count('secret')
censored=message.replace('secret','xxxxx')
print(message)
print(length)
print(count)
print(censored)


# # QUESTION 4.18:

# In[34]:


s='''It was the best of times, it was the worst of times;it was the age of wisdom,it was the age of foolishness;it was the epoch of belief,it was the epoch of incredulity; it was...'''
x=s.replace(';','      ')
print(x)


# # QUESTION 4.19:

# In[40]:


#A
first='Marlena'
last='Sigel'
middle='Mae'
print('{}, {} {}'.format(last,first,middle))


# In[38]:


#B
first='Marlena'
last='Sigel'
middle='Mae'
print('{}, {} {}.'.format(last,first,middle[0]))


# In[41]:


#C
first='Marlena'
last='Sigel'
middle='Mae'
print('{} {}. {}'.format(first,middle[0],last))


# In[45]:


#D
first='Marlena'
last='Sigel'
middle='Mae'
print('{}. {}. {}'.format(middle[0],middle[0],last))


# In[44]:


#E
first='Marlena'
last='Sigel'
middle='Mae'
print('{}, {}.'.format(last,middle[0]))


# # QUESTION 4.20:

# In[47]:


sender='tim@abc.com'
recipient='ton@xyz.org'
subject='Hello!'
print('From: {} \n To: {} \n Subject: {}'.format(sender,recipient,subject))


# # QUESTION 4.21:

# In[64]:


#A
from math import pi
print('{:1.1f}'.format(pi))
print('{:1.1e}'.format(e))


# In[66]:


#B
from math import pi
print('{:1.2f}'.format(pi))
print('{:1.2e}'.format(e))


# In[68]:


#C
from math import pi
print('{:e}'.format(pi))
print('{:e}'.format(e))


# In[70]:


#D
from math import pi
print('{:1.5f}'.format(pi))
print('{:1.5f}'.format(e))


# # QUESTION  4.22:

# In[7]:


def month(x):
    temp = 'JanFebMarMayJunJulAugSepOctNovDec'
    x=temp[(x-1)*3:x*3]
    return x
month(2)
        


# # QUESTION 4.23:

# In[78]:


def average():
    a=3
    b=4
    x=(a+b)/2
    print('Enter a sentance: ','A sample sentence')
    print(x)
average()


# # QUESTION 4.24:

# In[82]:


def cheer(Huskies):
    a='How do you spell winner'
    b='I know! I know'
    c='H U S K I E S'
    d='And thats how you spell winner'
    e='Go Huskies'
    print('{}? \n {}! \n {} ! \n {}! \n {}!'.format(a,b,c,d,e))
cheer('Huskies')


# # QUESTION 4.25:

# In[7]:


def vowelcount(x):
    vow='AEIOUaeiou'
    a = 0
    e = 0
    y = 0
    o = 0
    u = 0
    for i in x:
        if i in vow:
            if i == 'a' or i == "A":
                a += 1
            if i == 'e' or i == "E":
                e += 1
            if i == 'i' or i == "I":
                y += 1
            if i == 'o' or i == "O":
                o += 1
            if i == 'u' or i == "U":
                u += 1
    print('a, e, i, o, u appears {} {} {} {} {}'.format(a,e,y,o,u))
vowelcount("sarim")


# # QUESTION 4.26:

# In[2]:


def crypto(x):
    infile=open(x)
    r = infile.read()
    y = r.replace('secret','xxxxx')
    infile.close()
    return y
crypto('4.26.txt')


# # QUESTION 4.27:

# In[10]:


def fcopy(file1,file2):
    infile1=open(file1,'r')
    content=infile1.read()
    infile1.close()
    infile2=open(file2,'w')
    infile2.write(content)
    infile2.close()
fcopy('4.27_1.txt','4.27_2.txt')
    
    


# # QUESTION  4.29:

# In[17]:


def stats(filename):
    infile=open(filename,'r')
    text=infile.read()
    no_of_lines=text.count('\n')+1
    no_of_words=len(text.split())
    no_of_character=len(text)-no_of_lines+1
    print('Line count : ',no_of_lines)
    print('Word count : ',no_of_words)
    print('Character Count : ',no_of_character)
stats('4.27_2.txt')
    


# # PRACTICE PROBLEM 4.30:

# In[11]:


def distribution(filename):
    infile=open(filename,'r')
    content=infile.read()
    infile.close()
    print(content.count('A'),'students got A')
    print(content.count('A-'),'students got A-')
    print(content.count('B+'),'students got B+')
    print(content.count('B-'),'students got B-')
    print(content.count('C'),'students got C')
    print(content.count('C-'),'students got C-')
    print(content.count('F'),'students got F')
distribution('grades.txt')
    


# # QUESTION 4.31:

# In[16]:


def duplicate(filename):
    c=0
    infile=open(filename,'r')
    content=infile.read()
    splt=content.split()
    infile.close()
    for i in splt:
        if (splt.count(i))>1:
            return False 
            c=1
        if c!=1:
             return True
duplicate('4.27_1.txt')
    


# # QUESTION 4.32:

# In[19]:


def censor(filename):
    infile=open(filename,'r')
    content=infile.read()
    word=content.split()
    infile.close()
    for i in word:
        if (len(i)==4):
            text=content.replace(i,"****")
    outfile=open("cencored.txt",'w')
    outfile.write(text)
    outfile.close()
censor('example.txt')
    
               


# In[ ]:




