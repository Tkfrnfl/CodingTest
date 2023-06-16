#-*- coding:utf-8 -*-

def c_check(list,c):
    if c in list:
        return True
    else:
        return False

if __name__ == "__main__":
    n,d,k,c=map(int,input().split())
    array=[]
    ans=0
    ans_list=[]
    for i in range(n):
        tmp=int(input())
        array.append(tmp)
    array.extend(array[0:k])        #순환구조 생각하여 extend
    for i in range(k):              #초기 k개 설정
        ans_list.append(array[i])
    
    #print(array)
    tmp_set=set(ans_list)
    if c_check(tmp_set,c):
        ans=len(tmp_set)
    else:
        ans=len(tmp_set)+1

    for j in range(len(array)-k):
        ans_list.append(array[len(ans_list)+j])   
        ans_list.pop(0)
        tmp_set=set(ans_list)
        if c_check(tmp_set,c):
            ans=max(ans, len(tmp_set))
        else:
          ans=max(ans, len(tmp_set)+1)

    print(ans)             
