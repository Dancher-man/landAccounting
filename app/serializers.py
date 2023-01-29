from rest_framework import serializers
from .models import *


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['name']


class PlotSerializer(serializers.ModelSerializer):
    farmer = serializers.StringRelatedField()
    culture = serializers.StringRelatedField()
    season = serializers.StringRelatedField()

    class Meta:
        model = Plots
        fields = ['id', 'farmer', 'culture', 'season']
