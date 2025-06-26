from django.shortcuts import render,redirect ,get_object_or_404
from .models import Conversations,Conversation,Adj,Common_Word,Slang,Useful_sentene,Phrasal_Verb,Story,Vocabularies,Vocabulary,Blog
from django.views.generic import ListView
from .forms import ConversationForm
from django.http import JsonResponse
from django.core.mail import send_mail
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
import json
# Create your views here.
def home(request):
    blog = Blog.objects.all()
    conversations = Conversations.objects.all()
    vocabularies = Vocabularies.objects.all()
    stories = Story.objects.all()
    sent= False
    
    paginator = Paginator(blog, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
     # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
 # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        
    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        username = request.POST.get('name')
        message = f'{username} sent,{body}'
        _from = request.POST.get('email')
        to =['iu@gmail.com']
        send_mail(subject, message, _from,to)
        sent = True
         
    cotext={
        'conversations':conversations,
        'vocabularies':vocabularies,
        'stories':stories,
        'blogs':posts,
        
        'page':page
    }
    return render(request,'index.html',cotext)
def speaking(request):
    section = request.GET.get('section')
    conversations = Conversations.objects.all()
    stories = Story.objects.all()
    vocabularies = Vocabularies.objects.all()
    cotext = {
      
        'conversations':conversations,
        'stories':stories,
        'vocabularies':vocabularies,
        'section':section,
    }
    return render(request,'speaking.html',cotext)
def conversation_detail(request,slug):
    conversations = get_object_or_404(Conversations,slug=slug)
    conversation = conversations.conversation_set.all()
    if request.method == 'POST':
        conversation_ = Conversation.objects.create(
                 
                conversation = conversations,
                sentence_english = request.POST.get('sentence_en'),
                sentence_arabic = request.POST.get('sentence_ar'),
                song = request.FILES.get('song')
                )
        print(request.FILES.get('song'))
        return redirect('conversation',slug=conversations.slug)

        
    cotext={
        
        'conversations':conversation,
        'conv':conversations
    }
    return render(request,'conversation_detail.html',cotext)
def vocabulary_detail(request,slug):
    conversations = get_object_or_404(Vocabularies,slug=slug)
    conversation = conversations.vocabulary_set.all()
    if request.method == 'POST':
        conversation_ = Vocabulary.objects.create(
                 
                vocabulary = conversations,
                sentence_english = request.POST.get('sentence_en'),
                sentence_arabic = request.POST.get('sentence_ar'),
                song = request.FILES.get('song')
                )
        print(request.FILES.get('song'))
        return redirect('vocabulary',slug=conversations.slug)

        
    cotext={
        
        'conversations':conversation,
        'conv':conversations
    }
    return render(request,'voca_detail.html',cotext)
    
def adj_detail(request):
    conversations = Adj.objects.all()

        
    cotext={
        'page':'adjectives',
        'conversations':conversations,
        
    }
    return render(request,'ex_detail.html',cotext)
def slang_detail(request):
    conversations = Slang.objects.all()

        
    cotext={
        'page':'Slang',
        'conversations':conversations,
        
    }
    return render(request,'ex_detail.html',cotext)
def cw_detail(request):
    conversations = Adj.objects.all()

        
    cotext={
        'page':'Common Words',
        'conversations':conversations,
        
    }
    return render(request,'ex_detail.html',cotext)
def us_detail(request):
    conversations = Useful_sentene.objects.all()

        
    cotext={
        'page':'Useful sentenes',
        'conversations':conversations,
        
    }
    return render(request,'ex_detail.html',cotext)
def pv_detail(request):
    conversations = Phrasal_Verb.objects.all()

        
    cotext={
        'page':'Phrasal Verbs',
        'conversations':conversations,
        
    }
    return render(request,'ex_detail.html',cotext)
    
# def vocabulary_detail(request,pk):
#     vocabularies = Vocabularies.objects.get(id=pk)
#     vocabulary = vocabularies.vocabulary_set.all()
#     if request.method == 'POST':
#         vocabulary_ = Vocabulary.objects.create(
                 
#                 vocabulary = vocabularies,
#                 sentence_english = request.POST.get('sentence_en'),
#                 sentence_arabic = request.POST.get('sentence_ar'),
#                 song = request.FILES.get('song')
#                 )
#         print(request.FILES.get('song'))
#         return redirect('vocabulary',pk=vocabularies.id)

#     cotext={
        
#         'vocabularies':vocabulary,
#         'voca':vocabularies,
#         'page':'vocabulary'
#     }
#     return render(request,'conversation_detail.html',cotext)

def story_detail(request,slug):
    story = get_object_or_404(Story,slug)
    cotext={
        
        'story':story
    }
    
    return render(request,'story.html',cotext)
def update_conversation(request,slug,id):
    conversations = get_object_or_404(Conversations,slug)
    conversation = conversations.conversation_set.all()
    convDet = Conversation.objects.get(id=id)
    if request.method == 'POST':
        convDet.sentence_english =  request.POST.get('sentence_en')
        convDet.sentence_arabic =  request.POST.get('sentence_ar')
        convDet.song = request.FILES.get('song')
        convDet.save()
                
                
        return redirect('conversation',slug=conversations.slug)

        # if request.method == 'POST':
        #     sentence_en = request.POST.get('sentence_en')
        #     sentence_ar = request.POST.get('sentence_ar')
        #     song = request.POST.get('song')
    cotext={
        
        'conversations':conversation,
        'conv':conversations,
        'convDet':convDet
    }
    
    return render(request,'conversation_detail.html',cotext)
    
def create_conversations(request):
    # conversations = Conversations.objects.get(id =pk)
    if request.method == 'POST':
        conversations_ = Conversations.objects.create(
                 
                
                title = request.POST.get('conversationEn'),
                title_arabic = request.POST.get('conversationAr'),
                image = request.FILES.get('image')
                )
        
        return redirect('speaking')
    cotext={
        
        'conv':conversations,
        
    }
    
    return render(request,'speaking.html',cotext)
    
def create_story(request):
    # conversations = Conversations.objects.get(id =pk)
    if request.method == 'POST':
        story_ = Story.objects.create(
                 
                
                title = request.POST.get('storyNEn'),
                title_arabic = request.POST.get('storyNAr'),
                story_english = request.POST.get('storyEn'),
                story_arabic = request.POST.get('storyAr'),
                story_image = request.FILES.get('image'),
                song = request.FILES.get('song')
                )
        
        
        return redirect('speaking')
    cotext={
        
        'conv':conversations,
        
    }
    
    return render(request,'speaking.html',cotext)
    
def update_vocabulary(request,slug,id):
    conversations = get_object_or_404(Vocabularies, slug=slug)
    conversation = conversations.vocabulary_set.all()
    convDet = Vocabulary.objects.get(id=id)
    if request.method == 'POST':
        convDet.sentence_english =  request.POST.get('sentence_en')
        convDet.sentence_arabic =  request.POST.get('sentence_ar')
        convDet.song = request.FILES.get('song')
        convDet.save()
                
                
        return redirect('vocabulary',slug= conversations.slug)

        # if request.method == 'POST':
        #     sentence_en = request.POST.get('sentence_en')
        #     sentence_ar = request.POST.get('sentence_ar')
        #     song = request.POST.get('song')
    cotext={
        
        'conversations':conversation,
        'conv':conversations,
        'convDet':convDet
    }
    
    return render(request,'voca_detail.html',cotext)


def delete_conversation(request,pk,id):
    conversations = get_object_or_404(Conversations, slug=slug)
    conversation = conversations.conversation_set.get(id=id)
    if request.method == 'POST':
        conversation.delete()
        return redirect('conversation' ,slug=conversations.slug)
    cotext={
        'conversation':conversation
    }
    return render(request,'delete.html',cotext)
    
def delete_vocabulary(request,pk,id):
    conversations = Vocabularies.objects.get(id=pk)
    conversation = conversations.vocabulary_set.get(id=id)
    if request.method == 'POST':
        conversation.delete()
        return redirect('vocabulary' ,slug=conversations.slug)
    cotext={
        'conversation':conversation
    }
    return render(request,'delete.html',cotext)
# class ContentListView(ListView,pk):
#     template_name = 'blog.html'
#     context_object_name = 'content'

#     def get_queryset(self):
#         blog = Blog.objects.get(id=pk)
#         article = blog.article.all()
#         article_image = blog.image_article.all()

#         # Combine and order the articles and videos by publication date
#         content = sorted(
#             list(article) + list(article_image),
#             key=lambda obj: obj.pub_date,
#             reverse=True
#         )
#         return content

def blog_view(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    items = []

    image_articles = blog.image_article_set.all()
    articles = blog.article_set.all()

    content = sorted(
            list(articles) + list(image_articles),
            key=lambda obj: obj.pub_time,
            reverse=False
        )
    context={'blog': blog,'items': content}
    return render(request,'blog.html',context)

def search_view(request):
    q = request.GET.get('search') if request.GET.get('search') != None else ''
    
    blogs = Blog.objects.filter(
        Q(title__icontains=q) |
        Q(title_arabic__icontains=q) 
        )
        
    vocabularies = Vocabularies.objects.filter(
            Q(title__icontains=q) |
            Q(title_arabic__icontains=q) 
        )
    conversations = Conversations.objects.filter(
            Q(title__icontains=q) |
            Q(title_arabic__icontains=q) 
        )
        
    slangs = Slang.objects.filter(
            Q(sentence_english__icontains=q) |
            Q(sentence_arabic__icontains=q) 
        )
    phrasal_verbs = Phrasal_Verb.objects.filter(
            Q(sentence_english__icontains=q) |
            Q(sentence_arabic__icontains=q) 
        )
    adjectives = Adj.objects.filter(
            Q(sentence_english__icontains=q) |
            Q(sentence_arabic__icontains=q) 
        )
    useful_sentenes = Useful_sentene.objects.filter(
            Q(sentence_english__icontains=q) |
            Q(sentence_arabic__icontains=q) 
        )
    common_words = Common_Word.objects.filter(
            Q(sentence_english__icontains=q) |
            Q(sentence_arabic__icontains=q) 
        )
    searched_list = list(blogs)+list(conversations)+list(vocabularies)+list(useful_sentenes)+list(common_words)+list(slangs)+list(adjectives)+list(phrasal_verbs)
    context= {
            'searched_list':searched_list,
            'ml':['Conversations','story','vocabulary','blog']
        }
    return render(request,'search.html',context)
