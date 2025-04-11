from AutoRu.models import Vehicle
from AutoRu.serializers import VehicleSerializer


class APIMixin:
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class TitleMixin:
    title = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
