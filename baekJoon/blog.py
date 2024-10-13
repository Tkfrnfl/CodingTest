if __name__ == "__main__":
    n,x = map(int, input().split())

    arr =list(map(int, input().split()))
    ans=[]
    mx =0
    cnt =0

    sm = sum(arr[0:0+x])

    for i in range(0,n-x+1):
        if i>0:
            sm-=arr[i-1]
            sm+=arr[i+x-1]
        if sm>mx:
                mx=sm
                cnt=1
        elif sm==mx:
                cnt+=1    

    ans.append(mx)
    ans.append(cnt)
    
    if mx==0:
        print('SAD')   
    else:    
        for i in ans:
            print(i)
    #sad