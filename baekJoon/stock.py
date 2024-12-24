import sys 
if __name__ == "__main__":
    t=int(input())

    ans=[]
    tmp=0
    def get_max(array,n):
        global tmp
        index=0

        max_num=array[n-1]
        profit=0

        array.reverse()

        # for i in range(n):
        #     if array[i]<max_num:
        #         profit+=max_num-array[i]
        #     elif array[i]>=max_num and i<n-1:
        #         max_num=max(array[i+1:])

        for i in range(n):
            if array[i]>max_num:
                max_num=array[i]
            else:
                profit+= max_num-array[i]    

        tmp=profit        

    for i in range(t):
        n=int(input())
        array=list(map(int,input().split()))
        tmp=0

        get_max(array,n)
        print(tmp)


