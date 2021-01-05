function countingSort(ar) {
    let max = 0;
    let countArray = [];
    let sortedArray = [];
    for(let i = 0; i <= ar.length - 1; i++) {
        if(ar[i] > max) {
            max = ar[i];
        }
    }
    for(let i = 0; i <= max; i++) {
        countArray.push(0);
    }
    for(let i = 0; i <= ar.length - 1; i++) {
        countArray[ar[i]] += 1;
    }
    for(let i = 0; i <= countArray.length - 1; i++) {
        for(let j = 0; j < countArray[i]; j++) {
            sortedArray.push(i);
        }
    }
    console.log(sortedArray);

}

countingSort([4, 3, 2, 1, 1]);
