function sameFrequency(num1, num2) {
  // good luck. Add any arguments you deem necessary.
  const num1ToStrArr = num1.toString().split('');
  const num2ToStrArr = num2.toString().split('');
  let freq1 = {};
  let freq2 = {};

  num1ToStrArr.forEach(elem => {
    if (freq1[elem]) {
      freq1[elem]++;
    } else {
      freq1[elem] = 1;
    }
  });

  num2ToStrArr.forEach(elem => {
    if (freq2[elem]) {
      freq2[elem]++;
    } else {
      freq2[elem] = 1;
    }
  });

  let sameFreqBool = true;
  for (key in freq1) {
    if (freq1[key] !== freq2[key]) {
      sameFreqBool = false;
    }
  }
  return sameFreqBool;
}

sameFrequency(3511, 5311);
