function capitalizeFirst(arr) {
  // add whatever parameters you deem necessary - good luck!
  let finalList = [];

  function helper(newArr) {
    if (newArr.length === 0) {
      return;
    } else {
      finalList.push(newArr[0][0].toUpperCase() + newArr[0].slice(1));
      helper(newArr.slice(1));
    }
  }

  helper(arr);
  return finalList;
}

console.log(capitalizeFirst(['car', 'taco', 'banana'])); // ['Car','Taco','Banana']
