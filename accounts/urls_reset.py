# Note this file uses the deprecated function based password reset views to stay consistent with the module. 
# In a real Django 2.0+ project they should be class based views. See the Django docs for details. 

# from django.conf.urls import url
# from django.urls import reverse_lazy
# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

# urlpatterns = [
#     url('^$', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
#     url(r'^done/$', password_reset_done, name='password_reset_done'),
#     url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'post_reset_confirm': reverse_lazy('password_reset_complete')}, name='passwrd_reset_confirm'),
#     url('^complete/$', password_reset_complete, name='password_reset_complete')
# ]


from django.urls import path, reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    path('done/', password_reset_done, name='password_reset_done'),
    path('<uidb64>/<token>)/', password_reset_confirm, {'post_reset_confirm': reverse_lazy('password_reset_complete')}, name='passwrd_reset_confirm'),
    path('complete/', password_reset_complete, name='password_reset_complete')
]