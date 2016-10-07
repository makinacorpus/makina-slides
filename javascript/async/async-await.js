var fetch = require('node-fetch');

async function main() {
  var response = await fetch("http://localhost:8080/data/greeting.txt");
  var text = await response.text();
  console.log(text);
  var responses = await Promise.all([
    fetch("http://localhost:8080/data/data1.json"),
    fetch("http://localhost:8080/data/data2.json"),
    fetch("http://localhost:8080/data/data3.json")
  ]);
  var data = await Promise.all(
    responses.map((response) => response.json())
  );
  var numbers = data.map((item) => item.value);
  console.log(numbers);
}

main();
