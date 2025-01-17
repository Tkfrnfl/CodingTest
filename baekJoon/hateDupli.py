# -*- coding:utf-8 -*-
from collections import defaultdict

if __name__ == "__main__":
    n, k = map(int, input().split())
    array = list(map(int, input().split()))

    dict = defaultdict(int)
    start=0
    ans=0

    cnt=0
    for i in range(n):
        dict[array[i]]+=1

        while dict[array[i]]>k:
            dict[array[start]]-=1
            if dict[array[start]]==0:
                del dict[array[start]]
            start+=1    
        ans=max(ans,i-start+1)

    print(ans)        