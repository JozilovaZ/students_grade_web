from django.urls import path
from .views import home_page,oquvchi_page,fanlar_page,add_fanqoshish,add_oquvchiqosh,add_bahoq,signup_view,logout_view,login_view,grade_update_view
urlpatterns=[
    path('', home_page, name="bosh_sahifa"),
    path('oquvchilar/', oquvchi_page, name='oquvchilar_add' ),
    path('fanlar/', fanlar_page, name='fan_add' ),
    path('fan_qoshish/', add_fanqoshish, name='fan_qosh'),
    path('oquvchi_qoshish/', add_oquvchiqosh, name='qoshish'),
    path('b_qosh/',add_bahoq, name='b_q'),
    path('signup/',signup_view, name='royxatdan_otish'),
    path('kirish/',login_view, name='login'),
    path('logout/',  logout_view, name='logout'),
    path('update/<int:id>/', grade_update_view, name='update_grade'),





]



