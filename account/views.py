from rest_framework.views import APIView
from account.serializers import RegisterSerializer, ForgotPasswordSerializer,ForgotPasswordCompleteSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PhoneNumberVerification
from account.serializers import SendPhoneNumberVerificationSerializer, VerifyPhoneNumberSerializer

User = get_user_model()

class RegisterAPIView(APIView):
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались. Вам отправлено письмо с активацией', status=201)

class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Успешно', status=200)
        except User.DoesNotExist:
            return Response('Link expired', status=400)

class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_reset_password_code()
        return Response('вам отправлено письмо для восстановления пароля')

class ForgotPasswordCompleteAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно изменен')


class SendPhoneNumberVerificationView(APIView):
    serializer_class = SendPhoneNumberVerificationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        User, is_created = PhoneNumberVerification.create_user(phone_number)

        if is_created:
            User.send_token()
        
        return Response({'detail': 'Код подтверждения отправлен на ваш номер телефона'})


class VerifyPhoneNumberView(APIView):
    serializer_class = VerifyPhoneNumberSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        user = PhoneNumberVerification.get_user(phone_number)

        token = User.get_token()
        return Response({'token': token.key})
