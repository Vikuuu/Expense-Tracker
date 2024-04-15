from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import IncomeSerializer
from .models import Income
from rest_framework import permissions
from .permissions import IsOwner


class IncomeListView(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    # over-riding this method so that the logged in user is the one that is added in the model of the expense
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # over-riding this method so that the logged user gets only there expenses list.
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner,
    ]
    lookup_field = "id"

    # over-riding this method so that the logged user gets only there expenses list.
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
