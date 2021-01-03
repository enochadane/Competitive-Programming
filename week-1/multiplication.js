function multiply(multiplicand, multiplier) {
  let firstNumber = String(multiplicand);
  let secondNumber = String(multiplier);

  let rows = [];

  for (let i = secondNumber.length - 1; i >= 0; i--) {
    let row = "";
    let carry = 0;
    for (let j = firstNumber.length - 1; j >= 0; j--) {
      let product = (
        Number(secondNumber[i]) * Number(firstNumber[j]) +
        carry
      ).toString();
      carry = 0;
      if (product > 9) {
        carry = Number(product[0]);
        product = product[1];
      }

      row = product + row;
    }
    for (let k = 0; k < secondNumber.length - 1 - i; k++) {
      row += "0";
    }
    console.log(row);
    rows.push(row);
  }
  console.log(add(rows));
}

function add(rows) {
  let total = 0;
  for (let i = 0; i < rows.length; i++) {
    total = sumPositiveOnly(total, Number(rows[i]));
    console.log("total " + total);
  }

  console.log(total);

  return total;
}

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
    carry = 0;
    if (sum > 9) {
      if (i > 1) {
        carry = sum.toString()[0];
        sum = sum.toString()[1];
      }
    }
    result = sum + result;
  }

  result = Number(result);

  return result;
}

multiply(123, 124);
