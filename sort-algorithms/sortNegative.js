function sortNegative(ar) {
    let max = 0;
    let min = 0;
    let countArray = [];
    let sortedArray = [];
    for(let i = 0; i <= ar.length - 1; i++) {
        if(ar[i] > max) {
            max = ar[i];
        }
        if(ar[i] < min) {
            min = ar[i];
        }
    }
    for(let i = min; i <= (max - min); i++) {
        countArray.push(i);
    }
    for(let i = 0; i <= countArray.length - 1; i++) {
        for(let j = 0; j <= ar.length - 1; j++) {
            if(countArray[i] == ar[j]) {
                sortedArray.push(countArray[i]);
            }
        }
    }
    console.log(countArray);
    console.log(sortedArray);
}

sortNegative([4, 3, 2, 1, -3, -2]);
