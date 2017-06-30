from django.views import generic
from coster.models import Rides

class IndexView(generic.ListView):
    template_name = 'tenantTuto/index.html'
    context_object_name = 'ride'

    def get_queryset(self):
        return Rides.objects.all()
