from django.conf.urls import url
import views

urlpatterns = [
    url(r'^donors/$',views.DonorList.as_view(), name='donor_list'),
    url(r'^donor/create/(?P<pk>[0-9]+)/$',views.DonorDetail.as_view(),name='donor_detail'),
    url(r'^donor/create/$',views.DonorCreate.as_view(),name='donor_create'),
    url(r'^donor/update/(?P<pk>[0-9]+)/$',views.DonorUpdate.as_view(),name='donor_edit'),
    url(r'^donor/delete/(?P<pk>[0-9]+)/$',views.DonorDelete.as_view(),name='donor_delete'),
]