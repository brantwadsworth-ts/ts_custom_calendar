import csv
import datetime

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Add the custom calendar options here
csv_filename = 'custom_cal.csv'
start_date = "2024-01-01"
end_date = "2024-12-31"
month_offset = 2
week_starting = "Monday"
quarter_prefix = "Q"
year_prefix = "YR"

# Does the starting day of the calendar need to be the starting day of the week?

# Create a new CSV file and open it
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # Add the header row
    date_row = ["date", "day_of_week", "month"]
    writer.writerow(date_row)

    # Calculate the number of rows in the table
    sDate = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    eDate = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    days_delta =  (sDate - eDate).days *-1

    #set the default values
    date = sDate
    fiscaL_month = 1
    quarter = 1


     # fixme move the range back to days_delta
    for i in range(48):
    # for i in range(days_delta):

        day_of_week = date.strftime('%A')
        month_calc = date.month - month_offset
        year = date.year
        print("Month Calc: ", month_calc)
        if month_calc <= 0:
            year = year -1
            fiscaL_month = 12 + month_calc
            if fiscaL_month >= 10:
                quarter = 4
            elif fiscaL_month >= 7:
                quarter = 3
            elif fiscaL_month >= 4:
                quarter = 2
            else:
                quarter = 1
            print("Fiscal Month1: ", fiscaL_month)
        else:
            fiscaL_month =  date.month
            print("Fiscal Month2: ", fiscaL_month)
            quarter = quarter

        #fixme need to calcualte the day number based on the start day of week
        day_number_of_week = date.weekday() +1
        week_number_of_month = ""
        week_number_of_quarter = ""
        week_number_of_year = ""
        is_weekend = ""
        monthly = ""
        quarterly = ""
        day_number_of_month = ""
        day_number_of_quarter = ""
        day_number_of_year = ""
        month_number_of_quarter = ""
        month_number_of_year = ""
        quarter_number_of_year = ""
        absolute_week_number = ""
        start_of_week_epoch = ""
        end_of_week_epoch = ""
        absolute_month_number = ""
        start_of_month_epoch =""
        end_of_month_epoch =""
        absolute_quarter_number = ""
        start_of_quarter_epoch = ""
        end_of_quarter_epoch = ""
        absolute_year_number = ""
        start_of_year_epoch = ""
        end_of_year_epoch = ""


        print(
            "\nDate:", date,
            "\nDay of Week:", day_of_week,
            "\nMonth:", fiscaL_month,
            "\nQuarter:", quarter,
            "\nYear:", year,
            "\nDay Number: ", day_number_of_week
              )

        writer.writerow([
            date,
            day_of_week,
            fiscaL_month,
        ])

        date += datetime.timedelta(days=1)

