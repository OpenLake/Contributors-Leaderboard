from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('',views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('usernames/',views.UserNamesDetailView.as_view()),
    path('insertapi/',views.post_UserNames),
    path('tripathi/',views.current_user),
    path('register/',views.registerUser),
    path('ghfriends/',views.add_GithubFriends),
    path('getghfriends/',views.get_GithubFriends),
    path('dropghfriends/',views.drop_GithubFriends),
    path('olfriends/',views.add_OpenlakeFriends),
    path('getolfriends/',views.get_OpenlakeFriends),
    path('dropolfriends/',views.drop_OpenlakeFriends),
    path('leetcodecontestrankings/',views.ContestRankingsAPIView),
    
]


