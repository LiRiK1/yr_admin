from .views import *
from django.urls import path


urlpatterns = [
    path(
        'backend/api/juristlist/',
        JuristListView.as_view(),
        name='jurist-list'),
    path(
        'backend/api/get_user_jurist/<str:tg_id>/',
        ListLawyersSelectedByUser.as_view())
    # path(
    #     'backend/api/add_jurist/<str:tg_id>/<str:jurist_id>/',
    #     JuristAddView.as_view()),
    # path(
    #     'backend/api/delete_user_event/<str:tg_id>/<str:event_id>/',
    #     UserItemDeleteView.as_view()),
]



