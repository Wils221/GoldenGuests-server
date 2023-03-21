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
        if "isOrgTicket" in request.query_params:
            tickets = Ticket.objects.filter(isOrgTicket=request.query_params['isOrgTicket'])

        elif "user" in request.query_params:
            goldenguest = GoldenGuest.objects.get(user=request.query_params['user'])
            tickets = Ticket.objects.filter(goldenguest=goldenguest)    
        #get value of type query string parm
        #if value is claimed filter tickets to Claimed Org Tickets
        #tickets.filter(insert rules here on how to filter)
        
        #if value = unclaimed then filter to Available Org Tickets
        
        #if vaule = THcreated then fiter to tickets assined to the logged in user.
        else:
            tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)

        return Response(serializer.data)

    def create(self, request):

        goldenguest = GoldenGuest.objects.get(user=request.auth.user)
        opponent = Opponent.objects.get(pk=request.data["opponent"])

        ticket = Ticket.objects.create(
            section=request.data["section"],
            number_of_tickets=request.data["number_of_tickets"],
            date=request.data["date"],
            goldenguest=goldenguest,
            opponent=opponent
        )

        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.section = request.data ["section"]
        ticket.number_of_tickets = request.data ["number_of_tickets"]
        ticket.date = request.data ["date"]
        ticket.isOrgTicket = request.data ['isOrgTicket']
        opponent = Opponent.objects.get(pk=request.data ["opponent"])
        # if request.data ['isOrgTicket'] == 
        goldenguest = GoldenGuest.objects.get(user=request.data["goldenguest"])
        ticket.opponent = opponent
        ticket.goldenguest = goldenguest
        ticket.save()


        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class GoldenGuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoldenGuest
        fields = ('id', 'first_name', 'email')    


class TicketSerializer(serializers.ModelSerializer):
    goldenguest=GoldenGuestSerializer()
    class Meta:
        model = Ticket
        fields = ('id', 'section', 'number_of_tickets', 'date', 'goldenguest', 'opponent','isOrgTicket')
        depth = 1
