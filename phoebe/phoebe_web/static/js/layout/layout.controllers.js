(function() {
'use strict';

    angular
        .module('phoebe.layout')
        .controller('NavbarController', NavbarController);

    NavbarController.inject = ['$scope','Authentication'];
    function NavbarController($scope,Authentication) {
        //var vm = this;

        $scope.logout = logout

        function logout(){
            Authentication.logout()
        }
    }
})();