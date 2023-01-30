import itertools

def solution(n, weak, dist):

    dist.sort(reverse=True)


    # for i in range(len(dist)):
    #     visited=0
    #     for j in range(len(weak)):
            
    #         if weak[j]-dist[i]  #반시계로갈때 

    tmp= [weak[k] for k in range(0,3)]
    print(tmp)
    answer = 0
    return answer

if __name__ == "__main__":
	solution(12,[1, 5, 6, 10],[1, 2, 3, 4])            