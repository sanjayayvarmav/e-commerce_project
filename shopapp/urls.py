
from django.urls import path

import shopapp
from shopapp import views
app_name='shopapp'

urlpatterns = [

    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='prdcts_catgry'),
    path('<slug:c_slug>/<slug:p_slug>/',views.p_details,name='prdctdetails'),
]
