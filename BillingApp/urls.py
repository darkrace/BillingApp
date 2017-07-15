from django.conf import settings
from django.conf.urls import include , url
from django.conf.urls.static import static
from django.contrib import admin
from Billing import views

admin.autodiscover()

urlpatterns =[
	url(r'^$', views.index , name='index'),
    url(r'^Item_detail', views.Item_detail , name='Item_detail'),
    url(r'^Price_Detail', views.Price_Detail , name='Price_Detail'),
	url(r'^admin/', admin.site.urls),
	]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)