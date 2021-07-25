from .serializer import ReviewsSerializer
from django.shortcuts import render
from django.db import models
from rest_framework import generics
from .models import Reviews

# Create your views here.
class ReviewsListView(generics.ListCreateAPIView):    
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()




class ReviewsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()