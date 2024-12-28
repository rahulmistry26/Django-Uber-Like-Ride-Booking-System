from django.urls import path
from .views import UserView, RoleView, RideView,RideById,RideUpdate,UserLogin,UserUpdate

urlpatterns = [
    path('user/',UserView.as_view(),name=''),
    path('user/login/', UserLogin.as_view(), name='login'),
    path('role/', RoleView.as_view(), name='role'),
    path('rides/', RideView.as_view(), name='ride'),
    path('rides/<int:id>/',RideById.as_view(), name='ride-byid'),
    path('rides/<int:id>/status/',RideUpdate.as_view(), name='ride-update'),
    path('admin/rides/', RideView.as_view(), name='adminride'),
    path('admin/drivers/', UserView.as_view(), name='admin-ride-byid'),
    path('admin/drivers/<int:id>/',UserUpdate.as_view(), name='admin-ride-update'),
]
