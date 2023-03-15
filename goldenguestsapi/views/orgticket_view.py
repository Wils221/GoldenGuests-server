from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goldenguestsapi.models import GoldenGuest,OrgTicket, Ticket


class OrgTicketView(ViewSet):

    def retrieve(self, request, pk):
        orgTicket = OrgTicket.objects.get(pk=pk)
        serializer = OrgTicketSerializer(orgTicket)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        orgTicket = OrgTicket.objects.all()
        serializer = OrgTicketSerializer(orgTicket, many=True)
        return Response(serializer.data)

    def create(self, request):

        goldenguest = GoldenGuest.objects.get(pk=request.data["GoldenGuest"])
        ticket = Ticket.objects.get(pk=request.data["Ticket"])

        orgTicket = OrgTicket.objects.create(
            goldenguest=goldenguest,
            ticket=ticket
        )

        serializer = OrgTicketSerializer(orgTicket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        orgTicket = OrgTicket.objects.get(pk=pk)
        orgTicket.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OrgTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgTicket
        fields = ('id', 'goldenguest', 'ticket')
        depth = 1