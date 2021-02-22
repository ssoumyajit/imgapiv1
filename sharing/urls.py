from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SharingViewSets, CommentViewSets, LikesToSharingViewSets

router = DefaultRouter()

# sharing
router.register('sharing', SharingViewSets)
# likesToSharing
router.register('likes', LikesToSharingViewSets)
# comments
router.register('comments', CommentViewSets)

app_name = 'sharing'

urlpatterns = [
    path(r'', include(router.urls)),
]