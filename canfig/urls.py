from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from main.views import TaskViewSet

router = DefaultRouter()
router.register(r"tasks",TaskViewSet,basename="task")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include("rest_framework.urls")),
    path("api/v1/",include(router.urls))
]
