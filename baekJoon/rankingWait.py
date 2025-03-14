# -*- coding:utf-8 -*-

if __name__ == "__main__":
    p,m = map(int, input().split())
    array = []

    for i in range(p):
        lv,id=map(str, input().split())
        array.append((int(lv),id))

    room=[[]for _ in range(p)]

    for arr in array:
        for ro in room:
            # 빈방이면 첫유저 등록
            if ro==[]:
                ro.append(arr)
                break
            #아니라면 조건체크
            else:
                if ro[0][0]-10<=arr[0]<=ro[0][0]+10 and len(ro)<m:
                    ro.append(arr)
                    break
                else:
                    continue  
    


    for ro in room:
        if ro==[]:
            break

        ro.sort(key=lambda x:x[1])    

        if len(ro)==m:
            print('Started!')
        else:                
            print('Waiting!')

        for r in ro:
            print_str=''
            print_str+=str(r[0])
            print_str+=' '
            print_str+=r[1]
            print(print_str)    
