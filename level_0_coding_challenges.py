#!/usr/bin/env python
# coding: utf-8

# # Task 0.1

# In[5]:


x = 0
y = 1
print(x)
print(y)


# In[6]:


x = x + 3
y = y + x
print(x)
print(y)


# # Task 0.2

# In[3]:


x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + (1 * 2)
a = 1 + 1 * 2 / 2
b = (1 + 1 * 2) / 2
print(x,y,z,a,b)


# # Task 0.3

# In[17]:


def hello(name):
    print("Hello" + " " + name)


# In[18]:


hello("Decclan")


# # Task 0.4

# In[23]:


def even_or_odd(integer):
    if integer %2 == 0:
        print("even")
    elif integer %2 != 0:
        print("odd")


# In[27]:


even_or_odd(121)


# # Task 0.5

# In[29]:


def area_of_a_triangle(base, height):
    return (base * 0.5) * height


# In[31]:


area_of_a_triangle(6,3)


# # Task 0.6

# In[74]:


def maximum(int1,int2,int3):
    if int1 > int2 :
        return int1
    elif int1 > int3:
        return int1
    elif int2 > int3:
        return int2
    else:
        return int3


# In[76]:


maximum(6,3,4)


# In[86]:


def maximum(int1,int2,int3,int4):  #add int.. to parameter and edd elif int.. arguement to function
    if int1 > int2 :
        return int1
    elif int1 > int3:
        return int1
    elif int2 > int3:
        return int2
    elif int4 > int3:
        return int4
    else:
        return int3


# In[91]:


maximum(1,22,3,2)


# # Task 0.7

# In[95]:


def convert_c_to_f(celsius):
    return celsius * (9/5) +32     


# In[97]:


convert_c_to_f(100)


# In[102]:


def convert_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


# In[103]:


convert_f_to_c(212)


# # Task 0.8

# In[387]:


def time_conversion(number):
    hour = number // 60
    mins = (number % 60)
    time = hour + mins
    string_hour = str(hour)
    string_min = str(mins)
    if hour <= 1:
        print(string_hour + " " + "hour")
    else:
        print(string_hour + " " + "hours")
    if mins <= 1:
        print(string_min + " " + "minute")
    else:
        print(string_min + " " + "minutes")      


# In[393]:


time_conversion(122)


# # Task 0.9

# In[498]:


def vowel_grab(string):
    string = string.lower()
    for vowel in "aeiou":
        if vowel in string:
            print(vowel)


# In[500]:


vowel_grab("missisipayee")


# # Task 0.10

# In[533]:


def comparison_func(string1,string2):
    string1 = string1.lower()
    string2 = string2.lower()
    for letters in string1 and string2:
        if letters in string1 and string2:
            print(letters)
    


# In[534]:


comparison_func('house',"computers")

