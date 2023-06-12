import math
def sumOfThree(num: int):
      di=num/3
      print(math.modf(di)[0])
      result=[]
      print(f'di={di},type={type(di)}')
      if  math.modf(di)[0]==0:
          i=int(math.modf(di)[1])
          print('inside')
          result.append(i-1)
          result.append(i)
          result.append(i+1)
      return result
      
print(sumOfThree(33))
        