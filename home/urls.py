from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home , name = "home"),
    path('form/' , views.contact , name = "contact"),
    path('edit/<int:id>/' , views.update , name = "update"),
    path('delete/<int:id>/' , views.delete , name = "delete")

]


