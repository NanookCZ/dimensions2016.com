from django.shortcuts import render, get_object_or_404, Http404, HttpResponseRedirect
from .models import Category, ContentType, ContentBase, Author
from .forms import ReccommendContentForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from accounts.models import UserContentItem, UserProfile
from django.contrib.auth.models import User
from events.models import Event



def reccommend_content(request):
	try:
		the_user = request.user
		if request.method == 'GET':
			form_r = ReccommendContentForm()
		else:
			form_r = ReccommendContentForm(request.POST)
			if form_r.is_valid():
				link = form_r.cleaned_data['link']
				comment = form_r.cleaned_data['comment']
				is_visible = form_r.cleaned_data['is_visible']
				content = Author.objects.create(author = the_user, is_visible = is_visible, link = link, comment = comment)
				return HttpResponseRedirect(reverse('homepage'))
		return form_r
	except:
		return HttpResponseRedirect(reverse('login'))
	

def homepage(request):
	contents = ContentBase.objects.get_featured()
	month_course = ContentBase.objects.get(month_course = 'yes')
	categories = Category.objects.all()
	content_types = ContentType.objects.all()
	try: 
		the_user = request.user
		u = UserProfile.objects.get(user = the_user)
	except:
		u = None 
	form_r = reccommend_content(request)
	context = {"month_course" : month_course, "u" : u, "contents" : contents, "categories" : categories, "content_types" : content_types, "form_r" : form_r}
	template_name = 'home.html'
	return render(request, template_name, context)


def category_content(request, slug_cat):
	month_course = ContentBase.objects.get(month_course = 'yes')
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
	content_types = ContentType.objects.all()
	form_r = reccommend_content(request)
	queryset = ContentBase.objects.filter(category = obj_cat).order_by('created_date')
	context = {"month_course" : month_course, "u" : u, "form_r" : form_r, "obj_cat" : obj_cat, "queryset" : queryset, "categories" : categories, "content_types" : content_types}
	template_name = 'video/category_content.html'
	return render(request, template_name, context)

def content_type_content(request, slug_con):
	month_course = ContentBase.objects.get(month_course = 'yes')
	obj = get_object_or_404(ContentType, slug = slug_con)
	categories = Category.objects.all()
	content_types = ContentType.objects.all()
	form_r = reccommend_content(request)
	try: 
		the_user = request.user
		u = UserProfile.objects.get(user = the_user)
	except:
		u = None  
	queryset = ContentBase.objects.filter(content_type = obj).order_by('created_date')
	context = {"month_course" : month_course, "u" : u, "form_r" : form_r, "obj" : obj, "queryset" : queryset, "categories" : categories, "content_types" : content_types}
	template_name = 'video/content_type_content.html'
	return render(request, template_name, context)

def content_list(request, slug_cat, slug_con):
	month_course = ContentBase.objects.get(month_course = 'yes')
	try:
		obj_cat = get_object_or_404(Category, slug = slug_cat)
	except:
		pass
	try:
		obj_con = get_object_or_404(ContentType, slug = slug_con)
	except:
		pass

	try: 
		the_user = request.user
		u = UserProfile.objects.get(user = the_user)
	except:
		u = None 
	categories = Category.objects.all()
	content_types = ContentType.objects.all()
	form_r = reccommend_content(request)
	queryset = ContentBase.objects.filter(category = obj_cat, content_type = obj_con).order_by('created_date')
	context = {"month_course" : month_course, "u" : u, "form_r" : form_r, "obj_cat" : obj_cat, "obj_con" : obj_con, "queryset" : queryset, "categories" : categories, "content_types" : content_types}
	template_name = 'video/content_list.html'
	return render(request, template_name, context)

def search(request):
	try: 
		the_user = request.user
		u = UserProfile.objects.get(user = the_user)
	except:
		u = None
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		contents = ContentBase.objects.filter(title__icontains = q)
		categories = Category.objects.all()
		content_types = ContentType.objects.all()
		message = "No results found"
		context = {"u" : u, "contents" : contents, "message" : message, "query" : q, "categories" : categories, "content_types" : content_types}
		template_name = 'search.html'
		return render(request, template_name, context)
	else:
		return Http404

def content_detail(request, slug_con):
	categories = Category.objects.all()
	form_r = reccommend_content(request)
	content = ContentBase.objects.get(slug = slug_con)
	try:
		temp = content.reccommend_by.author.id
		print(content.reccommend_by.author.id)
		user = User.objects.get(id = temp)
	except:
		pass
	try: 
		the_user = request.user
		u = UserProfile.objects.get(user = the_user)
	except:
		u = None
	
	content_temp = str((content.get_content_type()))
	related_items = ContentBase.objects.filter(content_type = content_temp)[:5]

	context = {"u" : u, "form_r" : form_r, "categories" : categories, "content" : content, "related_items" : related_items}
	template_name = 'video/video_detail.html'
	return render(request, template_name, context)

def basepage(request):
	courses = ContentBase.objects.filter(month_course = 1)
	event = Event.objects.filter(month_event = 1)
	print(event)
	context = {"courses" : courses, "event" : event}
	template_name = 'base.html'
	return render(request, template_name, context)


















