from django.http import HttpResponse

import sys, os

# from Model.models import TestModel
# Add the project to the python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
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


def updatedb(request):
    test1 = TestModel.objects.get(id=1)
    test1.name = 'world'
    test1.save()

    TestModel.objects.filter(id=2).update(name='Google')

    # TestModel.objects.all().update(name='Google')

    return HttpResponse('<p>修改成功; <a href=\'/selectdb\'>点击查看</a></p>')


def deletedb(request):
    test1 = TestModel.objects.get(id=1)
    test1.delete()

    TestModel.objects.filter(id=1).delete()

    return HttpResponse('<p>删除成功; <a href=\'/selectdb\'>点击查看</a></p>')
