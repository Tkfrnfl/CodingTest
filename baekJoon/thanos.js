const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const inputLines = [];

rl.on('line', (line) => {
    inputLines.push(line); 
}).on('close', () => {
    let cnt0=0
    let cnt1=0

    for(i of inputLines[0]){
        if(i==='0'){
            cnt0+=1
        }
        else{
            cnt1+=1
        }
    }
    let ans=inputLines[0].split('')

    let cnt0_2=cnt0/2
    let cnt1_2=cnt1/2

    let cnt=ans.length
    while(cnt0>cnt0_2){
        if(ans[cnt-1]==='0'){
            cnt0-=1
            ans.splice(cnt-1,1)
        }
        cnt-=1
    }
    cnt=0
    while(cnt1>cnt1_2){
        if(ans[cnt]==='1'){
            cnt1-=1
            ans.splice(cnt,1)
        }
        cnt+=1
    }
    console.log(ans.join(''))
})