
from rest_framework import routers
from .views import OfficeView, RentalView

router = routers.DefaultRouter()

router.register('office', OfficeView)
router.register('rental', RentalView)


urlpatterns = router.urls
