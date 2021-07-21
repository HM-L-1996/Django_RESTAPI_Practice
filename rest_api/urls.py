from django.conf.urls import url
from rest_api import views

urlpatterns = [
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),#api/tutorials (?p):이 영역의 문자열에 정규표현식을 적용해서 pk가 [0-9]+ 패턴에 부합되는 것들만 views.tutorial_detail로 넘기겠다.
    url(r'^api/tutorials/published$', views.tutorial_list_published)
]