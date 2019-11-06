function collectStrings(obj) {
  let strs = [];

  function helper(obj) {
    for (let key in obj) {
      if (typeof obj[key] === 'string') {
        strs.push(obj[key]);
      }
      if (typeof obj[key] === 'object') {
        helper(obj[key]);
      }
    }
  }

  helper(obj);
  return strs;
}

const pureRec = obj => {
  let strs = [];
  for (let key in obj) {
    if (typeof obj[key] === 'string') {
      strs.push(obj[key]);
    }
    if (typeof obj[key] === 'object') {
      strs = strs.concat(pureRec(obj[key]));
    }
  }
  return strs;
};

const obj = {
  stuff: 'foo',
  data: {
    val: {
      thing: {
        info: 'bar',
        moreInfo: {
          evenMoreInfo: {
            weMadeIt: 'baz'
          }
        }
      }
    }
  }
};

console.log(pureRec(obj)); // ["foo", "bar", "baz"])
