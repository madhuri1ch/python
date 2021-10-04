nums=[1,2,3,4,5,6,7]

new_list=[]
for num in nums:
    new_list.append(num)

print(new_list) #[1, 2, 3, 4, 5, 6, 7]

new_list1=[ n for n in nums]
print(new_list1) #[1, 2, 3, 4, 5, 6, 7]

new_list2=map(lambda n:n*n, nums) #[1, 4, 9, 16, 25, 36, 49]
print(new_list2)

even_nums=[n for n in nums if n%2==0]
print(even_nums) #[2, 4, 6]

even_nums=map(lambda n:n%2==0, nums) #[False, True, False, True, False, True, False]
print(even_nums)

even_nums=filter(lambda n:n%2==0, nums) #[False, True, False, True, False, True, False]
print(even_nums) #[2, 4, 6]

two_lists=[(letter,num) for letter in 'ab' for num in '012'] #[('a', '0'), ('a', '1'), ('a', '2'), ('b', '0'), ('b', '1'), ('b', '2')]
print(two_lists)

#two_lists=map(lambda n:(n,n),  '012')# [('a', '0'), ('a', '1'), ('a', '2'), ('b', '0'), ('b', '1'), ('b', '2')]
#print(two_lists)

print(zip('ab','012')) #[('a', '0'), ('b', '1')]

di={letter:num for letter,num in zip('ab','012')}
print(di) #{'a': '0', 'b': '1'}

di={letter:num for letter,num in zip('ab','012') if num !='0'} #{'b': '1'}
print(di)