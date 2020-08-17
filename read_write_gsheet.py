import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authentication Information
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("[google_sheet_name]").sheet1

data = sheet.get_all_records() # Get all the info from the sheet
row = sheet.row_values(1) # get values from given row
col = sheet.col_values(1) # get values form given value
cell = sheet.cell(1,2).value # get value from specific cell
cell_ti = sheet.cell(2,5).value # get value of Total income Cell
cell_te = sheet.cell(2,6).value # get value of Total expences Cell
cell_p = sheet.cell(2,7).value # get value of profit Cell
numRows = sheet.row_count  # Get the number of rows in the sheet

def main():
    """
    This function allows the user to either
    read/write from a given point in the
    google spredsheet
    """

    program_run = True

    while program_run:
        item = 1 # Column A
        expense = 2 # Column B
        income = 3 # Column C
        month = 4 # Column D
        row_numbers = {
            "a": 5, # Row of items
            "b": 5, # Row of expences
            "c": 5, # Row of income
            "d": 5, # Row of month
            "e": 0
        }

        error_message = """
        Sorry! I don't seem to be able to carry out the request you gave me, please
        try again and give a valid argument (this program is case sensitive)
        """
        choice_q = """
        Would you like to Look at data options or put some data into your budget?
        [R/W]
        """
        read_q = """
        What information would you like to access?
        Total income[ti]
        Total expences[te]
        Profit[p]
        All[a]
        """
        write_q = "Have you sold or bought an item? [s/b] (q to quit)"
        type = "type 1 to read data, 2 to write data or q to quit: "

        input1 = input(type) # Asks user whether they want to read or write info
        if input1 == "q": # Allows the user to quit at any given time
            program_run = False
        elif input1 == "1": # input chosen 'read'
            while input1 == "1":
                input2 = input(read_q) # Asks user on info regarding reading info
                if input2 == "ti": # Prints total income for the user
                    print("\tYour total income is: " + cell_ti)
                    break
                elif input2 == "te": # Prints total expenses for the user
                    print("\tYour total expences are: " + cell_te)
                    break
                elif input2 == "p": # Prints total profit for user, if Profit
                    if cell_p <= 0: # below 0, user will get 'in debt' message.
                        print("\tYou're currently " + cell_p + " in debt.")
                        break
                    else:
                        print("\tYour total profit is: " + cell_p)
                        break
                elif input2 == "a": # User will get all of the information above
                    print("\tYour total income is: " + cell_ti + '\n' +
                    "\tYour total expences are: " + cell_te + '\n' +
                    "\tYour total profit is: " + cell_p)
                    break
                else:
                    print(error_message)
            else:
                break
        elif input1 == "2": # Input chosen 'write'
            while input1 == "2":
                input3 = input(write_q)
                if input3 == "s": # User sold something
                """
                Here the user is beigns to input the things that
                they sold including some more information that
                will be imputted into the google sheet
                """
                    item_sold = input("What did you sell?: ")
                    sheet.update_cell(row_numbers["a"],item, item_sold)
                    sheet.update_cell(row_numbers["b"],expense, row_numbers['e']) # This 'e'(0) is here since the user didn't actually lose
                    income_price = input("How much did you sell it for?: ")       # any money, it will fill in the cell marked 'expences'
                    sheet.update_cell(row_numbers["c"],income, income_price)      # to 0
                    month_sold = input("In what month did you make the sale?(eg. Aug): ")
                    sheet.update_cell(row_numbers["d"],month, month_sold)
                    if "a" in row_numbers:
                        row_numbers["a"] += 1
                    elif "b" in row_numbers:
                        row_numbers["b"] += 1
                    elif "c" in row_numbers:
                        row_numbers["c"] += 1
                    elif "d" in row_numbers:
                        row_numbers["d"] += 1
                    else:
                        break
                elif input3 == "b": # User bought something
                """
                Here the user is beigns to input the things that
                they have bought and also other information that
                will be imputted into the google sheet
                """
                    item_bought = input("What did you buy?: ")
                    sheet.update_cell(row_numbers["a"],item, item_bought)
                    item_expense = input("How much was the item?: ")
                    sheet.update_cell(row_numbers["b"],expense, item_expense)
                    sheet.update_cell(row_numbers["c"],income, row_numbers['e']) # again 'e' is the value 0 since user isn't making income
                    month_sold = input("In what month did you make the sale?(eg. Aug): ")
                    sheet.update_cell(row_numbers["d"],month, month_sold)
                    if "a" in row_numbers:
                        row_numbers["a"] += 1
                    elif "b" in row_numbers:
                        row_numbers["b"] += 1
                    elif "c" in row_numbers:  # This is still a working part as
                        row_numbers["c"] += 1 # I'm not sure on how to perm
                    elif "d" in row_numbers:  # update a dictionary, it's meant
                        row_numbers["d"] += 1 # to add one to the row in which
                    else:                     # its in which constantly adds more
                        row_numbers["d"] = 1  # data further down on the sheet
                    break
                elif input3 == "q":
                    break
                else:
                    print(error_message)
        else:
            print(error_message)
main()
