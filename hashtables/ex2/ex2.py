#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here # create an array with the same length as the tickets array
    destinations = [None] * length
    destination_lookup = dict()

    # store it's ticket's destination
    for ticket in tickets:
        destination_lookup[ticket.source] = ticket.destination
        # print(f"destination lookup: {destination_lookup}") # the chain starts with NONE

    # the starting ticket has a source of "NONE". Start there to build a chain
    next_destination = destination_lookup['NONE']

    for i in range(0, length):
        # record next destination
        destinations[i] = next_destination
        print(f"destinations[i]: {destinations[i]}")

        # retrieve next destination
        next_destination = destination_lookup[next_destination]
        print(f"next_destination: {next_destination}")

    return destinations
