from django.conf.urls import url

from . import views

urlpatterns = [
    url ( r"^$", views.index, name = "index" ),
    url ( r"^algorithm/(?P<algorithm_id>[0-9]+)/$", views.algorithm, name = "algorithm" ),
    url ( r"^classification/(?P<classification_id>[0-9]+)/$", views.classification, name = "classification" ),
    url ( r"^result/(?P<result_id>[0-9]+)/$", views.result, name = "result" ),
    url ( r"^sample/(?P<sample_id>[0-9]+)/$", views.sample, name = "sample" ),
    url ( r"^sample_input/(?P<sample_input_id>[0-9]+)/$", views.sample_input, name = "sample_input" ),
    url ( r"^sample_image_wing/(?P<sample_image_wing_id>[0-9]+)/$", views.sample_image_wing, name = "sample_image_wing" ),
    ]
