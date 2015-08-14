from django.shortcuts import render, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import UserContentItem, UserProfile
from videos.models import ContentBase, Category, Author
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserBasicForm
from videos.views import content_detail, reccommend_content

"""
User detail information 
"""

@login_required
def user_detail(request):
	user = request.user
	basic_user = User.objects.get(username = user)
	try:
		the_user = UserProfile.objects.get(user = user)
	except:
		the_user = None
	categories = Category.objects.all()
	try:
		profile_form = UserProfileForm(request.POST or None, instance = the_user)
	except:
		profile_form = None
	basic_form = UserBasicForm(request.POST or None, instance = basic_user)

	if profile_form.is_valid() and basic_form.is_valid():
		form1 = profile_form.save(commit = False)
		form1.user = request.user
		form1.save()
		form2 = basic_form.save(commit = False)
		form2.save()
		return HttpResponseRedirect(reverse('homepage'))

	form_r = reccommend_content(request)
		
	template_name = 'video/user_detail.html'
	context = {'form_r' : form_r, 'profile_form' : profile_form, 'basic_form' : basic_form, "categories" : categories}
	return render(request, template_name, context)


def single_user(request, id):
	the_user = request.user
	user1 = User.objects.get(id = id)

	form_r = reccommend_content(request)

	categories = Category.objects.all()
	template_name = 'video/one_user.html'
	context = {'form_r' : form_r, "user1" : user1, "categories" : categories, "user_content" : user_content}
	return render(request, template_name, context)

def all_users(request):
	users = User.objects.all()
	form_r = reccommend_content(request)
	context = {"users" : users, 'form_r' : form_r}
	template_name = 'users.html'
	return render(request, template_name, context)

@login_required
def user_content(request):
	month_course = ContentBase.objects.get(month_course = 'yes')
	the_user = request.user
	try:
		u = UserProfile.objects.get(user = the_user)
	except:
		u = None
	categories = Category.objects.all()
	content = ContentBase.objects.all()
	form_r = reccommend_content(request)
	user_content = UserContentItem.objects.filter(user = the_user)
	context = {"form_r" : form_r, "month_course" : month_course, "u" : u, "categories" : categories, "content":content, "user_content" : user_content}
	template_name='video/user_content.html'
	return render(request, template_name, context)



@login_required()
def add_to_list(request, slug):

	the_user = request.user
	try:
		content_base = ContentBase.objects.get(slug = slug)
		print(content_base.title)
	except ContentBase.DoesNotExist:
		return None
	try:
		user_content = UserContentItem.objects.get(content = content_base.id, user = the_user)
		print(user_content)
	except:
		user_content = UserContentItem()
		user_content.user = the_user
		user_content.content = content_base
		user_content.save()

	if request.method == 'POST':
		state = request.POST['state']
		if state == 'Favourite':
			user_content.content_state = state
			user_content.save()
			item = user_content
			return HttpResponseRedirect(reverse('favourite'))
		elif state == 'Learned':
			user_content.content_state = state
			user_content.save()
			item = user_content
			return HttpResponseRedirect(reverse('learned'))
		else:
			user_content.content_state = state
			user_content.save()
			item = user_content
			return HttpResponseRedirect(reverse('later'))

		
	return content_detail(request, slug)


