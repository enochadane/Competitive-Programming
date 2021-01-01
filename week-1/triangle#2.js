function drawTriangle2(n) {
    for(i = 1; i <= n; i++) {
        // let space = '';
        let row = '';
        for(j = n-i; j >= 1; j--) {
            row += ' ';
        }
        for(k = 0; k < 2 * i -1; k++) {
            row += '*';
        }
        console.log(row);
    }
}

drawTriangle2(5);