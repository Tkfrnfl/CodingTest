function solution(priorities, location) {

    // location 위치 표시를 위한 배열 변환
    for(var i=0;i<priorities.length;i++){
        priorities[i]=[priorities[i],0]
    }
    priorities[location][1]=7

    //console.log(priorities)
    pro=0;
    sortArray=[]

    while(priorities.length>1){

        for(var i=1;i<priorities.length;i++){ //조건에 맞을시 맨앞에서 맨뒤로
            if(priorities[i][0]>priorities[0][0]){
                tmp=priorities.shift()
                priorities.push(tmp)
                break
            }
            if(i==priorities.length-1){  //가장 큰 경우엔 shift
                sortArray.push(priorities.shift())
            }
        }
        
    }
    sortArray=sortArray.concat(priorities)

    var answer = 0;
    for (var i=0;i<sortArray.length;i++){
        if(sortArray[i][1]==7){
            answer=i+1
        }
    }
    //console.log(sortArray)

    //console.log(answer)
    return answer;
}

console.log(solution([1, 1, 9, 1, 1, 1],0))