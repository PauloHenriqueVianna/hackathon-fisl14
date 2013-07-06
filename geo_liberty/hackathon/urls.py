from django.conf.urls.defaults import patterns,url
from views import Index, Pobreza, Vagas


urlpatterns = patterns('hackathon',
    url(r'^$', Index),
    url(r'^pobreza/$',Pobreza),
     url(r'^vagas/(?P<id_municipio>\d+)/$',Vagas),
)