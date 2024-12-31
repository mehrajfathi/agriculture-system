from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import FarmPlotSerializer, CropSerializer
from crops.models import FarmPlot, Crop

class FarmPlotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FarmPlotSerializer

    def get_queryset(self):
        return FarmPlot.objects.filter(farmer=self.request.user)

class CropViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Crop.objects.all()
    serializer_class = CropSerializer 