if __name__ == "__main__":
    n= int(input())
    arr=list(map(int, input().split())) 
    m =int(input())
    ask_arr = [list(map(int, input().split())) for _ in range(m)]
    
    d=[]
    p=[]

    def pali(i):
        global arr
        count =0
        for j in range(i):
            if i-1-j>=0 and i+1+j<n and arr[i-1-j]==arr[i+1+j]:
                count+=1
            else:
                break
        return count        

    i = 0
    while i < n:
        cnt = pali(i)

        if cnt > 0:
            d.append(i)
            p.append(cnt)
        i+=1


    ans=[]

    for i in ask_arr:
        a= i[0]-1
        b= i[1]-1
        mid= (a+b)//2
        size= (b-a)//2

        if a==b:
            ans.append(1)
            continue
        if (b-a)%2 ==1:
            ans.append(0)
            continue
        if mid in d and size <= p[d.index(mid)]:
            ans.append(1)
            continue
        ans.append(0)        
    # print(d)
    # print(p)    

    for i in ans:   
        print(i)        
