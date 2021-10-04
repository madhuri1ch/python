l=[1,2,-10,4,-3,0,3,4,5]

current_sum=l[0]
max_sum=l[0]

for num in l[1::]:
    current_sum=max(current_sum,num+current_sum)
    max_sum=max(current_sum,max_sum)
    if 

print(max_sum)