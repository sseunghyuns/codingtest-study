input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

# 이동할 방향 정의
steps = [(-1,2),(1,2), (-1,-2), (1,-2), (-2,-1), (-2,1), (2,-1), (2,1)]
result=0
for step in steps:
  move_x, move_y = row + step[0], column+step[1]
  if move_x<1 or move_x>8 or move_y<1 or move_y>8:
    continue
  result+=1
print(result)