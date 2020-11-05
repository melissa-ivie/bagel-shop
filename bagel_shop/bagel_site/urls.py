from django.urls import path

from . import views

# This registers a namespace for the app which allows us to not hardcode urls in views and templates
app_name = "bagel_site"

urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # Ordering
    path('order', views.order, name='order'),

    # ACCOUNTS
    path('accounts/create', views.accounts_create, name='accounts-create'),
    path('accounts/login', views.accounts_login, name='accounts-login'),
    path('accounts/logout', views.accounts_logout, name='accounts-logout'),
    path('accounts/view', views.accounts_view, name='accounts-view'),
    path('accounts/edit', views.accounts_edit, name='accounts-edit'),
    path('accounts/reset-password', views.accounts_reset_password, name='accounts-reset-password'),
]
