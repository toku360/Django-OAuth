
from django.contrib import admin
from django.urls import path, include
from . import settings
# 静的なファイ ルを各アプリケーションから (さらに指定した別の場所からも) 一つの場所に集め、運 用環境で公開しやすくするもの
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('stores/', include('stores.urls')),
]

# debugモード=True(開発環境)の場合はローカルの画像を呼び出す
# 本番環境はgunicornなどwebサーバで管理が望ましい
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)