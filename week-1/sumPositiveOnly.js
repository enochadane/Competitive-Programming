function sumPositiveOnly(num1, num2) {
  var firstNumber = String(num1);
  var secondNumber = String(num2);

  let result = "";

  let longest =
    firstNumber.length > secondNumber.length
      ? firstNumber.length
      : secondNumber.length;

  let shortest =
    firstNumber.length > secondNumber.length
      ? secondNumber.length
      : firstNumber.length;

  let digitDifference = longest - shortest;

  if (longest == firstNumber.length) {
    for (i = 0; i < digitDifference; i++) {
      secondNumber = 0 + secondNumber;
    }
  } else {
    for (i = 0; i < digitDifference; i++) {
      firstNumber = 0 + firstNumber;
    }
  }

  let carry = 0;

  for (i = longest; i >= 1; i--) {
    let sum =
      Number(firstNumber[i - 1]) + Number(secondNumber[i - 1]) + Number(carry);
    if (sum > 9) {
      if (i > 1) {
        carry = sum.toString()[0];
        sum = sum.toString()[1];
      }
    }
    result = sum + result;
  }

  console.log(result);
}

sumPositiveOnly(99209, 803);
