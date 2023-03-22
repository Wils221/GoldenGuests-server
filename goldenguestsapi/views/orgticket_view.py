from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goldenguestsapi.models import GoldenGuest,OrgTicket, Ticket, Opponent


class OrgTicketView(ViewSet):

    def retrieve(self, request, pk):
        orgTicket = OrgTicket.objects.get(pk=pk)
        serializer = OrgTicketSerializer(orgTicket)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        if "orguser" in request.query_params:
            goldenguest = GoldenGuest.objects.get(user=request.query_params['orguser'])
            orgTickets = OrgTicket.objects.filter(goldenguest=goldenguest)    
        else:
            orgTickets = OrgTicket.objects.all()
        serializer = OrgTicketSerializer(orgTickets, many=True)
        return Response(serializer.data)

    def create(self, request):

        goldenguest = GoldenGuest.objects.get(user=request.data["GoldenGuest"])
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
    
class GoldenGuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoldenGuest
        fields = ('id', 'first_name', 'email')    
    
class OpponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opponent
        fields = ('id', 'opponent')
    
class TicketSerializer(serializers.ModelSerializer):
    opponent=OpponentSerializer()
    class Meta:
        model = Ticket
        fields = ('id', 'section', 'number_of_tickets', 'date', 'goldenguest', 'opponent')    


class OrgTicketSerializer(serializers.ModelSerializer):
    ticket=TicketSerializer()
    goldenguest=GoldenGuestSerializer()
    class Meta:
        model = OrgTicket
        fields = ('id', 'goldenguest', 'ticket')
        depth = 1