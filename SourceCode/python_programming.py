#!/usr/bin/env python
# coding: utf-8

# In[1]:


#assigning values to variables
counter = 100
miles = 1000.0
name = "John"

print(counter)
print(miles)
print(name)


# In[3]:


#multiple assignment
a = b = c = d = 1
e,f,g = 2,3,"John"
print(a, b, c, d, e, f, g)


# In[5]:


strKata = "Hello World!"
print(strKata)
print(strKata[0])
print(strKata[2:5])
print(strKata[2:])
print(strKata * 2)
print (strKata + "TEST")


# In[6]:


list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list1)          # Prints complete list
print(list1[0])       # Prints first element of the list
print(list1[1:3])     # Prints elements starting from 2nd till 3rd 
print(list1[2:])      # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list1 + tinylist) # Prints concatenated lists


# In[7]:


tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple1)           # Prints complete list
print(tuple1[0])        # Prints first element of the list
print(tuple1[1:3])      # Prints elements starting from 2nd till 3rd 
print(tuple1[2:])       # Prints elements starting from 3rd element
print(tinytuple * 2)   # Prints list two times
print(tuple1 + tinytuple) # Prints concatenated lists


# In[8]:


dict1 = {}
dict1['one'] = "This is one"
dict1[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(dict1['one'])       # Prints value for 'one' key
print(dict1[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values


# In[9]:


#decision
#single statement suites
var = 100
if ( var == 100 ) : print("Value of expression is 100")
print("Good bye!")


# In[10]:


#String formatting operator
print("My name is %s and weight is %d kg!" % ('Zara', 21))


# In[11]:


'''
%c	character
%s	string conversion via str() prior to formatting
%i	signed decimal integer
%d	signed decimal integer
%u	unsigned decimal integer
%o	octal integer
%x	hexadecimal integer (lowercase letters)
%X	hexadecimal integer (UPPERcase letters)
%e	exponential notation (with lowercase 'e')
%E	exponential notation (with UPPERcase 'E')
%f	floating point real number
%g	the shorter of %f and %e
%G	the shorter of %f and %E

'''


# In[12]:


print('C:\\nowhere')


# In[13]:


list1 = ['physics', 'chemistry', 1997, 2000];
print("Value available at index 2 : ")
print(list1[2])
list1[2] = 2001;
print("New value available at index 2 : ")
print(list1[2])


# In[14]:


list1 = ['physics', 'chemistry', 1997, 2000];
print(list1)
del list1[2];
print("After deleting value at index 2 : ")
print(list1)


# In[15]:


tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print(tup3);


# In[16]:


tup = ('physics', 'chemistry', 1997, 2000);
print( tup)
del tup;
print("After deleting tup : ")
print(tup)


# In[17]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

