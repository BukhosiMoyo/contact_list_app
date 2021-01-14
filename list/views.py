from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView


def home(request):

    context = {}
    return render(request, context)


class CreateContactView(CreateView):
    """Creates a new contact for us """
    template_name = "create.html"
    #model = Contact


class DeleteContactView(DeleteView):
    #model = Contact
    template_name = "delete.html"


class UpdateContactView(UpdateView):
    template_name = "update.html"
    #model = Contact

    
