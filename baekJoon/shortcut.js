const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const inputLines = [];

rl.on('line', (line) => {
    inputLines.push(line); 
}).on('close', () => {

    const [count, limit] = inputLines[0].split(' ').map(Number);

    const ranges = inputLines.slice(1).map(line => {
        const [start, end, value] = line.split(' ').map(Number);
        return [start, end, value];
    });

    let dp = new Array(limit + 1).fill(Infinity);
    dp[0] = 0; // 시작점 초기화

    
    for(let i=0;i<=limit;i++){
        if(i>0){
            dp[i]=Math.min(dp[i],dp[i-1]+1)
        }
        for(r of ranges){
            if(r[0]==i && r[1]<=limit){
                dp[r[1]]=Math.min(dp[r[1]],dp[r[0]]+r[2])
            }
        }
    }
   
    console.log(dp[limit]);
});
