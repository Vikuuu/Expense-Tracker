from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpenseSerializer
from .models import Expenses
from rest_framework import permissions
from .permissions import IsOwner


class ExpenseListView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expenses.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    # over-riding this method so that the logged in user is the one that is added in the model of the expense
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # over-riding this method so that the logged user gets only there expenses list.
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expenses.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner,
    ]
    lookup_field = "id"

    # over-riding this method so that the logged in user is the one that is added in the model of the expense
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # over-riding this method so that the logged user gets only there expenses list.
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
