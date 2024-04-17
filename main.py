class SeatBooking:
    def __init__(self):
        # customize the seat map, with A_F and 1-80 columns
        # X = Aisle, S = Storage, F = Free, R = Reserved
        self.row_labels = ['A', 'B', 'C', 'D', 'E', 'F',]
        self.column_labels = [str(i) for i in range(1, 81)]
        # Example layout with aisles approximately after every 20 seats for simplicity
        self.seat_map = [['F' if (i + 1) % 20 != 0 else 'X' for i in range(80)] for _ in self.row_labels]

    def display_seats(self):
        """ Display the current seat map. """
        # Print header with column labels
        print("\nCurrent Seat Map:")
        print("     " + " ".join(self.column_labels))
        # Print each row with row labels
        for i in range(len(self.seat_map)):
            print(self.row_labels[i] + "   " + " ".join(self.seat_map[i]))
        print()  # Empty line for better formatting
    def check_availability(self):
        """ Checks and displays available seats. """
        print("\nAvailable Seats:")
        available = False
        # go over the seat map to find free seats and print
        for i, row in enumerate(self.seat_map):
            for j, seat in enumerate(row):
                if seat == 'F':
                    print(f"{self.row_labels[i]}{self.column_labels[j]}", end=' ')
                    available = True
        if not available:
            print("No available seats.")
        else:
            print()
        print() # Empty line for better formatting



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

            if choice == '1':
                self.check_availability()


            elif choice == '4':
                self.display_seats()
            elif choice == '5':
                print("Exiting the program.")  # Inform user of program exit
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")  # Inform if choice is invalid


# run the application
if __name__ == "__main__":
    booking_app = SeatBooking()
    booking_app.run()