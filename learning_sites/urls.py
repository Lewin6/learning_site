"""define urlpatternsof learning_sites """
from django.urls import path, re_path
from . import views

# namespace
app_name = 'learning_sites'

urlpatterns=[
    # index
    path('', views.index, name='index'),
    # display all topics
    path('topics', views.topics, name='topics'),
    # specific topic's detail page
    path('topics/<topic_id>', views.topic, name='topic'),
    # add a new topic
    path('new_topic',views.new_topic,name='new_topic'),
    # add a new entry
    path('new_entry/<topic_id>',views.new_entry,name='new_entry'),
    # page for editing entry
    path('edit_entry/<entry_id>',views.edit_entry, name='edit_entry'),
]