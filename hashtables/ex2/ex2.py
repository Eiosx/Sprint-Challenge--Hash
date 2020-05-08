#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    ticketsDict = {}
    ticketsRoute = []

    for i in tickets:

        ticketsDict[i.source] = i.destination

    for i in range(len(tickets)):

        if i == 0:
            ticketsRoute.append(ticketsDict['NONE'])
        else:
            key = ticketsRoute[i - 1]
            ticketsRoute.append(ticketsDict[key])

    return ticketsRoute
