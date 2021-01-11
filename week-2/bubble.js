function bubbleSort(ar) {
    for(let i = 0; i <= ar.length - 1; i++) {
        for(let j = 0; j < ar.length - 1; j++) {
            if(ar[j] > ar[j + 1]) {
                let temp = ar[j];
                ar[j] = ar[j + 1];
                ar[j + 1] = temp;
            }
            // console.log(ar);
        }
        // console.log(ar);
    }
    // console.log(ar);
}

bubbleSort([4, 3, 6, 7, 0]);
