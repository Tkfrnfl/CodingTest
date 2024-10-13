import copy

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans=0


    for i in range(n):
        start= 0
        end = n-1
        now= arr[i]

        while start<end:
            if start==i:
                start+=1
                continue
            if end==i:
                end-=1  
                continue  

            total = arr[start] + arr[end]
            if total<now:
                start+=1
    
            elif total>now:
                end-=1  

            else: 
                ans+=1
                break


    print(ans) 