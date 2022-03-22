n, m = map(int, input().split())
weight = list(map(int, input().split()))

'''
나의 풀이
'''
# count = 0
# for i in range(len(weight)):
#     for j in range(i+1, len(weight)):
#         if weight[i]!=weight[j]:
#             count+=1 
# print(count)


'''
이코테 풀이
A가 먼저 번호가 작은 공부터 차례대로 선택했을 떄 각각의 케이스에 대한 번호 조합을 구한다.
문제에서 무게 m의 범위가 1이상 10이하라고 명시했기 때문에, weight_total이라는 무게를 index로 하는 리스트를 만들어 해당 무게의 볼링공의 개수 정보를 입력할 수 있다.
이를 활용하면 이중 for문을 돌았던 나의 풀이보다 훨씬 효율적으로 코드를 작성할 수 있다.
'''
weight_total = [0]*(11)

for i in weight:
    weight_total[i]+=1

count = 0
for i in range(1, len(weight_total)):
    n -= weight_total[i]
    count += weight_total[i]* n
print(count)
