#given list of stock prices for each day find the index to buy and index to sell for max profit

prices=[10,9,8,7]

buy=0
largest=0
i=1
l=len(prices)
cur_profit=0
final_buy=0
final_sell=0

while i<l:
    if prices[buy]>=prices[i]:   
        buy=i
        if(largest==0):
            final_buy=i
               
    else:
        if (prices[i]-prices[final_buy])>cur_profit:
            final_sell=i
            cur_profit=prices[i]-prices[buy]
            if(buy<final_sell):
                final_buy=buy
 
    i+=1

print("buy:{},sell:{},profit:{}".format(final_buy,final_sell,cur_profit))


