from django.urls import path
from .views import ExpenseSummaryStats


urlpatterns = [
    path(
        "expense-category-data/",
        ExpenseSummaryStats.as_view(),
        name="expense-category-data",
    ),
]
