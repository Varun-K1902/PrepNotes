from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from django.core.mail import send_mail
from django.conf import settings

def home_page(request):
    search = request.GET.get('search', '')
    subjects = models.Subject.objects.filter(title__icontains=search).order_by('title')

    paginator = Paginator(subjects, 9)
    page_num = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {'page_obj':page_obj, 'search': search}
    return render(request, 'notes/home_page.html', context)

def posts_page(request, pk):

    search = request.GET.get('search', '')

    subject = models.Subject.objects.get(title=pk)
    posts = subject.posts.filter(question__icontains=search)

    paginator = Paginator(posts, 9)
    page_num = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {'page_obj':page_obj, 'search': search, 'subject': subject}
    return render(request, 'notes/post_page.html', context)

def answer_page(request, subject, pk):
    post = models.Post.objects.get(id=pk)
    search = request.GET.get('search', '')
    page = request.GET.get('page', 1)
    context = {'post': post, 'search': search, 'page': page}
    return render(request, 'notes/answer_page.html', context)

def contact_page(request):
    if request.method == 'POST':
        send_mail(
            "StudyNotes: " + request.POST.get('subject', ''),  # Subject
            'From: ' + request.POST.get('email', '') + "\n" + request.POST.get('msg',''),  # Message
            settings.EMAIL_HOST_USER,  # From email
            [settings.EMAIL_TO_USER],  # To email
            fail_silently=False,
        )
    return render(request, 'notes/contact_page.html')

def about_page(request):
    return render(request, 'notes/about_page.html')