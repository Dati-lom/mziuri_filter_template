from ast import Dict, Tuple
from dataclasses import dataclass
from encodings.punycode import T
from pyexpat import model
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

@dataclass
class SearchTerm:
    model: str
    make: str
    
    model_year: Tuple[int,int]
    
    price: Tuple[float, float]
    year: Tuple[int, int]
    stock: Tuple[int, int]
    
    additional_filters: Dict[str, Any]

#
def get_all(request):
    pass

def get(request, car_id):
    pass

def get_by_make(request, make):
    pass

def get_by_price_range(request, min_price, max_price):
    pass

#ეს მერე ვქნათ
def get_by_make_or_model(request, search_term:SearchTerm):
    pass