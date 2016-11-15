from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from gigya.tests.test_views import index, account

urlpatterns = [
    url(r'^$', index),
    url(r'^account$', account),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)