from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_title = "X Crypto"
admin.site.site_header = f"{admin.site.site_title} Admin"
admin.site.index_title = "Admin"

urlpatterns = [
    path("api/", include("app.api.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "app.common.views.bad_request_handler"
handler403 = "app.common.views.permission_denied_handler"
handler404 = "app.common.views.not_found_handler"
handler500 = "app.common.views.server_error_handler"
