#!/usr/bin/env python
# coding: utf-8

# # How we can print strings?
# ## Let's start!
# 

# In[1]:


print("faizan")


# In[2]:


print("faizan is learning python with spirit!")


# In[17]:


data = "Name = Faizan \nClass = BS CS \nAge = 21" #write strings using " "

print(data)


# In[16]:


data = 'Name = Faizan \nClass = BS CS \nAge = 21' #write strings using ''

print(data)


# In[29]:


data = """ 
        Name  =\t  Faizan 
        Class =\t  BS CS 
        Age   =\t  21
        
        """
                    #""" """ triple double quotes are used to write multi line strings
print(data)          
                


# In[39]:


data = """
        Name  =\t Faizan
        Class =\t BS CS
        Age   =\t 21

        """
print(data.expandtabs(30))  #.expandtabs() is used to add additional tab spaces 


# # Let's create a variable
# 

# In[34]:


age = 21
print ("Faizan's age is",age)


# In[35]:


name = "Faizan Yousaf"
print("My name is", name)


# ## Let's see how we can concatinate variables and strings

# In[ ]:


# 1
Name = "Faizan Yousaf"
Class = "BS CS"
Age = 21
University = "UAF"
print(Name, Class, Age,University)


# In[43]:


# 2
Name = "Faizan Yousaf"   
Class = "BS CS "
Age = 21
University = "UAF"
#in jupyter, It returns the last variable value when you write the variable name without 
    #using print fuction;
        
# University
Age


# In[62]:


# 3
Name = "Faizan Yousaf"   
Class = "BS CS "
Age = 21
University = "UAF"
#we used "+" sign to combine variables and strings
    
print( "Your name is "+ Name +"\nYour class is "+ Class +"\nYour age is "+ str(Age) + "\nYou study at "+ University)


# In[69]:


# 3
Name = "Faizan Yousaf"   
Class = "BS CS "
Age = 21
University = "UAF"
#we can concatinate using .format() function
data = """
        Your name is = {}
        Your class is = {}
        Your age is =  {}
        You study at = {}
""".format(Name , Class, Age , University)
   #         0     1      2       3
print(data)       


# In[73]:


# 4
Name = "Faizan Yousaf"   
Class = "BS CS "
Age = 21
University = "UAF"

data = """
            Your name is {3}
            Your class is {0}
            Your age is {1}
            You study at {2}
        """.format(Class , Age , University , Name)
            #        0      1      2           3 
                   #we used .format fucntion with indexes to print out values of variables
print(data)


# In[74]:


# 5
Name = "Faizan Yousaf"   
Class = "BS CS "
Age = 21
University = "UAF"
 
data = f"""
            Your name is {Name}
            Your age is {Age}
            Your class is {Class}
            You study at {University}
            """
  #SIMPLEST    #just write 'f' after assignment operator and in '{}' write variable name;
print(data)


# # Let's see how we can use string ".functions"

# ## String Methods

# In[2]:


Name = "Faizan Yousaf"   
Class = "BS CS "
Age = 21
University = "UAF"
 
data = f"""
            Your name is {Name}
            Your age is {Age}
            Your class is {Class}
            You study at {University}
            """
                                  #SIMPLEST    #just write 'f' after assignment operator and in '{}' write variable name;
print(data)


# In[3]:


print(data)


# In[7]:


name = "Faizan Yousaf"
print(name)


# # capitalize function()

# In[16]:


name = "faizan yousaf"
name.capitalize()


# # casefold function()

# In[25]:


name = "Faizan yousaf"
print("faizan yousaf" == "faIZaN yousaf")  #false


name.casefold() =="faIZaN yousaf".casefold() #true


# # center function()

# In[27]:


name = "Faizan yousaf"
name.center(70)


# # strip function()

# In[30]:


name = "           Faizan yousaf        "

name.lstrip()


# In[31]:


name = "           Faizan yousaf        "

name.rstrip()


# In[34]:


name = "Faizan yousaf"
name.center(70)
name.strip()


# # cout function()

# In[46]:


name = "Faizan yousaf"
name.count('f')


# # encode function()

# In[54]:


name = "faizan yousaf"  #utf stands for Universal Transformation format 

name.encode('utf-16')


# # endswith function()

# In[61]:


name = "faizan yousaf"
name.endswith("f")        #true
name.endswith("saf")      #true
name.endswith("yousaf")   #true
# name.endswith('an')     #false


# # expandtabs function()

# In[4]:


name = "\tfaizan \t Yousaf"
print(name)
name.expandtabs(20)  #it adds additional tab spaces


# In[3]:


data = """
    name =\t faizan 
    class =\t Bs
    age =\t 21
    uni =\t UAF
            """
print(data.expandtabs(24))


# # find function()

# In[78]:


name = "faizan yousaf"

name.find('y')        #it tells us the index number of the string

name.find('a',5)      #to specify from which index number you want to start from!!!!


# # format function()

# In[9]:


name = "faizan"
grade = "BS"
age = 21
uni = "UAF"

data = """
    name = {} 
    class = {}
    age = {}
    uni = {}
        """
print(data.format(name,grade,age,uni))



# In[12]:


name = "faizan"
grade = "BS"
age = 21
uni = "UAF"

data = f"""
    name = {name} 
    class = {grade}
    age = {age}
    uni = {uni}
        """
print(data)


# # format_map function()

# In[20]:


data = {"a" : "faizan",     #dictionary
        "b" : "Yousaf"}

print("Name: {a} \nFather name: {b}".format_map(data))


# # index function()

# In[25]:


name = "Faizan"
name.index('a')
# name.index("a", 3)  #same as find funtion


# In[24]:


name = "Faizan"

name.index("a", 3)  #same as find funtion


# # isalnum function()

# In[26]:


name = "faizan"
name.isalnum()


# In[27]:


name = "faizan3"  #it will be true for both alphabets and numbers
name.isalnum()


# In[28]:


name = "faizan3$"  #if it contains any special symbol then it is false
name.isalnum() 


# # isalpha function()

# In[29]:


name = "faizan"
name.isalpha()


# In[30]:


name = "faizan22"       #it will false when any number or symbol is entered
name.isalpha()


# In[31]:


name = "faizan$2"      #it will false when any number or symbol is entered
name.isalpha()


# # isascii function()

# In[33]:


name = "faizan"
name.isascii()


# In[35]:


name = "faizan21"
name.isascii()


# # isdecimal function()

# In[38]:


name = "0"               #decimal = 0,1,2,3,4,5,6,7,8,9
name.isdecimal()


# In[39]:


name = "3"
name.isdecimal()


# In[40]:


name = "422"
name.isdecimal()


# In[41]:


name = "21.1"      #it returns false if we enter a floating point value

name.isdecimal()


# # isdigit function()

# In[43]:


name = "0"
name.isdigit()


# In[45]:


name = "3242"
name.isdigit()


# In[46]:


name = "0.2"
name.isdecimal()


# # isidentifier function()

# In[53]:


name = "faizan"          #it is false when we violate any rule of writing/initializing variables
name.isidentifier()


# In[52]:


name = "faizan_asdlk"    #spaces are not allowed while writing variable names, so we use "_"
name.isidentifier()


# In[55]:


name = "1faizan"          #it is false when we violate any rule of writing/initializing variables

name.isidentifier()


# # islower function()

# In[56]:


name = "Faizan"    #.islower() tells us if the string is lowercase or not!
name.islower()


# In[57]:


name = "faizan"
name.islower()


# In[62]:


name = "Faizan".casefold()

print("Faizan" == "faizan") #false

print(name.casefold()) # .casefold() makes the string content lowercase

name.islower()    #.islower() tells us if the string is lowercase or not!


# # lower function()

# In[63]:


name = "FaIzAn"
name.lower     # lower function()


# # isascii function()

# In[33]:


name = "faizan"
name.isascii()


# In[33]:


name = "faizan"
name.isascii()


# # isnumeric function()

# In[64]:


name = "21"
name.isnumeric()


# In[65]:


name = "21.3"
name.isnumeric()


# # istitle function()

# In[66]:


name = "faizan"
name.istitle()


# In[68]:


name = "Faizan Yousaf"
name.istitle()


# In[69]:


name = "Faizan yousaf"
name.istitle()


# # title function()

# In[70]:


name = "faizan yousaf"
name.title()


# # isspace function()

# In[76]:


name = " "     # Return True if the string is a whitespace string, False otherwise.

name.isspace()


# # strip function()

# In[77]:


name = "    faizan yousaf   "
name.strip()


# # rstrip function()

# In[82]:


name = "       faizan       " 
name.rstrip()


# # lstrip function()

# In[83]:


name = "       faizan       " 
name.lstrip()


# # isupper function()

# In[85]:


name = "FAIZAN"      #Return True if the string is an uppercase string, False otherwise
name.isupper()


# In[87]:


name = " F"
name.isupper()


# In[86]:


name = "Faizan"
name.isupper()


# In[84]:


name = "faizan"
name.isupper()


# # join function()

# In[95]:


list = ('1','2','3','4','5')
'+'.join(list)  .join()


# In[96]:


name= ('F','a','i','z','a','n')
''.join(name)


# In[98]:


name= ('F','a','i','z','a','n')
'-'.join(name)


# In[100]:


name= ('F','a','i','z','a','n')
'()'.join(name)


# In[102]:


list1 = ['f','a','z','i']
print("  ".join(list1))


# In[103]:


#Joining string character to string
'S'.join('12345')


# In[104]:


#Joining special symbols with string
'()'.join('12345')


# In[105]:


#Joining digits with string
'100'.join('Geeks')


# In[108]:


name =  ("f",'a','z','i')
'_'.join(name)


# In[109]:


name = ("faizan", "yousaf")
'_'.join(name)


# In[106]:


#Joining special character with dictionary
'_'.join({'Geek':1,'For':2,'Geeks':3})


# In[107]:


name =  ("f",'a','z','i')
'+)_+'.join(name)
name.


# # rjust function()

# In[116]:


name = "                                     faizan"
name.rjust(32)


# # ljust function()

# In[ ]:


name = "faizan     "
name.ljust(65)


# # replace function()

# In[120]:


name = "faizan"
name.replace('a','p')


# In[124]:


name = "faizan"
name.replace('a','W', 1)


# In[127]:


name = "faizan"
name.replace('a','W', 2)


# # maketrans function()

# In[136]:


name = "faizan"
name.maketrans()


# # partition function()

# In[149]:


name = "faizan is learning python"    #Partition the string into three parts using the given separator.
name.partition('is')


# In[145]:


name = "faizan is learning python"  #if the seperator is not found,then it prints the whole line in one
                                    #line and write other 2 in empty quotes
name.partition('not')                


# # isprintable function()

# In[146]:


name = "faizan"           #Return True if the string is printable i.e alphabets, numbers, spaces, symbols
name.isprintable()


# In[147]:


name = "faizan#$"            
name.isprintable()


# In[148]:


name = "faiz \n an"      #false in this case
name.isprintable()


# # upper function()

# In[154]:


name = "faizan yousaf"
name.upper()


# # isupper function()

# In[158]:


name = "FAIZAN"
name.isupper()


# # removeprefix function()

# In[159]:


name = "faizan is not a good student"
name.removeprefix("faizan")


# In[162]:


name = "faizan is not a good student"
name.removeprefix("f")


# # removesuffix function()

# In[164]:


name = "faizan is not a good student"
name.removesuffix("student")


# In[ ]:




