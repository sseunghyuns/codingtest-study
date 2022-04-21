'''
30분안에 못풀어서, 다시 한번 30분 타이머 놓고 도전
조금 더 깔끔한 코드+풀이를 고민해보기
'''

# 맨해튼 거리가 2 이하인 경우를 모두 체크
def get_p(place):
    info = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                info.append((i,j))
    return info

def get_l1(x1, x2):
    return abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])

'''
거리두기 실패 경우
1. 일직선상에 있을 경우
    1.1 x축-
    1.2 y축-
2. 대각선에 있을 경우
    사이에 모두 X 존재해야함. 

'''
def check(place, x1, x2): #(0,0), (0,1)같이 한칸만 떨어져 있는 경우?
    # 1. 일직선상
    if x1[0]==x2[0]: # 같은 x축에 있을 때 : (0,0), (0,1)
        min_y = min(x1[1], x2[1]) # 0
        
        for i in range(abs(x1[1]-x2[1])-1):   # range(0) -> 돌지 않음. 따로 조건 처리해줘야 할듯          
            
            if place[x1[0]][min_y+i+1] in ['O', 'P']:
                return False

    elif x1[1]==x2[1]: # 같은 y축에 있을 때 
        min_x = min(x1[0], x2[0])
        for i in range(abs(x1[0]-x2[0])-1):    
            if place[min_x + i+1][x1[1]] in ['O', 'P']:
                return False            
    else : # 대각선 -> 사이에 P가 있어도 거리두기 지켜지지 않고 있는 것.
        if x1[0]> x2[0]:
            greater = x1
            smaller = x2
        else:
            greater = x2
            smaller = x1
        
        if place[smaller[0]][greater[1]] in ['O', 'P'] or place[greater[0]][smaller[1]] in ['O', 'P']:
            return False
            
    return True
        

def solution(places):
    answer = []
    for idx, place in enumerate(places):
        # 시작
        info = get_p(place) # 모든 P의 좌표가져오기
        flag=True # 거리두기 지켜지고 있는지
        
        for i in range(len(info)): # 모든 P끼리 서로 비교
            for j in range(i, len(info)): 
                if i == j:
                    continue
                dist = get_l1(info[i], info[j])
                if dist <= 2: # 맨해튼 거리가 2 이하일 때
                    if dist == 1: #### -> (0,0), (0,1)같이 한칸만 떨어져 있는 경우에는 무조건 거리두기 지켜지지 않고 있음.
                        flag=False
                        break
                    elif not check(place, info[i], info[j]): # 거리두기를 지키지 않으면
                        flag=False
                        break
            else: # Nested for loop에서 조건 만족하면 break 하기
                continue
            break
                        
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer