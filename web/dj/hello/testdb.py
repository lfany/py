from __future__ import absolute_import

from django.http import HttpResponse

import sys

sys.path.append('..')
from Model.models import TestModel


def insertdb(request):
    model = TestModel(name='hello')
    model.save()
    return HttpResponse('<p>add data success!</p>')


def selectdb(request):
    response = ''
    response1 = ''

    list = TestModel.objects.all()

    response2 = TestModel.objects.filter(id=1)

    response3 = TestModel.objects.get(id=1)

    TestModel.objects.order_by('name')[0:2]

    TestModel.objects.order_by('id')

    TestModel.objects.filter(name='hello').order_by('id')

    for var in list:
        response1 += '<li>' + str(var.id) + '  ' + var.name + '</li>'
    response = response1
    return HttpResponse('<p><ul>' + response + '</ul></p>')
