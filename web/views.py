from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.core.mail import send_mail
from .models import SubscribedMail, UpcomingEvent, UserQuery, PastEvent

# Create your views here.

def index(request):
    past4Events = PastEvent.objects.all()[len(PastEvent.objects.all())-4:]
    return render(request, 'web/index.html', {
        "past4Events":past4Events,
    })

def about(request):
    return render(request, 'web/about.html')

def donate(request):
    return render(request, 'web/donate.html')

def contact(request):
    return render(request, 'web/contact.html')

def pastEvent(request):
    allPastEvents = PastEvent.objects.all()

    return render(request, 'web/events.html', {
        'allEvents': allPastEvents
    })
def upcomingEvent(request):
    allUpcomingEvents = UpcomingEvent.objects.all()[len(UpcomingEvent.objects.all())-1:]
    return render(request, 'web/upcomingEvent.html', {
        'allEvents': allUpcomingEvents
    })

def singleEvent(request, event_id):
    thatEvent =  PastEvent.objects.get(pk=event_id)
    past3Events = PastEvent.objects.all()[len(PastEvent.objects.all())-3:]
    upcomingEventa = UpcomingEvent.objects.all()[len(UpcomingEvent.objects.all())-1:][0]
    return render(request, "web/singleEvent.html",{
        "event":thatEvent,
        "upcoming1Events": UpcomingEvent.objects.all()[len(UpcomingEvent.objects.all())-1:][0],
        "past3Events":past3Events,
    })

def subscribe(request):
    if request.method == "POST":
        email_to_subscribe = request.POST['email']
        allregisteredmails = SubscribedMail.objects.all()
        print(allregisteredmails)
        if allregisteredmails.filter(email=email_to_subscribe).count()==0:
            is_success = send_mail(
                'You Have Successfully subscribed to ComeLetsShare',
                'Hi there.\nYou have subscribing to the newletter of ComeLetsShare. We all welcome you to the growing ComeLetsShareFamily. ',
                'bitsnbytesdevelopers@gmail.com',
                [email_to_subscribe]
            )
            if is_success:
                register = SubscribedMail(email=email_to_subscribe)
                register.save() 
                messages.success(request, f"Your mail id: {email_to_subscribe} has been successfully registered with us.")
            else:
                messages.error(request, "Please fill the form correctly")   
        else:
            messages.error(request, f"The mail id: {email_to_subscribe} is already registered with us.")

        return redirect('homePage')
    else:
        messages.error(request, "Incorrect Method")   
        return redirect('homePage')

def submitQuery(request):
    if request.method == "POST":
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_contact = request.POST['contact']
        user_query = request.POST['query']
        user_comments = request.POST['comments']
        user_subscribemail = request.POST.get('subscribemail', 'False')
        if user_subscribemail == "":
            user_subscribemail = True

        user_subscribewhatsapp = request.POST.get('subscribewhatsapp', 'False')
        if user_subscribewhatsapp == "":
            user_subscribewhatsapp = True
        
        print(user_subscribemail, " + ", user_subscribewhatsapp)
        if user_query == '1':
            query_type = 'CU'
        elif user_query == '2':
            query_type = 'SU'
        else:
            query_type = 'VU'
        a_user_query =  UserQuery(name=user_name, email=user_email, contact=user_contact, query=query_type, comments=user_comments, subscribe_to_mail=user_subscribemail, subscribe_to_whatsapp=user_subscribewhatsapp)
        a_user_query.save()
        
        alluserqueries = UserQuery.objects.all()
        allregisteredmails = SubscribedMail.objects.all()
        print(query_type)
        
        if allregisteredmails.filter(email=user_email).count()==0:
            is_success = send_mail(
                'You Have Successfully subscribed to ComeLetsShare',
                'Hi there.\nYou have subscribing to the newletter of ComeLetsShare. We all welcome you to the growing ComeLetsShareFamily. ',
                'bitsnbytesdevelopers@gmail.com',
                [user_email]
            )

        return redirect('contactUs')
    else:
        messages.error(request, "Incorrect Method")   
        return redirect('contactUs')