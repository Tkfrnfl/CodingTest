    var answer = [];
    var tmp = [];
    var tmpStart =[];
    var ticketArray=[];
    var candit=0
    var nonICN=[]
function solution(tickets) {

    // "ICN" 출발 티켓 우선순위 정하기
    for(var i =0; i<tickets.length;i++){
        if(tickets[i][0]=="ICN"){
            tmp.push(tickets[i])
            tickets.splice(i,1);
            i--;
        }
    }
    tmp.sort();
    nonICN=tickets
    var tmpDfs=[]

    for(var i=0;i<tmp.length;i++){
        tmpDfs.push(tmp[i])
    }
    //dfs
    tmpDfs.splice(candit,1)
    ticketArray=nonICN.concat(tmpDfs) //탐색할 전체 배열
    dfs(tmp[candit][1],candit,ticketArray,tmpStart)


    //우선순위 설정이 잘못된 경우
    if(ticketArray.length>0){
        //candit 올려서 다시 탐색
        candit++;
        tmpDfs=[]
        tmpStart=[]

        for(var i=0;i<tmp.length;i++){
            tmpDfs.push(tmp[i])
        }
        tmpDfs.splice(candit,1)
        ticketArray=nonICN.concat(tmpDfs) //탐색할 전체 배열

        dfs(tmp[candit][1],candit,ticketArray,tmpStart)
    }
    else{
        answer.push(tmpStart) //정답 후보 저장
    }
    
    answer.sort()
    answer=makeAnswer(answer[0])
    answer.unshift('ICN')
    console.log(answer)
    return answer;
}
function dfs(nextRoute,candit,ticketArra,tmpStar){
    for(var i=0;i<ticketArra.length; i++){
        if(ticketArra[i][0]==nextRoute){
            tmpStar.push(ticketArra[i])
            ticketArra.splice(i,1)
            ticketArray=ticketArra
            tmpStar=tmpStar
            dfs(tmpStar[tmpStar.length-1][1],candit,ticketArra,tmpStar)
        }
    }
}
function makeAnswer(array){
    var answer=[]
    answer.push(array[0][0])
    answer.push(array[0][1])
    for(var i=1;i<array.length;i++){
        answer.push(array[i][1])
    }
    return answer
}


console.log(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))
