from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from urllib3 import request
from pagination.models import *


def pagination(request):
    all_items = paginationData.objects.all()
    p = Paginator(all_items, 3)

    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {'items': page}
    return render(request, 'index.html', context)
