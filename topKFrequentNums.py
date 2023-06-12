'''
ALGO
1. store the num and its number of occurance as a key(num) and value(occurance) 
in dict
2. covert the dict into a tuple with (value,key) and using heapq get nlargest elements get the result
3. covert resulted tuple into array and return

'''
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        l=len(nums)
        if l<k:
            return 0
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
    
        h= [(v,k) for k,v in d.items()]
        import heapq
        lar=heapq.nlargest(k,h)
        result=[]
        for i in range(k):
            result.append(lar[i][1])
        return result