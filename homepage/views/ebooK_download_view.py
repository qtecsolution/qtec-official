from django.shortcuts import render,redirect

from qtec_official import settings
from django.core.mail import send_mail, EmailMessage
from homepage.forms.ebook_form import Book_Download_Form

def download_book(request):
    if request.method == 'POST':
        form = Book_Download_Form(request.POST)
        if form.is_valid():
            form.save()
            to_email = form.cleaned_data.get('email')

            subject = "Thanks for downloading the book"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [to_email]
            message = "Click this link to download the book: http://127.0.0.1:8000/static/book/demo.pdf"

            send_mail(subject, message, from_email, recipient_list)

            return redirect("/e-book/")
    else:
        form = Book_Download_Form()
    
    return render(request, 'homepage/e-book.html', {'form': form})