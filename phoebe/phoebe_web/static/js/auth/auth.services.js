(function () {

    angular
        .module('phoebe.auth')
        .factory('Authentication', Authentication)

    Authentication.$inject = ['$http'];

    function Authentication($http) {
        var service = {
            login: login,
            // register: register,
            logout: logout
        }
        return service;

        ////////////////
        function login(user, password) {
            return $http.post('/api/v1/auth/login/', {
                    user: user,
                    password: password
                })
                .then(loginSuccessFn, loginErrorFn);

            function loginSuccessFn(data, status, headers, config) {
                // Authentication.setAuthenticatedAccount(data.data);
                window.location = '/';
            }

            function loginErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }
        }

        ////////////////
        function logout() {
            return $http.post('/api/v1/auth/logout/')
                .then(logoutSuccessFn, logoutErrorFn);

            function logoutSuccessFn(data, status, headers, config) {
               // Authentication.unauthenticate();
                window.location = '/';
            }

            function logoutErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }
        }
    }

})()