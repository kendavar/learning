from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    #url(r'^$',views.index,name='index'),
    url(r'^user/',views.users,name="users"),
    # url(r'^formpage/',views.form_view),
]
