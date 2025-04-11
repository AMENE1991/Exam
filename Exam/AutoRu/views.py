from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from AutoRu.models import Vehicle
from AutoRu.utils import APIMixin, TitleMixin
from AutoRu.forms import VehicleForm


class VehiclePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 20
    page_query_param = "page_size"


class VehicleViewSet(APIMixin, ModelViewSet):
    pagination_class = VehiclePagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["username"]
    ordering_fields = ["username"]

    def list(self, request, *args, **kwargs):
        vehicles = Vehicle.objects.all()
        serializer = self.get_serializer(vehicles, many=True)
        return Response({
            "status": "success",
            "count": len(vehicles),
            "data": serializer.data
            })


class VehicleCreateView(TitleMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "create.html"
    success_url = reverse_lazy("Vehicles")
    title = "Create Page"

    def form_valid(self, form):
        response = super().form_valid(form)
        print(f"Создан новый продукт {self.object.brand}")
        return response

    def form_invalid(self, form):
        print(f"Ошибка при создании формы: {form.errors}")
        return super().form_invalid(form)


class VehicleDetailView(TitleMixin, DetailView):
    model = Vehicle
    template_name = "details.html"
    context_object_name = "Vehicle"
    title = "Details Page"

    def get_object(self, queryset=None):
        return get_object_or_404(Vehicle, pk=self.kwargs['pk'])


class VehicleDeleteView(TitleMixin, DeleteView):
    model = Vehicle
    success_url = reverse_lazy("Vehicles")
    template_name = "delete.html"
    context_object_name = "Vehicle"
    title = "Delete Page Confirm"

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        obj = self.get_object()
        obj.delete()
        return HttpResponseRedirect(self.success_url)


class VehicleUpdateView(TitleMixin, UpdateView):
    model = Vehicle
    template_name = 'update.html'
    context_object_name = "Vehicle"
    form_class = VehicleForm
    success_url = reverse_lazy("Vehicles")
    title = "Update Page"

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class VehicleListView(TitleMixin, ListView):
    model = Vehicle
    template_name = "Vehicles.html"
    context_object_name = "Vehicles"
    title = "Vehicles"

    def get_queryset(self):
        return Vehicle.objects.all()

    def next_page_view(request):
        return render(request, "page.html")