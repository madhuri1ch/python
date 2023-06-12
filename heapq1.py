
import heapq

a=[10,2,4,7,1,10,3]
print(a)

print(heapq.heapify(a))
print(a)

for i in range(len(a)):
    print(heapq.heappop(a))

