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


// sidebar controller

(function() {
'use strict';

    angular
        .module('phoebe.layout')
        .controller('SidebarController', SidebarController);

    SidebarController.inject = ['$scope'];
    function SidebarController($scope) {

                                if (typeof jQuery === 'undefined') {
            throw new Error('Theme\'s JavaScript requires jQuery');
            }

            var Side = {
            _ps: $('.app-side'),
            _body: $('body'),

            responsive: function responsive() {
                $(window).width() < 768 ? Side._body.removeClass('app-side-mini app-side-opened').addClass('app-side-closed') : Side._body.addClass('app-side-opened').removeClass('app-side-closed');
                if (Side._body.hasClass('page-fixed') & !Side._body.hasClass('app-side-expand-on-hover')) 
                Side._body.removeClass('app-side-mini');
            }
            };

            $(document).ready(function(){
            $(".metismenu").metisMenu();
            
            $(".side_menu_btn").click(function(event){
            event.preventDefault();
            if(this.id=="mini")
                    Side._body.toggleClass('app-side-mini');
                else
                    Side._body.toggleClass('app-side-opened app-side-closed');
                stopMetisMenu();
            });
            
            function stopMetisMenu(){
                $('.side-nav').find('li').removeClass('active');
                $('.side-nav').find('a').attr('aria-expanded', false);
                $('.side-nav').find('ul.collapse').removeClass('in').attr('aria-expanded', false);
            }
            alert("ok")
            });


        activateMetisMenu()

        function activateMetisMenu(){
            $('#side-menu').metisMenu();
        }
    }
})();