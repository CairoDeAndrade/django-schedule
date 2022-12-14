from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Contact
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contacts = Contact.objects.order_by('-id').filter(
        show=True
    )
    paginator = Paginator(contacts, 1)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def see_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if not contact.show:
        raise Http404

    return render(request, 'contacts/see_contact.html', {
        'contact': contact
    })


def search(request):
    term = request.GET.get('term')

    if term is None or not term:
        messages.add_message(request, messages.ERROR, 'The field "Search" can not be empty!')
        return redirect('index')

    fields = Concat('name', Value(''), 'last_name')

    contacts = Contact.objects.annotate(
        complete_name=fields
    ).filter(
        complete_name__icontains=term
    )

    return render(request, 'contacts/search.html', {
        'contacts': contacts
    })