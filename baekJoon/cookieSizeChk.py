# -*- coding:utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    array = []
    for i in range(n):
        line=input()
        array.append(line)

    

    def fheart():
        global n,array

        xx=[-1,1,0,0]
        yy=[0,0,-1,1]

        #find heart
        for i in  range(n):
            for j in range(n):
                _chk=0
                for k in range(4):
                    x=i+xx[k]
                    y=j+yy[k]

                    if 0<=x<n and 0<=y<n and array[x][y]=='*':
                        _chk+=1

                if _chk==4:
                    return (i,j)

    def fL_arm(heart):
        global array

        x,y=heart

        y-=1
        l_arm_cnt=0

        while 0<=y and array[x][y]=='*' :
            l_arm_cnt+=1
            y-=1

        return l_arm_cnt

    def fR_arm(heart):
        global array,n

        x,y=heart

        y+=1
        r_arm_cnt=0

        while y<n and array[x][y]=='*' :
            r_arm_cnt+=1
            y+=1

        return r_arm_cnt    
        
    def fWaist(heart):
        global array

        x,y=heart

        x+=1
        waist_cnt=0

        while x<n and array[x][y]=='*' :
            waist_cnt+=1
            x+=1

        return waist_cnt        

    def fL_leg(waist):
        global array

        x,y=waist

        x+=1
        y-=1
        l_leg_cnt=0

        while x<n and array[x][y]=='*' :
            l_leg_cnt+=1
            x+=1

        return l_leg_cnt      

    def fR_leg(waist):
        global array

        x,y=waist

        x+=1
        y+=1
        r_leg_cnt=0

        while x<n and array[x][y]=='*' :
            r_leg_cnt+=1
            x+=1

        return r_leg_cnt              

    heart= fheart()
    L_arm= fL_arm(heart)
    R_arm= fR_arm(heart)
    Waist= fWaist(heart)
    L_leg= fL_leg((heart[0]+Waist,heart[1]))
    R_leg= fR_leg((heart[0]+Waist,heart[1]))    

    print(heart[0]+1, end=" ")
    print(heart[1]+1)

    print(L_arm, end=" ")
    print(R_arm, end=" ")
    print(Waist, end=" ")
    print(L_leg, end=" ")
    print(R_leg)