from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from goldenguestsapi.models import GoldenGuest


class GoldenGuestView(ViewSet):

    def retrieve(self, request, pk):
        goldenGuest = GoldenGuest.objects.get(pk=pk)
        serializer = GoldenGuestSerializer(goldenGuest)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        goldenGuest = GoldenGuest.objects.all()
        serializer = GoldenGuestSerializer(goldenGuest, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        goldenGuest = GoldenGuest.objects.get(pk=pk)
        goldenGuest.isTicketHolder = request.data["isTicketHolder"]
        goldenGuest.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        goldenGuest = GoldenGuest.objects.get(pk=pk)
        goldenGuest.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GoldenGuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoldenGuest
        fields = ('id', 'user', 'isTicketHolder')
        depth = 1
