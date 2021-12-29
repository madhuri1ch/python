from heapq import heappop,heappush
    
def hotel(arrive, depart, K):
    arrive.sort()
    print(arrive)
    depart.sort()
    print(depart)
    rooms=[]
    heappush(rooms, depart[0])
    rooms_cnt=1
    for arr in arrive[1:]:
        print(arr)
        if rooms[0]<=arr:
            heappop(rooms)
        else:
            rooms_cnt+=1
            heappush(rooms,)
            if rooms_cnt>K:
                return False
    return True
A = [ 1, 2, 3, 4 ]
B = [ 10, 2, 6, 14 ]
C = 4
print(hotel(A,B,C))
    
