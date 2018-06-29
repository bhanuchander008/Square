from rest_framework.decorators import api_view
from rest_framework.response import Response
from list.models import TestSquare
from django.shortcuts import render
from django.core import serializers
from .serializers import TestSquareSerializer
from django.http import JsonResponse
import MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = 'bhanu123'
DATABASE = 'details'


@api_view(['GET'])
def Test(request):
	return Response({'Everything': 'Fair and Lovely', 'Welcome': 'everybody'})

@api_view(['GET'])
def getNumber(request,_Number):
    _Number = _Number.replace('%', ' ')
    stud = TestSquare.objects.filter(Number= _Number)
    if stud:
        serializer = TestSquareSerializer(stud,many=True)
        return Response(serializer.data)

    else:
        return Response({"Message": ' Number NOT FOUND'})

@api_view(['GET'])
def get(request, _num):
    _mar = TestSquare.objects.filter(Number = _num)
    if _mar:
        serializer = sqmathserializer(_mar, many = True)
        return Response(serializer.data)
    else:
        _sq = int(_num) * int(_num)
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('INSERT INTO list_testsquare(Number, SquareNumber) values(%s, %s)',(float(_num),float(_sq)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': "New number and it's square inserted", 'Number': _num, 'Square': _sq})


@api_view(['GET'])
def post(request, _values):
    _num, _sq = _values.split('-')
    _mar = TestSquare.objects.filter(Number = _num)
    if _mar:
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('UPDATE list_testsquare SET SquareNumber = %s WHERE Number = %s',(float(_sq),float(_num)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': 'Square of the given number is updated', 'Number': _num, 'Square': _sq})
    else:
        db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
        cursor = db.cursor()
        cursor.execute('INSERT INTO app_sqmath (Number, SquareNumber) values(%s, %s)',(float(_num),float(_sq)))
        db.commit()
        cursor.close()
        print (_sq)
        return Response({'Message': 'New number and square inserted', 'Number': _num, 'SquareNumber': _sq})
