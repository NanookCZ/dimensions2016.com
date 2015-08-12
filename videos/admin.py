from django.contrib import admin
from .models import Category, ContentType, ContentBase, Source, Author

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug" : ("title",)}
	class Meta:
		model = Category

class ContentTypeAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug" : ("title",)}

	class Meta:
		model = ContentType

class ContentBaseAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug" : ("title",)}

	class Meta:
		model = ContentBase

		
admin.site.register(Category, CategoryAdmin)
admin.site.register(ContentType, ContentTypeAdmin)
admin.site.register(ContentBase, ContentBaseAdmin)
admin.site.register(Source)
admin.site.register(Author)
