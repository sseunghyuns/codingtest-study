n = 5
money = [3, 2, 1, 1, 9]
print(money)

impossible_sum = 0
for i in range(1, sum(money)+1):
    
    if i in money:
        impossible_sum = i+1
        continue
    
    print(i)