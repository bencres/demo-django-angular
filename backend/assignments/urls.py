from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet, DriverViewSet

router = DefaultRouter()
router.register(r'assignments', AssignmentViewSet)
router.register(r'drivers', DriverViewSet)

urlpatterns = router.urls
