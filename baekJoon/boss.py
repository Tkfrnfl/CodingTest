#-*- coding:utf-8 -*-

if __name__=="__main__":
    n,m,i=map(int,input().split())

    array_age=list(map(int,input().split()))
    
    node=[[0]*2 for i in range(n+1)]

    Inf=int(1e9)
    for _ in range(m):
        a,b=map(int,input().split())

        if node[a][0]==0:
            node[a][0]=b
        else:
            node[a][1]=b 

    input_list=[]
    for _ in range(i):
       input_list.append(list(map(str, input().split())))


    def P(num):                         
        tmp=Inf

        for j in range(1,n+1):
            if node[j][0]==num or node[j][1]==num:
                tmp=min(tmp,array_age[j-1])

                tmp=min(tmp,P(j))
        # if tmp==Inf:
        #     tmp='*'
        return tmp        

    for j in range(i):
        if input_list[j][0]=='P':
            num=int(input_list[j][1])
            tmp=P(num)
            if tmp==Inf:
                tmp='*'
            print(tmp)
        elif input_list[j][0]=='T':
            num1=int(input_list[j][1])
            num2=int(input_list[j][2])

            tmp1=node[num1]
            tmp2=node[num2]
            node[num1]=tmp2
            node[num2]=tmp1
            for k in range(1,n+1):
                if node[k][0]==num1:
                    node[k][0]=num2
                elif node[k][1]==num1:
                    node[k][1]=num2   
                elif node[k][0]==num2:
                    node[k][0]=num1 
                elif node[k][1]==num2:
                    node[k][1]=num1     

            #print(node)
