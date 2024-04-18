from rest_framework.views import APIView
import datetime
from expenses.models import Expenses
from income.models import Income
from rest_framework import response, status


class ExpenseSummaryStats(APIView):

    def get_category(self, expense):
        return expense.category

    def get_amount_for_category(self, expense_list, category):
        expenses = expense_list.filter(category=category)
        amount = 0
        for expense in expenses:
            amount += expense.amount

        return {"amount": str(amount)}

    def get(self, request):
        todays_date = datetime.date.today()
        year_ago_date = todays_date - datetime.timedelta(days=365)
        expenses = Expenses.objects.filter(
            owner=request.user,
            date__gte=year_ago_date,
            date__lte=todays_date,
        )

        context = {}
        categories = list(set(map(self.get_category, expenses)))

        for expense in expenses:
            for category in categories:
                context[category] = self.get_amount_for_category(expenses, category)

        return response.Response({"category_data": context}, status=status.HTTP_200_OK)


class IncomeSummaryStats(APIView):

    def get_source(self, expense):
        return expense.source

    def get_amount_for_source(self, expense_list, source):
        expenses = expense_list.filter(source=source)
        amount = 0
        for expense in expenses:
            amount += expense.amount

        return {"amount": str(amount)}

    def get(self, request):
        todays_date = datetime.date.today()
        year_ago_date = todays_date - datetime.timedelta(days=365)
        expenses = Income.objects.filter(
            owner=request.user,
            date__gte=year_ago_date,
            date__lte=todays_date,
        )

        context = {}
        sources = list(set(map(self.get_source, expenses)))

        for expense in expenses:
            for source in sources:
                context[source] = self.get_amount_for_source(expenses, source)

        return response.Response({"source_data": context}, status=status.HTTP_200_OK)
