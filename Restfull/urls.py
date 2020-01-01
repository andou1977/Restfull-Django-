"""Restfull URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, include
from rest_framework import routers


from Api import views

router = routers.DefaultRouter()
router.register('Institution', views.InstitutionView)
router.register('Faculter', views.FaculterView)
router.register('Option', views.OptionView)
router.register('Expert', views.ExpertView)
router.register('Utilisateur', views.UtilisateurView)


urlpatterns = [
    # url(r'^$', views.index),
    #  path('admin/', admin.site.urls),

    path("polls/", views.polls_list, name="polls_list"),
    path("polls/<int:pk>/", views.polls_detail, name="polls_detail"),

    path('', include(router.urls))

]
