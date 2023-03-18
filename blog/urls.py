from django.urls import path
from .views import homeView, blogPage, addBlog, editBlog, deleteBlog, addCategory

urlpatterns = [
    # path('',views.home, name="home"),
    path('', homeView.as_view(), name='home'),
    path('blog/<slug:slug>', blogPage.as_view(), name='blogPage'),
    path('addBlog', addBlog.as_view(), name='addBlog'),
    path('editBlog/<slug:slug>', editBlog.as_view(), name='editBlog'),
    path('deleteBlog/<slug:slug>', deleteBlog.as_view(), name='deleteBlog'),
    path('addCategory', addCategory.as_view(), name='addCategory'),
]