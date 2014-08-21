from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'book.views.index'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','bookstore.book.views.index'),
    #url(r'^books/(?p<book_id>\d+)/$','bookstore.book.views.detail'),

    url(r'^admin/', include(admin.site.urls)),
)
