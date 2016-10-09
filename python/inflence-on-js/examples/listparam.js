function listParam(csvStr) {
  var params = csvStr.split(",");
  return {
    csvStr: csvStr,
    [Symbol.iterator]: function() {
      return params[Symbol.iterator]();
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
