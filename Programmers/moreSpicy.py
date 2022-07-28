from bisect import bisect_left, bisect_right
import heapq

def solution(scoville, K):

    scoville.sort()
    heapq.heapify(scoville)

    # print(scoville)
    # left=bisect_left(scoville,K)

    # scoville=scoville[:left]

    # #print(scoville)
    # answer = 0
    # success=False
    # while len(scoville)>0 and scoville[0]<K:

    #     if len(scoville)==1:
    #         if success:
    #             answer+=1
    #         else:
    #             answer=-1    
    #         break
    #     elif len(scoville)>1:
    #         tmp=scoville[0]+scoville[1]*2

    #         scoville.pop(0)
    #         scoville.pop(0)

    #         if tmp<K:       
    #             scoville.append(tmp)
    #             scoville.sort()
    #         else:
    #             success=True    
    #         answer+=1
    # #print(answer)

    answer = 0

    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1

        left=heapq.heappop(scoville)
        right=heapq.heappop(scoville)
        heapq.heappush(scoville,left+right*2)

        answer += 1
    print(answer)    
    return answer


if __name__ == "__main__":
	solution([1, 2, 3, 9, 10, 12],7)       