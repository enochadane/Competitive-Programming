function insertionSort(ar) {
    for(let i = 1; i <= ar.length - 1; i++) {
        for(let j = i; j > 0; j--) {
            if(ar[j - 1] > ar[j]) {
                let temp = ar[j - 1];
                ar[j - 1] = ar[j];
                ar[j] = temp;
            }
        console.log(ar);
        }
    }
}

console.log(insertionSort([4, 3, 2, 1]));
