function capitalizedWords(arr) {
  // add whatever parameters you deem necessary - good luck!
  let finalList = [];
  function helper(newArr) {
    if (newArr.length === 0) {
      return;
    }
    finalList.push(newArr[0].toUpperCase());
    helper(newArr.slice(1));
  }

  helper(arr);
  return finalList;
}

let words = ['i', 'am', 'learning', 'recursion'];
console.log(capitalizedWords(words)); // ['I', 'AM', 'LEARNING', 'RECURSION']
