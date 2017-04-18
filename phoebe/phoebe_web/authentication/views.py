from django.views.static import HttpResponse
from rest_framework import permissions, viewsets,status,views
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer


from rest_framework import permissions
class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            del serializer.validated_data['confirm_password']
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


import re,json
from django.contrib.auth import authenticate, login
from .models import Account
class LoginApiView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body.decode('utf-8'))
        if not data:
             return Response({
                'status': 'Unauthorized',
                'message': 'Username/password not provided.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        user = data.get('user', None)
        password = data.get('password', None)
        if re.match('[\w.-]+@[\w.-]+.\w{2,4}', user):
            # email is given. finds username
            user = Account.objects.get(email=user).username
            print('usre====',user)
        
        account = authenticate(username=user, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


#TODO: remove these to dynamic index view.
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
class LoginView(TemplateView):
    template_name = 'login.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)