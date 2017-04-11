from django.views.static import HttpResponse
from rest_framework import permissions, viewsets,status
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