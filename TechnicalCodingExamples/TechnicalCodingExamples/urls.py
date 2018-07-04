"""TechnicalCodingExamples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from PythonTechnicalExamples import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'python/$', views.python, name='python'),
    url(r'helloworld/$', views.helloworld, name='helloworld'),
    url(r'helloworld1/$', views.helloworld1, name='helloworld1'),
    url(r'helloworld2/$', views.helloworld2, name='helloworld2'),
    url(r'helloworld3/$', views.helloworld3, name='helloworld3'),
    url(r'sum/$', views.sumofnum, name='sum'),
    url(r'sumofnum1/$', views.sumofnum1, name='sumofnum1'),
    url(r'sumofnum2/$', views.sumofnum2, name='sumofnum2'),
    url(r'sumofnum3/$', views.sumofnum3, name='sumofnum3'),
    url(r'evennumbers/$', views.evenrange, name='evennumbers'),
    url(r'even/$', views.even, name='even'),
    url(r'even2/$', views.even2, name='even2'),
    url(r'even3/$', views.even3, name='even3'),
    url(r'even4/$', views.even4, name='even4'),
    url(r'odd/$', views.Odd, name='odd'),
    url(r'odd1/$', views.Odd1, name='odd1'),
    url(r'odd2/$', views.Odd2, name='odd2'),
    url(r'odd3/$', views.Odd3, name='odd3'),
    url(r'odd4/$', views.Odd4, name='odd4'),
    url(r'prime/$', views.prime, name='prime'),
    url(r'prime1/$', views.prime1, name='prime1'),
    url(r'prime2/$', views.prime2, name='prime2'),
    url(r'prime3/$', views.prime3, name='prime3'),
    url(r'feb/$', views.feb, name='feb'),
    url(r'feb1/$', views.feb1, name='feb1'),
    url(r'additionofmatrix/$', views.additionofmatix, name='additionofmatrix'),
    url(r'^admin/', admin.site.urls),
]
