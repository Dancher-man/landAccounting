from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Plots, Culture
from app.serializers import PlotSerializer


class PlotsAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            plot_list = Plots.objects.get(pk=pk)
            if plot_list.farmer.name != request.user.username:
                return Response({"error": "No access right"})
            serializer_data = PlotSerializer(plot_list)
        else:
            plot_list = Plots.objects.filter(farmer__name=request.user.username)
            serializer_data = PlotSerializer(plot_list, many=True)

        return Response({'plots': serializer_data.data})

    def post(self, request, *args, **kwargs):
        if not Culture.objects.filter(name=request.data['culture']):
            Culture.objects.create(name=request.data['culture'])

        plot = get_object_or_404(Plots, pk=kwargs.get('pk'))
        if plot.farmer.name != request.user.username:
            return Response({"error": "No access right"})
        culture = get_object_or_404(Culture, name=request.data['culture'])
        plot.culture = culture
        plot.save()
        return Response({'status': 201})

    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


