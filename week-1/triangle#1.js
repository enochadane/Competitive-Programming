
function drawTriangle(n) {
    for(i = 1; i <= n; i++) {
        var row = '';
        for(j = 1; j <= i; j++) {
            row += '*';
        }
        console.log(row);
    }
}

drawTriangle(5);