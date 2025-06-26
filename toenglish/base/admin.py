from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Common_Word)
 
admin.site.register(Vocabulary)

admin.site.register(Article)
admin.site.register(Image_article)
admin.site.register(Conversation)

admin.site.register(Adj)
admin.site.register(Slang)
admin.site.register(Phrasal_Verb)
admin.site.register(Useful_sentene)
 
@admin.register(Conversations)
class ConversationsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Vocabularies)
class VocabulariesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
