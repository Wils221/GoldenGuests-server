from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goldenguestsapi.models import GoldenGuest, Opponent, Ticket, OrgTicket

class TicketView(ViewSet):


    def retrieve(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)
    
    def create(self, request):

        genre = Genre.objects.get(pk=request.data["genre"])

        ticket = Ticket.objects.create(
        name=request.data["name"],
        description=request.data["description"],
        genre=genre
    )
        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('id', 'section', 'number_of_tickets', 'date', 'goldenguest', 'opponent' )
        depth= 1