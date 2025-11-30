from django.http import HttpResponseRedirect
from django.views.generic import CreateView,ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    template_name = "notes_form.html"
    success_url = '/smart/notes'
    form_class = NotesForm

    #to fix IntegrityError at /smart/notes/new
    #we create an object with user before directly saving to the db
    #commit=False ->  prohibit saving to the database
    def form_valid(self, form):
        self.object = form.save(commit=False) #do not directly store to the db
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes_list.html"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes_detail.html"

class NotesUpdateView(UpdateView):
    model = Notes
    template_name = "notes_form.html"
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    template_name = 'notes_delete.html'
    success_url = '/smart/notes'
