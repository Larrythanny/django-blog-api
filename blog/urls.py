
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = router.urls



# from django.urls import path
# from .views import blog_list_create

# urlpatterns = [
#     path('blogs/', blog_list_create),
# ]