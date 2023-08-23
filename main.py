from random import randint

#Create the class parking_garage
class Parking_garage():
    #init attributes
    def __init__(self,spaces):
        self.tickets = [x for x in range(spaces)]
        self.parkingSpaces = [x for x in range(spaces)]
        self.currentTicket = {}

    def takeTicket(self):  #takeTicket method
        ticket = randint(1,(len(self.parkingSpaces) - 1))
        #should decrease the amount of tickets avaiable by 1
        self.tickets.remove(ticket)
        #should decrease the amount of parkingSpace avaible by 1
        self.parkingSpaces.remove(ticket)

        self.currentTicket[ticket] = 'unpaid'
        return

    def payForParking():
        #display an input that waits for an amount from the user and store it in a variable

        #if the payment variable is not empty then 

        #update currentTicket dictionary key "paid" to true
        retun
    def leaveGarage():
        #if ticket paid, display a message of "Thank You, have a nice day"
        #if ticket not pad, display an input prompt for payment
            #once paid, display message "Thank you, have a nice day!"
        #update parkingSpaces list to increase by 1
        #update tickets list to increase by 1
        return