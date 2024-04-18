from tabulate import tabulate
class SeatBooking:
    def __init__(self):
        # customize the seat map, with A_F and 1-80 columns
        # X = Aisle, S = Storage, F = Free, R = Reserved
        self.row_labels = ['A', 'B', 'C', 'D', 'E', 'F', ]
        self.column_labels = [str(i) for i in range(1, 81)]
        # layout with aisles after every 20 seats for simplicity
        self.seat_map = [['F' if (i + 1) % 20 != 0 else 'X' for i in range(80)] for _ in self.row_labels]
        # define storage areas (rows D, E, and F)
        for row in range(3, 6):
            for col in range(4):
                self.seat_map[row][col] = 'S'  # mark storage areas as 'S'

    def display_seats(self):
        """ display the current seat map. """
        # Print header with column labels
        print("\nCurrent Seat Map:")
        table = [[''] + self.column_labels]  # add empty header for row letters
        for i in range(len(self.seat_map)):
            row = [self.row_labels[i]] + self.seat_map[i]
            table.append(row)
        # display table using tabulate
        print(tabulate(table, headers='firstrow', tablefmt='grid'))
    def check_availability(self):
        """ checks and displays available seats. """
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

    def book_or_free_seat(self, action='book'):
        """ Allows a user to book or free a seat. """
        self.display_seats()  # display current seat map
        row = input("Enter the row (A-F): ").upper()  # get user input for row
        column = input("Enter the seat number (1-80): ")  # get user input for column

        # check if the entered row and column are valid
        if row in self.row_labels and column in self.column_labels:
            row_index = self.row_labels.index(row)
            col_index = self.column_labels.index(column)

            # if user wants to book a seat and the seat is free, book it
            if action == 'book' and self.seat_map[row_index][col_index] == 'F':
                self.seat_map[row_index][col_index] = 'R'
                print("Seat successfully booked!")
            # if user wants to free a seat and the seat is reserved, free it
            elif action == 'free' and self.seat_map[row_index][col_index] == 'R':
                self.seat_map[row_index][col_index] = 'F'
                print("Seat has been freed.")
        else:
            print("Invalid seat selection. Please try again.")  # inform if seat selection is invalid

    # function for running the program
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
            elif choice == '2':
                self.book_or_free_seat(action='book')
            elif choice == '3':
                self.book_or_free_seat(action='free')
            elif choice == '4':
                self.display_seats()
            elif choice == '5':
                print("Exiting the program.")  # inform user of program exiting
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")  # iform if choice is invalid


# run the application
if __name__ == "__main__":
    booking_app = SeatBooking()
    booking_app.run()