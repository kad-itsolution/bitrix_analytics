from django.http import HttpResponse
from django.shortcuts import render

from bitrix_analysis.models import RuSitesAll, BitrixOnSites
from bitrix_analysis.find_bitrix import find_bitrix


# Create your views here.
def default(request, start=0, finish=0):
    if start == 0 and finish == 0:
        return HttpResponse("search_for_bitrix/<int:start>/<int:finish>", content_type="text/plain")
    res = RuSitesAll.objects.all()[start:finish]
    for i in res:
        ans = find_bitrix(i)
        print(ans)
        BitrixOnSites.objects.create(id=i,
                                     domain=ans["url"],
                                     found_bitrix=ans["found_bitrix"],
                                     had_redirect=ans["had_redirect"],
                                     status=ans["status"],
                                     )
    return HttpResponse("return this string", content_type="text/plain")
