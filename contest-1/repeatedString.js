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

// Complete the repeatedString function below.
function repeatedString(s, n) {

    let countA = 0;
    let totalAs = 0;
    for(let i = 0; i <= s.length - 1; i++) {
        if(s[i] == 'a') {
            countA += 1;
        }
    }
    if(n%s.length == 0) {
        totalAs = (n * countA) / s.length;
    } else {
        let multipleN = Math.floor(n/s.length) * s.length;
        let lastS = n - multipleN;
        let extraAs = 0;
        for(let i = 0; i <= lastS - 1; i++) {
            if(s[i] == 'a') {
                extraAs += 1;
            }
        }
        totalAs = (multipleN * countA) / s.length + extraAs;
    }
    
    return totalAs;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const n = parseInt(readLine(), 10);

    let result = repeatedString(s, n);

    ws.write(result + "\n");

    ws.end();
}
