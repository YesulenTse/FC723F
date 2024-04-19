from tabulate import tabulate
import random
import string
class SeatBooking:
    def __init__(self):
        # customize the seat map, with A_F and 1-80 columns
        # X = Aisle, S = Storage, F = Free, R = Reserved
        self.row_labels = ['A', 'B', 'C', 'D', 'E', 'F', ]
        self.column_labels = [str(i) for i in range(1, 81)]
        # layout with aisles after every 20 seats for simplicity
        self.seat_map = [['F' if (i + 1) % 20 != 0 else 'X' for i in range(80)] for _ in self.row_labels]
        self.booked_seats = {}  # to store booking references
        self.booking_references = set()
        self.customer_data = {}  # to store customer details
        self.load_data()  # Load data from file when starting the application

        # define storage areas (rows D, E, and F)
        for row in range(3, 6):
            for col in range(4):
                self.seat_map[row][col] = 'S'  # mark storage areas as 'S'

    def generate_booking_reference(self):
        """ generates a unique 8-character alphanumeric booking reference. """
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if reference not in self.booking_references:
                self.booking_references.add(reference)
                return reference

    def save_data(self):
        """Save booking and customer data to a text file."""
        with open("booking_data.txt", "w") as file:
            for ref, details in self.booked_seats.items():
                file.write(f"{details['Booking Reference']},{details['Passport Number']},{details['First Name']},{details['Last Name']},{details['Seat Row']},{details['Seat Column']}\n")
    def load_data(self):
        """Load booking and customer data from a text file."""
        try:
            with open("booking_data.txt", "r") as file:
                for line in file:
                    ref, passport, first_name, last_name, seat_row, seat_column = line.strip().split(',')
                    self.customer_data[ref] = {
                        'passport_number': passport,
                        'first_name': first_name,
                        'last_name': last_name,
                        'seat_row': seat_row,
                        'seat_column': seat_column
                    }
                    row_index = self.row_labels.index(seat_row)
                    col_index = self.column_labels.index(seat_column)
                    self.seat_map[row_index][col_index] = ref
                    self.booking_references.add(ref)  # Add booking reference to the set
        except FileNotFoundError:
            print("No existing booking data found.")

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
                booking_ref = self.generate_booking_reference()
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                passport_number = input("Enter passport number: ")

                # store booking details
                self.booked_seats[(row, column)] = {
                    'Booking Reference': booking_ref,
                    'First Name': first_name,
                    'Last Name': last_name,
                    'Passport Number': passport_number,
                    'Seat Row': row,
                    'Seat Column': column
                }

                self.seat_map[row_index][col_index] = booking_ref  # Place booking reference in the seat
                print("Seat successfully booked!")
                self.save_data()

            # if user wants to free a seat and the seat is reserved, free it
            elif action == 'free' and self.seat_map[row_index][col_index] != 'F' and self.seat_map[row_index][col_index] != 'X' and self.seat_map[row_index][col_index] != 'S':
                print("Booked Seats before freeing:", self.booked_seats)
                booking_ref = self.seat_map[row_index][col_index]
                seat_key = (row, column)
                if seat_key in self.booked_seats and self.booked_seats[seat_key]['Booking Reference'] == booking_ref:
                    del self.booked_seats[seat_key]
                    self.seat_map[row_index][col_index] = 'F'
                    print("Seat has been freed.")
                else:
                    print("No such booking found.")
            else:
                print("Invalid seat selection or action. Please try again.")
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