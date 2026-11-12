from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = Contact()
            contact.full_name = form.cleaned_data['full_name']
            contact.email = form.cleaned_data['email']
            contact.phone_number = form.cleaned_data['phone_number']
            contact.save()

            return render(request, 'result.html', {
                'message': contact.full_name
            })

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

# Create your views here.
