from rest_framework.routers import DefaultRouter
from app.api.views import TaskApiViewSet

router_task = DefaultRouter()

router_task.register(prefix = 'post', basename='post', viewset=TaskApiViewSet)