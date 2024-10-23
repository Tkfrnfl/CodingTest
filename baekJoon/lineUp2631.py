# #-*- coding:utf-8 -*-

# 그냥 부분증가수열 최대 길이만 구하기 : 이진탐색, 정확한 값은 못구함

# import bisect

# if __name__ == "__main__":
#    n=int(input())
#    arr=[int(input()) for _ in range(n)]

#    p_list=[]

#    for ar in arr:
#       pos=bisect.bisect_left(p_list,ar)

#       if pos<len(p_list):
#          p_list[pos]=ar
#       else:
#          p_list.append(ar)

#    print(n-len(p_list))         

# dp 로 정확한 부분수열 값까지 구하면서 최대길이 구하기

if __name__ == "__main__":
   n=int(input())
   arr=[int(input()) for _ in range(n)]

   dp=[1 for _ in range(n+1)]

   for i in range(0,n):
      for j in range(i):
         if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+1)

   print(n-max(dp))         