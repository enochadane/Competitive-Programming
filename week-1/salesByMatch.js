'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the sockMerchant function below.
function sockMerchant(n, ar) {

    let pairCounter = 0;
    let similarSocks = [];
    for(let i = 0; i <= n-1; i++) {
        let counter = 1;
        let sock = ar[i];
        let counted = false;
        
        for(let j = 0; j < i; j++) {
            if(ar[i] == ar[j]) {
                counted = true;
            }
        }
        
        if(!counted) {
            for(let k = i + 1; k <= n-1; k++) {
                if(sock == ar[k]) {
                    counter += 1;
                }
            }
            similarSocks.push(counter);
        }
    }
    
    for(let j = 0; j <= similarSocks.length - 1; j++) {
        let pairSocks = Math.floor(similarSocks[j]/2);
        pairCounter += pairSocks;
    }
    
    return pairCounter;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const ar = readLine().split(' ').map(arTemp => parseInt(arTemp, 10));

    let result = sockMerchant(n, ar);

    ws.write(result + "\n");

    ws.end();
}
