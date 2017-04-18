(function (){

    angular
        .module('phoebe.auth')
        .controller('LoginController', LoginController);
    
    LoginController.$inject = ['$scope','$location','Authentication'];

    function LoginController($scope,$location,Authentication){
        $scope.error = null
        $scope.login = login

        function login(){
          var a=  Authentication.login($scope.user, $scope.password)
          
          alert(a.status)
          $scope.error = a.status
        }
    }
})()