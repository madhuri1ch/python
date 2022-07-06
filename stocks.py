#find the max differnce but any 2 elements in a given array
#find hte max profile for single stock buy and stock sell


def findmaxprofit(prices):
    max_profit=prices[1]-prices[0]
    min_ele=prices[0]
    final_buy=min_ele
    final_sell=prices[1]
    for i in range( 1, len(prices) ):
        if(prices[i]-min_ele)>max_profit:
            max_profit=prices[i]-min_ele
            final_buy=prices.index(min_ele)
            final_sell=i


        if prices[i]<min_ele:
            min_ele=prices[i]

    return max_profit,final_buy,final_sell

arr = [10,7,2,6,5,18,1]

print(findmaxprofit(arr))
