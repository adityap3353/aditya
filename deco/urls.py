from rest_framework.routers import SimpleRouter

from .views import aview

router = SimpleRouter()


router.register('',aview)


urlpatterns = router.urls