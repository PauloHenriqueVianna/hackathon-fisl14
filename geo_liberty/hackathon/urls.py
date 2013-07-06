from django.conf.urls.defaults import patterns,url
from views import Inicio, Pobreza, PobrezaEstado


urlpatterns = patterns('hackathon',
    url(r'^$', Inicio),
    url(r'^pobreza/$',Pobreza),
    url(r'^pobreza-estado/$',PobrezaEstado),
)