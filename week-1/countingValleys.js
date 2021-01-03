'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */

function countingValleys(steps, path) {
    
    let trackMove = '';
    let valleyOrMount = [];
    let countValley = 0;
    let countD = 0;
    let countU = 0;
    
    for(let i = 0; i <= steps - 1; i++) {
        if(path[i] == 'D') {
            countD += 1;
        } else {
            countU += 1;
        }
        trackMove += path[i];
        
        if(countD == countU && countD != 0) {
            valleyOrMount.push(trackMove);
            trackMove = '';
            countD = 0;
            countU = 0;
        }
    }
    for(let i = 0; i <= valleyOrMount.length - 1; i++) {
        if(valleyOrMount[i].toString()[0] == 'D') {
            countValley += 1;
        }
    }
    
    return countValley;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const steps = parseInt(readLine().trim(), 10);

    const path = readLine();

    const result = countingValleys(steps, path);

    ws.write(result + '\n');

    ws.end();
}
