from django.urls import path
from review.api import views as api_view


urlpatterns = [
    path('review/', api_view.review_list_api_view.as_view(), name="review-list"),
    path('review/<int:pk>', api_view.review_details_api_view.as_view(), name="review-detail"),
    path('review/<int:book_pk>/make_review/', api_view.review_make_api_view.as_view(), name="make-review"),
]
