from django.shortcuts import render, HttpResponseRedirect
# JSONResponse import
from django.http import JsonResponse
from dashboard.models import BookDownloader
from qtec_official import settings
from django.core.mail import send_mail, EmailMessage
from homepage.forms.ebook_form import Book_Download_Form


def download_book(request):
    title = 'Ebook'
    return render(request, 'e-book.html', {'title': title})


# def req_to_download_book(request):
#     if request.method == 'POST':
#         user_name = request.POST['user_name']
#         phone_number = request.POST['phone_number']
#         email = request.POST['email']

#         to_email = request.POST.get('email')
#         to_name = request.POST.get('user_name')

#         subject = 'Download Your Free eBook: "An Entrepreneur\'s Guide to Develop Software for Business"'
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [to_email]
#         message =f"""Dear {to_name},

#         We hope this email finds you well! As a fellow entrepreneur, we believe you'll find immense value in our latest
#         eBook titled "An Entrepreneur's Guide to Develop Software for Business." Whether you're just starting your business
#         or looking to enhance your existing operations, this comprehensive guide is designed to provide you with valuable
#         insights and strategies to leverage the power of software development for your business growth.

#         In this eBook, you will discover:

#         * Understanding the Importance of Software Development for Business Success
#         * Identifying the Right Software Solutions for Your Unique Needs
#         * Navigating the Software Development Process: From Idea to Execution
#         * Best Practices for Working with Software Development Teams
#         * Key Considerations for Budgeting and Timelines
#         * How to Ensure Software Security and Data Privacy
#         * Real-life Case Studies and Success Stories
#         And much more!

#         To download your complimentary copy of "An Entrepreneur's Guide to Develop Software for Business," simply click on the link below:


#         {request.build_absolute_uri('/static/ebook/QSL_Ebook_1.pdf')}"

#         We genuinely believe that this eBook can make a significant impact on your business journey, and we're thrilled to share it with you. Feel free to share this offer with your fellow entrepreneurs or anyone who might find it valuable.

#         If you have any questions or require further assistance regarding software development or any other entrepreneurial matter, don't hesitate to reach out. We're here to help you succeed!

#         Thank you for being a part of our entrepreneurial community. We wish you all the best in your business endeavors.

#         Best regards,
#         Qtec Solution Limited """

#         send_mail(subject, message, from_email, recipient_list)
#         notify ="Thank You"+ " " + to_name
#         return JsonResponse({'notify': notify})

def req_to_download_book(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        # save to Book Downloader
        try:
            BookDownloader.objects.create(
                user_name=user_name, phone_number=phone_number, email=email)
        except Exception as e:
            print(e)
            pass
        to_email = request.POST.get('email')
        to_name = request.POST.get('user_name')

        subject = 'Download Your Free eBook: "An Entrepreneur\'s Guide to Develop Software for Business"'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [to_email]
        cc_email = [settings.EMAIL_HOST_USER]

        message = f"""Dear {to_name},

        We hope this email finds you well! As a fellow entrepreneur, we believe you'll find immense value in our latest
        eBook titled "An Entrepreneur's Guide to Develop Software for Business." Whether you're just starting your business 
        or looking to enhance your existing operations, this comprehensive guide is designed to provide you with valuable 
        insights and strategies to leverage the power of software development for your business growth.

        In this eBook, you will discover:

        * Understanding the Importance of Software Development for Business Success
        * Identifying the Right Software Solutions for Your Unique Needs
        * Navigating the Software Development Process: From Idea to Execution
        * Best Practices for Working with Software Development Teams
        * Key Considerations for Budgeting and Timelines
        * How to Ensure Software Security and Data Privacy
        * Real-life Case Studies and Success Stories
        And much more!

        We genuinely believe that this eBook can make a significant impact on your business journey, and we're thrilled to share 
        it with you. Feel free to share this offer with your fellow entrepreneurs or anyone who might find it valuable.If you have 
        any questions or require further assistance regarding software development or any other entrepreneurial matter, don't 
        hesitate to reach out. We're here to help you succeed!

        Thank you for being a part of our entrepreneurial community. We wish you all the best in your business endeavors.

        Best regards,
        Qtec Solution Limited"""

        # Create an email message object
        email_message = EmailMessage(
            subject, message, from_email, recipient_list, cc=cc_email)

        # Path to the eBook file
        ebook_path = settings.BASE_DIR / 'static' / 'ebook' / 'QSL_Ebook_1.pdf'

        # Attach the eBook file
        email_message.attach_file(ebook_path)

        # Send the email
        email_message.send()

        notify = "Thank You " + to_name
        return JsonResponse({'notify': notify})
