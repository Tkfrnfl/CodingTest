import sys
sys.setrecursionlimit(3000)

answer =''
def dfs(n, m, x, y, r, c, k,d,ans,dx,dy):
    global answer
    if k-d<abs(r-x)+abs(c-y):
        return 

    
    if x==r and y==c and k==d:
        answer =ans
        return 
    
    directions = ['d', 'l', 'r', 'u']
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if answer == '' and 1 <= xx <= n and 1 <= yy <= m:
            dfs(n, m, xx, yy, r, c, k, d + 1, ans + directions[i], dx, dy)


def solution(n, m, x, y, r, c, k):

    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    
    if (k-abs(r-x)-abs(c-y))%2==1 or abs(r-x)+abs(c-y)>k:
        return "impossible"


    dfs(n, m, x, y, r, c, k,0,answer,dx,dy)
    return answer


if __name__ == "__main__":
	solution(3,4,2,3,3,1,5)  