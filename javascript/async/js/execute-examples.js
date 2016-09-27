/* global $ */

$(function() {

  "use strict";

  function sum(arr) {
    return arr.reduce((acc, cur) => acc + cur, 0);
  };

  function request(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.addEventListener("load", function() {
      callback(xhr.responseText);
    });
    xhr.open("GET", url, true);
    xhr.send(null);
  }

  function requestPromise(url) {
    return new Promise(function(resolve, reject) {
      var xhr = new XMLHttpRequest();
      xhr.addEventListener("load", function() {
        resolve(xhr.responseText);
      });
      xhr.open("GET", url, true);
      xhr.send(null);
    });
  }

  function requestObservable(url) {
      return Rx.Observable.create(function(observer) {
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("load", function() {
          observer.onNext(xhr.responseText);
          observer.onCompleted();
        });
        xhr.open("GET", url, true);
        xhr.send(null);
      });
    }

  // Generator runner borrowed from
  // https://github.com/getify/You-Dont-Know-JS/blob/master/async%20%26%20performance/ch4.md#promise-aware-generator-runner
  // thanks to Benjamin Gruenbaum (@benjamingr on GitHub) for
  // big improvements here!
  function run(gen) {
    var args = [].slice.call( arguments, 1), it;

    // initialize the generator in the current context
    it = gen.apply( this, args );

    // return a promise for the generator completing
    return Promise.resolve()
    .then( function handleNext(value){
      // run to the next yielded value
      var next = it.next( value );

      return (function handleResult(next){
        // generator has completed running?
        if (next.done) {
          return next.value;
        }
        // otherwise keep going
        else {
          return Promise.resolve( next.value )
          .then(
            // resume the async loop on
            // success, sending the resolved
            // value back into the generator
            handleNext,

            // if `value` is a rejected
            // promise, propagate error back
            // into the generator for its own
            // error handling
            function handleErr(err) {
              return Promise.resolve(
                it.throw( err )
              )
              .then( handleResult );
            }
          );
        }
      })(next);
    } );
  }

  $("button.run").each(function() {
    var $resultContainer = $('<div class="result-container"></div>');
    $(this).html("Exécuter").after($resultContainer);
    var $button = $(this);
    var log = function(string) {
      $("<p>" + string + "</p>").hide().appendTo($resultContainer).slideDown();
    };
    var code = $button.parent().prev('.highlight').find('pre').text();
    $button.click(function() {
      $resultContainer.empty();
      (new Function('log', 'request', 'requestPromise', 'requestObservable', 'sum', 'run', code))(log, request, requestPromise, requestObservable, sum, run);
    });
  });


});
