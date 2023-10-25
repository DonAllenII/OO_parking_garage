from random import randint
from IPython.display import clear_output

#Create the class parking_garage
class Parking_garage():
    #init attributes
    def __init__(self, spaces, park_price):
        self.tickets = [x for x in range(spaces)]
        self.parkingSpaces = [x for x in range(spaces)]
        self.oustandingTickets = {}
        self.currentTicket = None
        self.price = park_price

    def takeTicket(self):  #takeTicket method
        self.currentTicket = randint(1,(len(self.parkingSpaces) - 1))
        #should decrease the amount of tickets avaiable by 1
        self.tickets.remove(self.currentTicket)
        #should decrease the amount of parkingSpace avaible by 1
        self.parkingSpaces.remove(self.currentTicket)

        self.oustandingTickets[self.currentTicket] = {'paid' : False}
        print(self.oustandingTickets)
        print("\n\n")
        print(f'You have space #{self.currentTicket}.')
        return

    def payForParking(self):
        while True:
            try:
                space = int(input('Please enter space #...'))
                if space in self.oustandingTickets.keys():
                #if space a valid oustanding number
                    self.currentTicket = space
                    while True:
                        #display an input that waits for an amount from the user and store it in a variable
                        payment = float(input(f'Parking cost is {self.price}. Please enter payment..'))
                        #if the payment variable is not empty then 
                        if payment >= self.price:
                            self.oustandingTickets[self.currentTicket]['paid'] = True
                            #update oustandingTickets dictionary key "paid" to true
                            break
                        else:
                            print("Please pay off ticket in full")
                    if self.oustandingTickets[self.currentTicket]['paid'] == True:
                        break
                else:
                    print(f'# {space} is not a valid outstanding parking space number')
            except ValueError:
                print("Please enter numbers only\n\n")
        return
    def leaveGarage(self):
        while True:
        #if currentTicket paid, display a message of "Thank You, have a nice day"
            if self.oustandingTickets[self.currentTicket]['paid'] ==  True:
                print('\nThank You, have a nice day!')
            #update parkingSpaces list to increase by 1
                self.tickets.insert(self.currentTicket, self.currentTicket)
            #update tickets list to increase by 1
                self.parkingSpaces.insert(self.currentTicket, self.currentTicket)
                del self.oustandingTickets[self.currentTicket]
                break
                
            clear_output()

        #if currentTicket not pad, display an input prompt for payment
            if self.oustandingTickets[self.currentTicket]['paid'] == False:
                print('Please pay for parking in full before attempting to leave')
                self.payForParking()


    def run(self):
        while True:
            answer = str(input(" Press 'P' for a parking ticket\n Press 'E' to exit\n Press 'Q' to quit\n\n\n\n"))
            if answer.lower() == 'p':
                self.takeTicket()
            if answer.lower() == 'e':
                self.payForParking()
                self.leaveGarage()
            if answer.lower() == 'q':
                break
            

parking_garage = Parking_garage(20, 5.99)
parking_garage.run()
        