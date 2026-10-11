from datetime import datetime


def main():
    print("Raywag8025 Spreadsheet Automation Menu")
    print()
    print("Choose a number from the following options:")
    print()
    print("1. Input Data")
    print("2. View Current Data")
    print("3. Generate Report")
    print()

    # The next line retrieves the inputted option and stores into the variable called selection.
    selection = input("Select an option: ")

    current_time = datetime.now()

    print()
    print(f"You selected option {selection} at {current_time}")


if __name__ == "__main__":
    main()
