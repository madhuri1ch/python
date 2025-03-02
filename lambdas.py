"""
lambda is a function without a name , use and trow 

lambda takes an input and does something and returns output

"""

x=lambda i:i+2

print(x(2)) #prints 4

y=(lambda x:x.upper())
print(y('abc')) #prints ABC

"""
map() takes a function and iterable(s) as input and applies the function to all the elements of the iterable 
    1.  If additional iterables arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. 
    2. 

"""

y=(map(lambda x:x.upper(),['abc','ccd'])) 
print(y) #<map object at 0x000001D84426BD90>
print(list(y)) #['ABC', 'CCD']

y=(map(lambda x,y:[x.upper(),y.upper()],['abc','ccd'],['xyz','est'])) 

print(list(y)) #[['ABC', 'XYZ'], ['CCD', 'EST']]

y=(map(lambda x,y:[x.upper(),y.upper()],['abc','ccd'],['xyz'])) 

print(list(y)) #[['ABC', 'XYZ']]
 
