from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goldenguestsapi.models import GoldenGuest, Opponent, Ticket


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

        goldenguest = GoldenGuest.objects.get(pk=request.data["GoldenGuest"])
        opponent = Opponent.objects.get(pk=request.data["Opponent"])

        ticket = Ticket.objects.create(
            section=request.data["section"],
            number_of_tickets=request.data["number_of_tickets"],
            date=request.data["date"],
            goldenguest=goldenguest,
            opponent=opponent
        )

        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('id', 'section', 'number_of_tickets', 'date', 'goldenguest', 'opponent')
        depth = 1
