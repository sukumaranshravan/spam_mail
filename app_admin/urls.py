from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    path('log_in/',views.log_in,name='log_in'),
    path('log_inaction/',views.log_inaction,name='log_inaction'),
    path('add_hobby/',views.add_hobby,name='add_hobby'),
    path('add_hobby_factor/',views.add_hobby_factor,name='add_hobby_factor'),
    path('add_season/',views.add_season,name='add_season'),
    path('add_season_factor/',views.add_season_factor,name='add_season_factor'),
    path('security_question/',views.security_question,name='security_question'),
    path('log_out/',views.log_out,name='log_out'),
    path('forgot/',views.forgot,name='forgot'),
    path('recover_id/',views.recover_id,name='recover_id'),
    path('start_password_reset/',views.start_password_reset,name='start_password_reset'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('add_age_factor/',views.add_age_factor,name='add_age_factor'),
]
