function reverse(str) {
  // add whatever parameters you deem necessary - good luck!
  if (str.length === 0) {
    return '';
  }
  return str[str.length - 1].concat(reverse(str.slice(0, str.length - 1)));
}

console.log(reverse('awesome')); // 'emosewa'
console.log(reverse('rithmschool')); // 'loohcsmhtir'

function reverse(str) {
  if (str.length <= 1) return str;
  // builds it backwards by adding the front letter to the end of the word
  return reverse(str.slice(1)) + str[0];
}
