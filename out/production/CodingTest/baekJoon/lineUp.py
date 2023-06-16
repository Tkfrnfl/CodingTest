# #-*- coding:utf-8 -*-

# if __name__ == "__main__":
#     n=int(input())
#     array=[]
#     for _ in range(n):
#         array.append(int(input()))


#     def same_check(num_list):           #연속 수 개수체크
#         count=1
#         for i in range(1,n):
#             if num_list[i-1]+1==num_list[i]:
#                 count+=1

#         return count        
    
#     dp=[]
#     tmp=same_check(array)
#     dp.append(tmp)

#     num=0
#     dp_before=array
#     dp_after=[]
    
#     while num<5:
#         num+=1
#         dp.append(0)
#         #print(array)
#         for i in range(n):
#             for j in range(n):
#                 if i<j:
#                     tmp_list=dp_before[0:i]+dp_before[i+1:j+1]+[dp_before[i]]+dp_before[j+1:]       #자리바꾸기
#                     print(tmp_list)
#                     tmp=same_check(tmp_list)
#                     print(tmp)
#                     if tmp==n:
#                         print(num)
#                         break

#                     if tmp>dp[num-1]:
#                         dp[num]=max(dp[num],tmp)                                        #이전보다 클경우 최대값 저장    
#                         dp_after=tmp_list
#         #print(dp[num])
#         dp_before=dp_after                


import sys
from collections import deque
input=sys.stdin.readline


if __name__ == "__main__":
   n=int(input())
   arr=[int(input()) for _ in range(n)]
   dp=[0 for _ in range(n)]
   dp[0]=1
   MAX=0
   for i in range(1,n):
      for j in range(0,i):
         if arr[i] > arr[j]:
            MAX = max(MAX,dp[j])
      dp[i]=MAX+1
      MAX=0
   print(dp)   
   print(n-max(dp)) 