from django.conf.urls.defaults import patterns,url
from views import Inicio, Pobreza, Vagas


urlpatterns = patterns('hackathon',
    url(r'^$', Inicio),
    url(r'^pobreza/$',Pobreza),
     url(r'^vagas/(?P<id_municipio>\d+)/$',Vagas),
)