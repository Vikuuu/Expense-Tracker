from django.urls import path
from .views import ExpenseSummaryStats, IncomeSummaryStats


urlpatterns = [
    path(
        "expense-category-data/",
        ExpenseSummaryStats.as_view(),
        name="expense-category-data",
    ),
    path(
        "income-source-data/",
        IncomeSummaryStats.as_view(),
        name="income-source-data",
    ),
]
