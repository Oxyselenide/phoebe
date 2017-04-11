(function () {
  'use strict';

  angular
    .module('phoebe', [
      'phoebe.routes',
      'phoebe.authentication'
    ]);

  angular
    .module('phoebe.routes', ['ngRoute']);
})();


run.$inject = ['$http'];

/**
* @name run
* @desc Update xsrf $http headers to align with Django's defaults
*/
function run($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}

