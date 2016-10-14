function paramIterator(csv_str) {
  var position = 0;
  var done = false;
  return {
    next: function() {
      if (done)
        return {done: true, value: undefined};
      var commaPosition = csv_str.indexOf(",", position);
      if (commaPosition === -1) {
        done = true;
        var value = csv_str.slice(position);
      } else {
        var value = csv_str.slice(position, commaPosition);
        position = commaPosition + 1;
      }
      return {done: false, value: value};
    }
  }
}

var it = paramIterator("one,two,three");
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
