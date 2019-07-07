from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = [
    path('victor/admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('suggestions/', include('suggestions.urls')),
    path('', include('blog.urls')),
    path('users/', include('users.urls')),
    path('egbevictorjunior/creator/', TemplateView.as_view(
        template_name='victor.html',
        extra_context={'title': 'The Developer'}
    ), name='creator'),
    path('facebook/', RedirectView.as_view(url='https://facebook.com/egbevictorjunior'), name='facebook'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
