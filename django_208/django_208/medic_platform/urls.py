from django.urls import path
from .views import home, register, therapist_login, GetTokenView

urlpatterns = [
    # 这里'patients/'将被认为是应用的根URL
    # path('list/', patient_list, name='patient-list'),
    path('register/', register, name='register'),
    path('login/', therapist_login, name='login'),
    path('home/', home, name='home'),
    path('get_token/', GetTokenView.as_view(), name='get_token'),
]
# Compare this snippet from medic_platform/models.py: