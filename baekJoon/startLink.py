from itertools import combinations
import copy

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]


    comb= list(combinations(range(n),n//2))    
    all_list = [i for i in range(n)]

    ans =int(1e9)

   
    for com in comb:
        com_r = copy.deepcopy(all_list)
        start=0
        link=0

        for i in com:
            com_r.remove(i)
            for j in com:
                start+=arr[i][j]

        for k in com_r:
            for l in com_r:
                link+=arr[k][l]

        ans=min(ans,abs(start-link))                

    print(ans)