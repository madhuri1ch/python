nums=[1,2,3,4,5,6]

def my_gen(nums):
    for n in nums:
        yield n*n

my_g=my_gen(nums)

for i in my_g:
    print(i)

    '''1
4
9
16
25
36'''

#usig comprehension


my_ge=(n*n for n in nums)

for i in my_ge:
    print(i)

    '''1
4
9
16
25
36'''

