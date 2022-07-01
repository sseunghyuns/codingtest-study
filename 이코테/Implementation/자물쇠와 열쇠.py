def rotate(array): # (2,3)
    
    n_row = len(array) # 2
    n_col = len(array[0]) # 3
    
    rotated = [[0]*n_row for _ in range(n_col)]  # (3,2)
    
    for i in range(n_row): # 2
        for j in range(n_col): # 3
            rotated[j][n_row-i-1] = array[i][j] #### 
            # (0)
    return rotated

def can_unlock(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):    
    n_lock = len(lock)
    n_key = len(key)
    
    new_lock = [[0]*(n_lock*3) for _ in range(n_lock*3)]
    
    # 값 채워넣기
    for i in range(n_lock):
        for j in range(n_lock):
            new_lock[i+n_lock][j+n_lock] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for r in range(4):
        key = rotate(key) # 회전됨
        
        # 슬라이딩 윈도우 방식으로 끼워넣기
        for i in range(n_lock*2):
            for j in range(n_lock*2):
                for x in range(n_key):
                    for y in range(n_key):
                        new_lock[i+x][j+y] += key[x][y]
                if can_unlock(new_lock):
                    return True
                for x in range(n_key):
                    for y in range(n_key):
                        new_lock[i+x][j+y] -= key[x][y]

            
    return False