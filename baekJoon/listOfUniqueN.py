if __name__ == "__main__":
    n= int(input())
    arr=list(map(int, input().split())) 

    num_list=[0]*100001


    left=0
    result =0

    for i in range(n):
        num_list[arr[i]]+=1


        while num_list[arr[i]]>1:
            num_list[arr[left]]-=1
            left+=1


        result+= (i-left)+1
    print (result)        