function listParam(csvStr) {
  return {
    [Symbol.iterator]: function*() {
      var position = 0;
      var commaPosition = csvStr.indexOf(",", position);
      while (commaPosition != -1) {
        yield csvStr.slice(position, commaPosition);
        position = commaPosition + 1
        commaPosition = csvStr.indexOf(",", position);
      }
      yield csvStr.slice(position);
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
