from rest_framework import serializers
from vendor_app.models import Vendor,HistoricalPerformance


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Vendor
        fields ="__all__"



class MetricsSerializer(serializers.ModelSerializer):

    class Meta:
        model= HistoricalPerformance
        fields ="__all__"