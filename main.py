class SeatBooking:
    def __init__(self):
        # customize the seat map, with A_F and 1-80 columns
        # X = Aisle, S = Storage, F = Free, R = Reserved
        self.row_labels = ['A', 'B', 'C', 'D', 'E', 'F',]
        self.column_labels = [str(i) for i in range(1, 81)]
        # Example layout with aisles approximately after every 20 seats for simplicity
        self.seat_map = [['F' if (i + 1) % 20 != 0 else 'X' for i in range(80)] for _ in self.row_labels]



    # function to run the program
    def run(self):
        """ Main menu for the seat booking application. """
        choice = ''
        # print the menu unless the user exits
        while choice != '5':
            print("\nMenu:")
            print("1. Check Seat Availability")
            print("2. Book a Seat")
            print("3. Free a Seat")
            print("4. Show Booking State")
            print("5. Exit Program")
            choice = input("Choose an option (1-5): ")


# run the application
if __name__ == "__main__":
    booking_app = SeatBooking()
    booking_app.run()