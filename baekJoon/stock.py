import sys 
if __name__ == "__main__":
    t=int(input())

    ans=[]
    tmp=0
    def get_max(array,n):
        global tmp
        index=0
        # while array:
        #     max_num=max(array)
        #     index=array.index(max_num)
        #     for i in range(index):
        #         tmp+=(max_num-array[0])
        #         array.pop(0)
        #     array.pop(0)    
        max_num=max(array)
        for i in range(n):
            #print(max_num)
            if array[i]==max_num:
                array[i]=0
                max_num=max(array[i:n])
            else:
                tmp+=(max_num-array[i])    
        #print(tmp)    


    for i in range(t):
        n=int(input())
        array=list(map(int,sys.stdin.readline().split()))
        tmp=0
        get_max(array,n)
        print(tmp)
    #print(ans)    

