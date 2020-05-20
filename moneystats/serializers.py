from rest_framework import serializers
from .models import Check, Category, Expense


class CheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Check
        fields = ['date']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = '__all__'


class DiagramCategorySerializer(serializers.ModelSerializer):

    expenses = ExpenseSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'expenses']
