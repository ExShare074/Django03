from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from news_app import views  # ⬅️ добавили импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', views.home, name='news_page'),  # ⬅️ добавили маршрут
    path('news_app/', include('news_app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
