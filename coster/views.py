# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from .models import Rides
from rest_framework.views import APIView
from .serializers import RidesSerializer
from rest_framework.response import Response


class IndexView(generic.ListView):
    template_name = 'coster/index.html'
    context_object_name = 'ride'

    def get_queryset(self):
        return Rides.objects.all()

class DetailView(generic.DetailView):
    model = Rides
    template_name = 'coster/detail.html'

class RidesList(APIView):

    def get(self, request):
        rides = Rides.objects.all()
        serializer = RidesSerializer(rides,many=True)

        return  Response(serializer.data)

    def post(self):
        pass

