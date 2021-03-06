from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class PublishedManager(models.Manager): 
    def get_queryset(self): 
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Task(models.Model): 
    STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    ) 
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250,  
                            unique_for_date='publish') 
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='user_tasks')     
    body = models.TextField() 
    image = models.ImageField(upload_to='tasks/%Y/%m/%d/', blank=True)
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,  
                              choices=STATUS_CHOICES, 
                              default='draft') 
    
    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.

    class Meta: 
        ordering = ('-publish',) 
        verbose_name_plural = "tasks"

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('activity:task_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

class Activity(models.Model): 
    STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    ) 
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250,  
                            unique_for_date='publish') 
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='activities')
    tasks = models.ManyToManyField(Task)
    body = models.TextField() 
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,  
                              choices=STATUS_CHOICES, 
                              default='draft') 
    
    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.

    class Meta: 
        ordering = ('-publish',) 
        verbose_name_plural = "activities"

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('activity:activity_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
