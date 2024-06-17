from django.shortcuts import render
from rest_framework import generics
from .models import JuristName, Payment, User
from .serializers import UsersSerializer, JuristnameSerializer, PaymentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


# псевдо защита
def is_api_call_authorized(request):
    if 'Authorization' in request.headers:
        request_api_key = request.headers['Authorization']
        api_key = 'E?C_igKbRXg3MZ^'
        return request_api_key == api_key


class JuristListView(generics.ListAPIView):
    serializer_class = JuristnameSerializer

    def get_queryset(self):
        queryset = JuristName.objects.all()

        # Получение параметров запроса
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        specialization = self.request.query_params.get('specialization')
        email = self.request.query_params.get('email')
        phone_number = self.request.query_params.get('phone_number')
        rating = self.request.query_params.get('rating')

        # Фильтрация по параметрам запроса
        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)

        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)

        if specialization is not None:
            queryset = queryset.filter(specialization__icontains=specialization)

        if email is not None:
            queryset = queryset.filter(email__icontains=email)

        if phone_number is not None:
            queryset = queryset.filter(phone_number__icontains=phone_number)

        if rating is not None:
            queryset = queryset.filter(rating_icontains=rating)

        return queryset


class ListLawyersSelectedByUser(APIView):
    def get(self, request, tg_id):
        # Найти пользователя по telegram_id
        try:
            user = User.objects.get(telegram_id=tg_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Получить id пользователя
        user_id = user.id

        # Найти платежи по id пользователя
        user_jurist = Payment.objects.filter(user__id=user_id)
        serializer = PaymentsSerializer(user_jurist, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

#
# class JuristAddView(APIView):
#     def get(self, request, tg_id, event_id):
#         if not is_api_call_authorized(request):
#             return Response({}, status=status.HTTP_418_IM_A_TEAPOT)
#
#         try:
#             # Retrieve the User and Event objects based on tg_id and event_id
#             user = User.objects.get(tg_id=tg_id)
#             event = Event.objects.get(id=event_id)
#
#             # Create a new UserItem object
#             user_item = UserItem(id_users=user, id_events=event)
#             user_item.save()
#
#             serializer = UserItemSerializer(user_item)
#
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except User.DoesNotExist:
#             return Response({'message': 'User not found'},
#                             status=status.HTTP_404_NOT_FOUND)
#         except Event.DoesNotExist:
#             return Response({'message': 'Event not found'},
#                             status=status.HTTP_404_NOT_FOUND)
# #
#
# class UserItemDeleteView(APIView):
#     def get(self, request, tg_id, event_id):
#         if not is_api_call_authorized(request):
#             return Response({}, status=status.HTTP_418_IM_A_TEAPOT)
#
#         user_item = UserItem.objects.filter(
#             id_users__tg_id=tg_id, id_events=event_id).first()
#         if user_item:
#             user_item.delete()
#             return Response(
#                 {'message': 'UserItem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         return Response({'message': 'UserItem not found'},
#                         status=status.HTTP_404_NOT_FOUND)

