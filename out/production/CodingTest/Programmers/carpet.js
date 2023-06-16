var candi=[]

function solution(brown, yellow) {

    if(yellow==1){
        var answer=[3,3]
    }
    else{
        decomposition(yellow)
        var i =checkAns(brown)

        var answer = [candi[i][1]+2,candi[i][0]+2];
        //console.log(answer)
    }
    return answer;
}

//소인수 분해
function decomposition(yellow){

    for(var i=1;i<Math.sqrt(yellow);i++){
        if(yellow%i==0){
            var tmp=[i,yellow/i]
            
            candi.push(tmp)
        }
    }
}
//정답확인
function checkAns(brown){
    for(var i=0;i<=candi.length;i++){
        if((candi[i][1]*2+candi[i][0]*2)+4==brown){
            return i
        }
    }
}

console.log(solution(10,2))