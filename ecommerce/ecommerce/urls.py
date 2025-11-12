"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# import auth views for login/logout
from django.contrib.auth import views as auth_views

# import your store views (prefer explicit names instead of star import)
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # store app routes
    path('', store_views.store, name="store"),
    path('cart/', store_views.cart, name="cart"),
    path('checkout/', store_views.checkout, name="checkout"),
    path('update_item/', store_views.updateItem, name="update_item"),
    path('process_order/', store_views.processOrder, name="process_order"),

    # auth routes (login/logout/register if you have it)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # optional: include built-in auth URLs for password reset etc.
    path('accounts/', include('django.contrib.auth.urls')),
]

# serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
