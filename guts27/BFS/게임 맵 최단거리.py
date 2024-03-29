from collections import deque
def solution(maps):
    global answer
    answer = 1e9
    dx,dy = [-1,0,1,0],[0,1,0,-1]
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
            elif maps[nx][ny] > 1 and maps[nx][ny] > maps[x][y] + 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
        
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
