// fib(4) // 3  == fib(3) + fib(2)
// fib(10) // 55
// fib(28) // 317811
// fib(35) // 9227465

// fib(1) == 0 + 1 => 1
// fib(2) ==

function fib(num) {
  // add whatever parameters you deem necessary - good luck!
  if (num === 0) {
    return 0;
  }
  if (num === 1) {
    return 1;
  }

  return fib(num - 1) + fib(num - 2);
}

console.log(fib(50));
