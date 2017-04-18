(function(){

    angular
            .module('phoebe.auth')
            .factory('Authentication', Authentication)

    Authentication.$inject = ['$http'];
    /* factory method of authentication
    */
    function Authentication($http) {
        var services = {
            login: login,
           // register: register,
           // logout: logout
        }
        return services;

        function login(user, password) {
            return $http.post('/api/v1/auth/login/', {
                    user: user,
                    password: password
                })
                .then(loginSuccessFn, loginErrorFn);
        }
    }

    /*
    */

    function loginSuccessFn(data, status, headers, config) {
        // Authentication.setAuthenticatedAccount(data.data);

        // window.location = '/';
        alert(data)
    }
    function loginErrorFn(data, status, headers, config) {
        alert(data)
        console.error('Epic failure!');
    }

})()