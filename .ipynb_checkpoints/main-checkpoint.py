from random import randint
from IPython.display import clear_output

#Create the class parking_garage
class Parking_garage():
    #init attributes
    def __init__(self, spaces, park_price):
        self.tickets = [x for x in range(spaces)]
        self.parkingSpaces = [x for x in range(spaces)]
        self.currentTicket = {}
        self.price = park_price

    def takeTicket(self):  #takeTicket method
        self.ticket = randint(1,(len(self.parkingSpaces) - 1))
        #should decrease the amount of tickets avaiable by 1
        self.tickets.remove(self.ticket)
        #should decrease the amount of parkingSpace avaible by 1
        self.parkingSpaces.remove(self.ticket)

        self.currentTicket['paid'] = False
        return

    def payForParking(self):
        #display an input that waits for an amount from the user and store it in a variable
        payment = float(input('Please enter payment..'))
        #if the payment variable is not empty then 
        if payment > self.price:
            self.currentTicket['paid'] = True
        #update currentTicket dictionary key "paid" to true
        return
    def leaveGarage(self):
        while True:
        #if ticket paid, display a message of "Thank You, have a nice day"
            if self.currentTicket['paid'] == True:
                print('Thank You, have a nice day!')
            #update parkingSpaces list to increase by 1
                self.tickets.insert(self.ticket, self.ticket)
            #update tickets list to increase by 1
                self.parkingSpaces.insert(self.ticket, self.ticket)
                del self.currentTicket['paid']
                break
                
            clear_output()

        #if ticket not pad, display an input prompt for payment
            if self.currentTicket['paid'] == False:
                self.payForParking()
                print('Please pay off ticket in full')
            
        