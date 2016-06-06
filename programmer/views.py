from django.shortcuts import render, get_object_or_404
from .models import Lookforjob
from django.utils import timezone
from .forms import LookforjobForm
from django.shortcuts import redirect
# Create your views here.


def lookforjob_list(request):
    lookforjobs = Lookforjob.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'programmer/lookforjob_list.html',{'lookforjobs':lookforjobs})


def lookforjob_detail(request, pk):
    lookforjob = get_object_or_404(Lookforjob, pk=pk)
    return render(request, 'programmer/lookforjob_detail.html', {'lookforjob': lookforjob})

def lookforjob_new(request):
    if request.method == "POST":
        form = LookforjobForm(request.POST)
        if form.is_valid():
            lookforjob = form.save(commit=False)
            lookforjob.author = request.user
            lookforjob.published_date = timezone.now()
            lookforjob.save()
            return redirect('programmer.views.lookforjob_detail', pk=lookforjob.pk)
    else:
        form = LookforjobForm()

    return render(request, 'programmer/lookforjob_edit.html', {'form': form})

def lookforjob_edit(request, pk):
    lookforjob = get_object_or_404(Lookforjob, pk=pk)
    if request.method == "POST":
        form = LookforjobForm(request.POST, instance=lookforjob)
        if form.is_valid():
            lookforjob = form.save(commit=False)
            lookforjob.author = request.user
            lookforjob.published_date = timezone.now()
            lookforjob.save()
            return redirect('programmer.views.lookforjob_detail', pk=lookforjob.pk)
    else:
        form = LookforjobForm(instance=lookforjob)

    return render(request, 'programmer/lookforjob_edit.html', {'form': form})