function* delegate_gen() {
  yield "from delegate";
}

function* f() {
  yield* delegate_gen();
  var value = yield;
  console.log("Got value " + value);
}

gen = f();
console.log(gen.next());
console.log(gen.next());
console.log(gen.next(42));
