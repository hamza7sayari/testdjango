from rest_framework import routers

from recruitments.candidates.viewsets import  CandidateViewSet

app_name = "candidates"

router = routers.SimpleRouter()
router.register('', CandidateViewSet, basename='candidates')

urlpatterns = router.urls