from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goldenguestsapi.models import Opponent

class OpponentView(ViewSet):

    def retrieve(self, request, pk):
        opponent = Opponent.objects.get(pk=pk)
        serializer = OpponentSerializer(opponent)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        opponent = Opponent.objects.all()
        serializer = OpponentSerializer(opponent, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        opponent = Opponent.objects.get(pk=pk)
        opponent.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class OpponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opponent
        fields = ('id', 'opponent')
