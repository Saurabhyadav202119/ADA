def knapsack(W_bag,s_a):
    s_a=sorted(s_a,key=lambda i:i[1],reverse=True)
    result=0
    for item in s_a:
        if item[0]<W_bag:
            W_bag=W_bag-item[0]
            result=result+item[1]
    return (result)    

# takes input size of the bag
W_bag=int(input("Enter the bag size:"))  
# takes input weights of each item 
wt_item=input("Enter the weight of the items:").split()
# takes input profits of each item
wt_item=[int(item) for item in wt_item]
val_item=input("Enter the value of the item:").split()
val_item=[int(item) for item in val_item]
# sort
s_a=[[wt_item[i],val_item[i]] for i in range(3)]
print (s_a)
print(knapsack(W_bag,s_a))