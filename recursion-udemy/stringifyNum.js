function stringifyNumbers(obj) {
  let newObj = Object.assign({}, obj);

  function helper(obj) {
    for (let key in obj) {
      if (typeof obj[key] === 'number') {
        obj[key] = obj[key].toString();
      }
      if (typeof obj[key] === 'object') {
        helper(obj[key]);
      }
    }
  }
  helper(newObj);
  return newObj;
}

let obj = {
  num: 1,
  test: [],
  data: {
    val: 4,
    info: {
      isRight: true,
      random: 66
    }
  }
};

console.log(stringifyNumbers(obj));

/*
{
    num: "1",
    test: [],
    data: {
        val: "4",
        info: {
            isRight: true,
            random: "66"
        }
    }
}
*/
