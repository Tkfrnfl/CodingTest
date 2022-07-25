function solution(clothes) {

    let map =new Map();

    for(var i=0;i<clothes.length;i++){   // mapping
        map.set(clothes[i][0],clothes[i][1])
    }

    let values =Array.from(map.values()) 
    values=new Set(values) //중복제거
    values=Array.from(values.values())
    
    let keys=[]
    
    for(var i=0;i<values.length;i++){  //각 value에 따른 key 값 개수 저장
        keys[i]=getByValue(map,values[i])
    }

    function getByValue(map, searchValue) {
        let tmpArray=[]
        for (let [key, value] of map.entries()) {
          if (value === searchValue)
            tmpArray.push(key)
        }
        return tmpArray.length
      }


    var answer = 1;
    //key +1 하여 선택 안했을때의 경우의 수도 고려
    for(var i=0;i<keys.length;i++){

        tmp=keys[i]+1
        answer*=tmp
    }
    answer-=1 //아무것도 안고른것 제외
    console.log(answer)
    return answer;
}
console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))