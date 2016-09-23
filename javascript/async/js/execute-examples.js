/* global $ */

$(function() {

  "use strict";

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
      (new Function('log', code))(log);
    });
  });


});
