#-*- coding:utf-8 -*-
import math

# def solution(info, edges):

    

#     class Node:
#         def __init__(self,num, data):
#             self.num=num
#             self.data = data
#             self.left = None
#             self.right=None

#     node_list=[]
#     visiting=[]
#     for i in range(0,len(info)):
#         node=Node(i,info[i])
#         node_list.append(node)

#     for idx,val in enumerate(edges):
#         if node_list[val[0]].left == None:
#             node_list[val[0]].left=node_list[val[1]]
#         else:
#             node_list[val[0]].right=node_list[val[1]]

#     # tmp=node_list[0]
#     # while tmp.right:
#     #     print(tmp.num)
#     #     tmp=tmp.right        


#     def dfs(start,sheep,wolf):
        
#         if start==None:
#             return sheep,wolf

#         print(start.num)
#         if sheep<=wolf:
#             return sheep,wolf

#         if start.left!=None:
#             visiting.append(start.left.num)
#         if start.right!=None:    
#             visiting.append(start.left.num)

#         if start.data==0:
#             sheep+=1
#         else :
#             wolf+=1

#         for i in range(0,len(visiting)):
#             visiting.remove(visiting[i])
#             sheep,wolf= dfs(node_list[visiting[i]],sheep,wolf)


                   
#     answer,aw = dfs(node_list[0],1,0)
#     print(answer)

#     return answer


# if __name__ == "__main__":
# 	solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])     
def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = 0

	# 루트 노드부터 시작
    visited[0] = 1
    dfs(1, 0)

    print(max(answer))
    return max(answer)

if __name__ == "__main__":
        solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])