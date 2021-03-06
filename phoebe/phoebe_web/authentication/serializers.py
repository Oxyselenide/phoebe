from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ("id", 'email', 'username', 'created_at', 'updated_at',
                    'first_name', 'last_name', 'password','confirm_password',
                    'team', 'designation'
                )
        
        read_only_fields = ('created_at','updated_at',)

        def create(self, validated_data):
            raise Exception('for testing'+str(validated_data))
            print( 'ser',validated_data)
            #assert (validated_data.get(password) == validated_data.get(confirm_password))
            #return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            raise Exception('for testing update'+str(validated_data))
            instance.username = validated_data.get('username', instance.username)
            instance.first_name = validated_data.get('first_name', instance.first_name)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance