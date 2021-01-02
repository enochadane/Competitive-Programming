function sumWithNegatives(minuend, subtrahend) {
  let firstNumber = String(minuend);
  let secondNumber = String(subtrahend);

  let firstArray = [];
  let secondArray = [];

  for (const el of firstNumber) {
    firstArray.push(el);
  }

  for (const el of secondNumber) {
    secondArray.push(el);
  }

  let longest =
    firstNumber.length > secondNumber.length
      ? firstNumber.length
      : secondNumber.length;

  let shortest =
    firstNumber.length > secondNumber.length
      ? secondNumber.length
      : firstNumber.length.length;

  let digitDifference = longest - shortest;

  if (firstArray.length > secondArray.length) {
    for (let i = 0; i < digitDifference; i++) {
      secondArray.unshift('0');
    }
  } else {
    for (let i = 0; i < digitDifference; i++) {
      firstArray.unshift('0');
    }
  }
  
  if (Number(firstNumber) > Number(secondNumber)) {
    console.log(getDifference(firstArray, secondArray, longest));
  } else {
    console.log(`-${getDifference(secondArray, firstArray, longest)}`);
  }
}

function balanceDigits() {
  
}

function getDifference(firstArray, secondArray, longest) {
  let result = "";
  for (let i = longest; i > 0; i--) {
    let difference;

    if (Number(firstArray[i - 1]) < Number(secondArray[i - 1])) {
        firstArray[i - 1] = (10 + Number(firstArray[i - 1])).toString();
        firstArray[i - 2] = (Number(firstArray[i - 2]) - 1).toString();
    }

    difference = Number(firstArray[i - 1]) - Number(secondArray[i - 1]);

    result = difference + result;
  }
  res = Array.from(result);
  var index = res.findIndex(val=>val[0] > 0 || val[1] > 0);
  result = result.slice(index);
  return result;
}

sumWithNegatives(103, 9);

