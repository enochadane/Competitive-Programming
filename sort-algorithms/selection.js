function selectionSort(ar) {
  for (let i = 0; i <= ar.length - 1; i++) {
    let min = i;
    for (let j = i + 1; j <= ar.length - 1; j++) {
      if (ar[j] < ar[min]) {
        min = j;
      }
    }
    if (min != i) {
      let temp = ar[i];
      ar[i] = ar[min];
      ar[min] = temp;
    }
    console.log(ar);
  }
  // console.log(ar);
}

selectionSort([3, 2, 5, 0, 7]);
