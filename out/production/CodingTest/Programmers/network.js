function solution(n, computers) {
    var visitedCehck= new Array(n).fill(0)
    
    var answer=0;
   
    for(var i=0;i<n;i++){
        if(visitedCehck[i]==0){
            answer++;             // 재귀식 다돌고도 남을시 네트워크 추가하고 재탐색
            visitedCehck[i]=1
            bfs(i)
        }
    }

    function bfs(now){
        var tmpQueue=[]

        console.log(visitedCehck)

        for(var i=0;i<n;i++){
            if(computers[now][i]==1){
                tmpQueue.push(i)         //연결된 컴퓨터 배열에 저장
            }
        }

            for(var j=0;j<tmpQueue.length;j++){
                if(visitedCehck[tmpQueue[j]]==0){
                    visitedCehck[tmpQueue[j]]=1
                    bfs(tmpQueue[j])
                }
            }

    }

    console.log(answer)
    return answer;
}

console.log(solution(4,[[1,0,1,1],[0,1,0,0],[1,0,1,1],[0,0,1,1]]))