#-*- coding:utf-8 -*-


if __name__ == "__main__":
    a,b=map(int,input().split())

    ans=0

    def countOne(num):

        n=num
        one_num=0

        while n>1:
            q=n//2
            r=n%2
            if r==1:
                one_num+=1
            n=q

        if n==1:
            one_num+=1

        return one_num        
    
    for i in range(a,b+1):
        ans+=countOne(i)

    print(ans)    