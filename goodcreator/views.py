from goodcreator.models import Category, Entry
from django.shortcuts import render
from django.views import generic


def index(request):
    categories = Category.objects.filter(archive=False)
    entries = Entry.objects.filter(archive=False)

    return render(request, 'goodcreator/index.html', {'categories': categories, 'entries': entries})


class EntryIndexView(generic.ListView):
    template_name = 'goodcreator/list.html'
    context_object_name = 'entries'
    queryset = Entry.objects.filter(archive=False)


class EntryDetailView(generic.DetailView):
    model = Entry
    template_name = 'goodcreator/detail.html'
    queryset = Entry.objects.filter(archive=False)


class CategoryIndexView(generic.ListView):
    template_name = 'goodcreator/list.html'
    context_object_name = 'entries'
    queryset = Entry.objects.filter(archive=False)


class CategoryDetailView(generic.DetailView):
    model = Entry
    template_name = 'goodcreator/detail.html'
    queryset = Entry.objects.filter(archive=False)
