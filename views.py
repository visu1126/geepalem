from django.shortcuts import render

from rest_framework.views import APIView
from .serializers import goodsSerializers
from .models import goods
from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class itemcrud(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        students_qs = goods.objects.all()
        student_serializers = goodsSerializers(students_qs, many=True)
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(goods, id=pk)
        student_serializers = goodsSerializers(student)
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def create(self, request):
        student_serializers = goodsSerializers(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, ):
        student = get_object_or_404(goods, id=pk)
        student_serializers = goodsSerializers(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None, ):
        student = get_object_or_404(goods, id=pk)
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)
