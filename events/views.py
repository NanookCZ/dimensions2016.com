from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.template import RequestContext
from .models import Event, Guest
from .forms import GuestForm, EventForm
from videos.models import Category
from django.contrib.auth.decorators import login_required


def event_view(request):
	events = Event.objects.all()
	month_event = Event.objects.get(month_event = 'yes')
	categories = Category.objects.all()
	context = {'month_event':month_event, 'events' : events, 'categories' : categories}
	template_name = 'event/events.html'
	return render(request, template_name, context)

@login_required
def user_event_view(request):
	the_user = request.user
	events = Event.objects.filter(hosted_by=the_user)
	month_event = Event.objects.get(month_event = 'yes')
	categories = Category.objects.all()
	context = {'month_event':month_event, 'events' : events, 'categories' : categories}
	template_name = 'event/my_events.html'
	return render(request, template_name, context)

@login_required
def attending_view(request):
	try:
		the_user = request.user
	except:
		the_user = None
	events = Guest.objects.filter(user=the_user, attending_status = 'yes')
	print(events)
	month_event = Event.objects.get(month_event = 'yes')
	categories = Category.objects.all()
	context = {'month_event':month_event, 'events' : events, 'categories' : categories}
	template_name = 'event/attending.html'
	return render(request, template_name, context)



def category_event(request, slug_cat):
	month_event = Event.objects.get(month_event = 'yes')
	try:
		obj_cat = get_object_or_404(Category, slug = slug_cat)
	except:
		pass

	try: 
		the_user = request.user
		u = UserProfile.objects.get(user = the_user)
	except:
		u = None 
	categories = Category.objects.all()
	queryset = Event.objects.filter(category = obj_cat).order_by('created_date')
	context = {'month_event':month_event, "u" : u, "obj_cat" : obj_cat, "queryset" : queryset, "categories" : categories}
	template_name = 'event/category_event.html'
	return render(request, template_name, context)

def event_detail(request, slug):
	categories = Category.objects.all()
	event = Event.objects.get(slug = slug)
	guests = Guest.objects.filter(event = event.id, attending_status = 'yes')

	participants = []

	for g in guests:
		participants.append(g)

	print(participants)

	guest_form = GuestForm(request.POST)
	if guest_form.is_valid():
		print(guest_form)
		attending_status = guest_form.cleaned_data['attending_status']
		comment = guest_form.cleaned_data['comment']
		new_guest = Guest.objects.get_or_create(user = request.user, event = event, attending_status = attending_status, comment = comment)
		return HttpResponseRedirect(reverse('events'))
	
	

	context = {"categories" : categories, "event" : event, "guests" : guests, "form" : guest_form, "participants" : participants}
	template_name = 'event/event_detail.html'
	return render(request, template_name, context)

@login_required
def add_event(request):
	the_user = request.user
	month_event = Event.objects.get(month_event = 'yes')
	form_event = EventForm(request.POST)
	if form_event.is_valid():
		print(form_event)
		title = form_event.cleaned_data['title']
		description = form_event.cleaned_data['description']
		event_start = form_event.cleaned_data['event_starts']
		event_end = form_event.cleaned_data['event_end']
		time_of_event = form_event.cleaned_data['time_of_event']
		hosted_by = the_user
		street_address = form_event.cleaned_data['street_address']
		city = form_event.cleaned_data['city']
		state = form_event.cleaned_data['state']
		zip_code = form_event.cleaned_data['zip_code']
		telephone = form_event.cleaned_data['telephone']
		category = form_event.cleaned_data['category']
		event = Event.objects.create(title = title,
			description = description, 
			event_start = event_start,
			event_end = event_end,
			time_of_event = time_of_event,
			hosted_by = hosted_by,
			street_address = street_address,
			city = city,
			state = state,
			zip_code = zip_code,
			telephone = telephone,
			category = category)
		event.save()
		return HttpResponseRedirect(reverse('events'))

	context = {'month_event':month_event, "form_event" : form_event}
	template_name = 'event/add_event.html'
	return render(request, template_name, context)
@login_required
def edit_event(request, id):
	user = request.user
	event = Event.objects.get(id=id)

	try:
		event_form = EventForm(request.POST or None, instance = event)
	except:
		event_form = None

	if event_form.is_valid():
		event_form = event_form.save(commit = False)
		event_form.save()
		
	template_name = 'event/edit_event.html'
	context = {'event_form' : event_form, 'event':event}
	return render(request, template_name, context)


	
	




