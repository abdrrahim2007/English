
from django.db import models
from django.urls import reverse

class Conversations(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200)
    title_arabic = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    model = 'Conversations'
    @property
    def ImageURL(self):
        try:
           url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('conversation',args=[self.slug])


class Conversation(models.Model):
    conversation =  models.ForeignKey(Conversations,on_delete=models.CASCADE)

    sentence_english = models.TextField(null=True,blank=True)
    sentence_arabic = models.TextField(null=True,blank=True)
    song = models.FileField(null=True, blank=True)
    
    
    @property
    def SongURL(self):
        try:
           url = self.song.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.sentence_english

# class Stories(models.Model):
#     title = models.CharField(max_length=200, null=True)
#     title_arabic = models.CharField(max_length=200, null=True)
#     story = models.ManyToManyField('Story',  blank=True)

#     def __str__(self):
#         return self.title

class Story(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200)
    model= 'story'
    title_arabic = models.CharField(max_length=200, null=True)
    story_english = models.TextField()
    story_arabic = models.TextField()
    story_image = models.ImageField(null=True, blank=True)
    song = models.FileField(null=True, blank=True)
    
    @property
    def SongURL(self):
        try:
           url = self.song.url
        except:
            url = ''
        return url
    @property
    def ImageURL(self):
        try:
           url = self.story_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('story',args=[self.slug])

class Adj(models.Model):
    sentence_english = models.CharField(max_length=200, null=True)
    sentence_arabic = models.CharField(max_length=200, null=True)
    song = models.FileField(null=True, blank=True)
    model='adj'
    @property
    def SongURL(self):
        try:
           url = self.song.url
        except:
            url = ''
        return url
    def get_absolute_url(self):
        return reverse('adj')


    def __str__(self):
        return self.sentence_english
        
class Slang(models.Model):
    sentence_english = models.CharField(max_length=200, null=True)
    sentence_arabic = models.CharField(max_length=200, null=True)
    song = models.FileField(null=True, blank=True)
    model='slang'
    @property
    def SongURL(self):
        try:
           url = self.song.url
        except:
            url = ''
        return url
    

    def __str__(self):
        return self.sentence_english
    def get_absolute_url(self):
        return reverse('slang')

class Phrasal_Verb(models.Model):
    sentence_english = models.CharField(max_length=200, null=True)
    sentence_arabic = models.CharField(max_length=200, null=True)
    song = models.FileField(null=True, blank=True)
    model='phrasal_verb'
    @property
    def SongURL(self):
        try:
           url = self.song.url
        except:
            url = ''
        return url
    def get_absolute_url(self):
        return reverse('phver')


    def __str__(self):
        return self.sentence_english
class Useful_sentene(models.Model):
    sentence_english = models.CharField(max_length=200, null=True)
    sentence_arabic = models.CharField(max_length=200, null=True)
    song = models.FileField(null=True, blank=True)
    model='useful_sentene'
    @property
    def SongURL(self):
        try:
           url = self.song.url
        except:
            url = ''
        return url
    def get_absolute_url(self):
        return reverse('usefulse')


    def __str__(self):
        return self.sentence_english
class Common_Word(models.Model):
    sentence_english = models.CharField(max_length=200, null=True)
    sentence_arabic = models.CharField(max_length=200, null=True)
    song = models.FileField(null=True, blank=True)
    model='common_word'
    @property
    def SongURL(self):
        try:
           url = self.song.url
        except:
            url = ''
        return url
    

    def __str__(self):
        return self.sentence_english
    def get_absolute_url(self):
        return reverse('commonWords')

class Vocabularies(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200)
    title_arabic = models.CharField(max_length=200, null=True)
    model='vocabulary'
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('vocabulary',args=[self.slug])

class Vocabulary(models.Model):
    vocabulary =  models.ForeignKey(Vocabularies,on_delete=models.CASCADE)

    sentence_english = models.CharField(max_length=400, null=True)
    sentence_arabic = models.CharField(max_length=400, null=True)
    song = models.FileField(null=True, blank=True)
    
    @property
    def SongURL(self):
        try:
           url = self.song.url
        except:
            url = ''
        return url


    def __str__(self):
        return self.sentence_english

class Blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200,unique=True)
    model='blog'
    title_arabic = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=False, blank=False)

    intro = models.TextField()
    pub_time      =  models.DateTimeField(auto_now_add=True)
    
    @property
    def ImageURL(self):
        try:
           url = self.image.url
        except:
            url = ''
        return url 
        
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog',args=[self.slug])
        
class Article(models.Model):
    name = 'article'
    blog =  models.ForeignKey(Blog,on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    content_text = models.TextField()
    pub_time      =  models.DateTimeField(auto_now_add=True)
class Image_article(models.Model):
    blog =  models.ForeignKey(Blog,on_delete=models.CASCADE)
    name = "image_article"
    title = models.CharField(max_length=200, null=True)
    content_image = models.ImageField(null=True, blank=True)
    pub_time      =  models.DateTimeField(auto_now_add=True)
    @property
    def ImageURL(self):
        try:
           url = self.content_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title