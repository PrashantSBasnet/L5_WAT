from django.views.generic import CreateView,ListView, DetailView, UpdateView

from .forms import NotesForm
from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    template_name = "notes_form.html"
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes_detail.html"

class NotesUpdateView(UpdateView):
    model = Notes
    template_name = "notes_form.html"
    success_url = '/smart/notes'
    form_class = NotesForm