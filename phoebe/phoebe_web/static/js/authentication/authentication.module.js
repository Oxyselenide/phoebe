(function () {
  'use strict';

  angular
    .module('phoebe.authentication', [
      'phoebe.authentication.controllers',
      'phoebe.authentication.services'
    ]);

  angular
    .module('phoebe.authentication.controllers', []);

  angular
    .module('phoebe.authentication.services', ['ngCookies']);
})();