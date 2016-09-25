/* global $ */

$(function() {

  "use strict";

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
      (new Function('log', 'request', 'requestPromise', code))(log, request, requestPromise);
    });
  });


});
