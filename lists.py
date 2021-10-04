#lists are mutable



courses=['history','math','physics','chem']
lang=['eng','sans']
print(courses)
print(courses[0])
print(courses[-1])# prints last item
print(courses[0:2])# index 0 is included and index 2 is not inclided
print(courses[0:])#['history', 'math', 'physics', 'chem']
print(courses[:-2])#['history', 'math']
print(courses[-2:]) #['physics', 'chem']

print(courses.append('social'))# returns non and appaends social
print(courses)#['history', 'math', 'physics', 'chem', 'social']

#print(courses.append(lang))# returns non
#print(courses)#['history', 'math', 'physics', 'chem', 'social', ['eng', 'sans']]

print(courses.extend(lang))# returns non 
print(courses)#['history', 'math', 'physics', 'chem', 'social', ['eng', 'sans'], 'eng', 'sans']

courses.remove('math')
print(courses)# 'history', 'physics', 'chem', 'social', ['eng', 'sans'], 'eng', 'sans']

print(courses.pop())#removes last index and retrurn the item removed
print(courses)

nums=[1,2,3,4]
print(nums.reverse()) #reversse the existing list adnd returns none
print(nums) #[4, 3, 2, 1]

print(nums.sort()) # modifies the existing list to store data in ascending order and returns none
print(nums)

print(nums.sort(reverse=True))# modifies the existing list to store data in descending order and returns none
print(nums)

print(sorted(nums))# does not modifies the existing list  and returns  a new list [1, 2, 3, 4]
print(nums)
print(sorted(nums,reverse=True))# does not modifies the existing list  and returns  a new list [4, 3, 2, 1]

print(sum(nums))# returns 10

print(max(nums))# 4

print(courses.index('physics')) # returns index of input value

print('physics' in courses) # returns true 

for course in courses:
    print(course)

    '''istory
physics
chem
social
['eng', 'sans']
eng'''

for index,course in enumerate(courses):
    print(index,course)

    '''(0, 'history')
(1, 'physics')
(2, 'chem')
(3, 'social')
(4, ['eng', 'sans'])
(5, 'eng')'''

for index,course in enumerate(courses,start=1): #starts index from 1
    print(index,course)

    '''(1, 'history')
(2, 'physics')
(3, 'chem')
(4, 'social')
(5, ['eng', 'sans'])
(6, 'eng')'''

course_str=', '.join(courses)
print(course_str) #history, physics, chem, social, engs

new_list=course_str.split(', ')
print(new_list) #['history', 'physics', 'chem', 'social', 'eng']

#tuples are immutable

#sets 
#order is not garintied
#no duplicates 
courses={'math','math','physics','science'}
lang={'eng','sans','physics'}

print(courses)# set(['science', 'physics', 'math'])
print(courses.intersection(lang)) #set(['physics'])
print(courses.union(lang))#set(['sans', 'eng', 'science', 'physics', 'math'])
print(courses.difference(lang)) #set(['science', 'math'])