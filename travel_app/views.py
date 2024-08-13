# destinations/views.py
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer
from .forms import DestinationForm

class DestinationListCreate(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
#
# def rest_index(request):
#     context = {}
#     template = loader.get_template("rest_tali.html")
#     return HttpResponse(template.render(context, request))

def dest_index(request):
    return render(request, 'index222.html', )
def destination_list(request):
    destinations = Destination.objects.all()
    form = DestinationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('destination-list')
    return render(request, 'list_create.html', {'destinations': destinations, 'form': form})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'detail.html', {'destination': destination})

def destination_update(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    form = DestinationForm(request.POST or None, request.FILES or None, instance=destination)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('destination-detail', pk=destination.pk)
    return render(request, 'update.html', {'form': form})

def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.delete()
        return redirect('destination-list')
    return render(request, 'delete.html', {'destination': destination})
