from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from polls.models import Poll

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    (r'^$', 
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html')),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html')),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results'),
    (r'^(?P<poll_id>\d+)/vote/$','polls.views.vote'),
)

