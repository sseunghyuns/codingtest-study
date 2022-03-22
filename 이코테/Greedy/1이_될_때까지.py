n, k = map(int, input().split())

#######
# 단순 풀이
counter=0

while True:
  if n ==1:
    break
  
  if n%k==0:
    n /=k
    counter+=1
  else:
    n-=1
    counter+=1

print(counter)

#######
# N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식
counter = 0
while True:
  target = (n//k) * k
  # 예를들어 n=18, k=4이면, target을 16으로 만들어준다.
  # 이떄, 18 -> 16으로 가야하기 때문에 1을 2번씩 빼주는 작업을 수행해야하는데 이를 아래와 같이 한번에 계산한다
  counter += (n-target)
  n = target

  # n이 k보다 작을 때 반복문 탈출
  if n < k:
    break
  
  # k로 나누기
  n //= k
  counter+=1

# 마지막으로 남은 수에 대하여 1씩 빼기
# n=4이면, 반복문 돌 필요 없이 3을 단순히 빼주면 된다
counter += (n-1) 
print(counter)