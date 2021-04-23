from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority,date=date)
        obj.save()
    obj1 = Task.objects.all()
    return render(request, 'home.html', {'obj1': obj1})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})

def update(request,id):
    task=Task.objects.get(id=id)
    forms=Todoform(request.POST or None,instance=task)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':forms})

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'obj1'
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')





