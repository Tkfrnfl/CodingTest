#-*- coding:utf-8 -*-
def solution(key, lock):

    m=len(key[0])
    n=len(lock[0])

    key0=[]
    lock_list90=[]
    lock_list180=[]
    lock_list270=[]

    lock_list=[]
    lock_list_spin=[]
    lock_list_spin90=[]
    lock_list_spin180=[]
    lock_list_spin270=[]
    # 열쇠 모양 체크
    for i in range(m):
        for j in range(m):
            if key[i][j]==1:
                key0.append((i,j))
                # key90.append((j,m-1-i))
                # key180.append((m-1-i,m-1-j))
                # key270.append((m-1-j,i))
    #자물쇠 빈공간 체크
    for i in range(n):
        for j in range(n):
            if lock[i][j]==0:
                lock_list.append((i,j))
                lock_list90.append((j,m-1-i))
                lock_list180.append((m-1-i,m-1-j))
                lock_list270.append((m-1-j,i))
            else:
                lock_list_spin.append((i,j))    
                lock_list_spin90.append((j,m-1-i))
                lock_list_spin180.append((m-1-i,m-1-j))
                lock_list_spin270.append((m-1-j,i))

    answer = False

    x=[0,0,1,-1]
    y=[1,-1,0,0]
    # 맞는지 체크
    for i in range(-18,18):
        for j in range(-18,18):
            tmp=0
            for idx,val in enumerate(lock_list):
                if (val[0]+i,val[1]+j)in key0:
                    tmp+=1           
            if tmp==len(lock_list):     #열쇠구멍 맞을시 돌기 체크
                spin_check=True
                for idx,val in enumerate(lock_list_spin):
                    if (val[0]+i,val[1]+j)in key0:  
                        spin_check=False
                if spin_check:                                     
                    return spin_check       
            tmp=0
            for idx,val in enumerate(lock_list90):
                if (val[0]+i,val[1]+j)in key0:
                    tmp+=1
            if tmp==len(lock_list):
                spin_check=True
                for idx,val in enumerate(lock_list_spin90):
                    if (val[0]+i,val[1]+j)in key0:  
                        spin_check=False
                if spin_check:                                     
                    return spin_check       
            tmp=0    
            for idx,val in enumerate(lock_list180):
                if (val[0]+i,val[1]+j)in key0:
                    tmp+=1
            if tmp==len(lock_list):
                spin_check=True
                for idx,val in enumerate(lock_list_spin180):
                    if (val[0]+i,val[1]+j)in key0:  
                        spin_check=False
                if spin_check:                                     
                    return spin_check        
            tmp=0    
            for idx,val in enumerate(lock_list270):
                if (val[0]+i,val[1]+j)in key0:
                    tmp+=1
            if tmp==len(lock_list):
                spin_check=True
                for idx,val in enumerate(lock_list_spin270):
                    if (val[0]+i,val[1]+j)in key0:  
                        spin_check=False
                if spin_check:                                     
                    return spin_check       


    #print(answer)
    return answer

    
if __name__ == "__main__":
	solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])        