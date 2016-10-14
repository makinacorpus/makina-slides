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

function listParam(csvStr) {
  return {
    csvStr: csvStr,
    [Symbol.iterator]: function() {
      return paramIterator(csvStr);
    },
    toString: function() {
      return csvStr;
    }
  }
}

var params = listParam("one,two,three");
console.log("My list param is " + params + ".");
for (var param of params)
    console.log("One of its params is " + param + ".")
