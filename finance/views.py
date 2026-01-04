from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # C'est la partie "Magique" pour ta démo
    @action(detail=False, methods=['get'])
    def summary(self, request):
        # Calcule la somme des revenus
        income = Transaction.objects.filter(category__type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
        # Calcule la somme des dépenses
        expense = Transaction.objects.filter(category__type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
        
        return Response({
            "total_income": income,
            "total_expense": expense,
            "balance": income - expense
        })
