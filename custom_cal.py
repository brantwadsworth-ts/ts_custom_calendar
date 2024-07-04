import csv
from datetime import datetime, timedelta

#change these parameters to create different calendars
start_date = datetime(year=2023, month=4, day=1)
end_date = datetime(year=2023, month=4, day=30)
calendar_type = '4-4-5'  # Change this to '4-5-4', '5-4-4', or 'custom' as needed
monthly_offset = 'April'
start_day_of_week = "Sunday"



print("************* Default Variables ************* \n",
      "Calendar Type:",calendar_type,
      "\n Start day of week: " , start_day_of_week,
      "\n******************************************* ")


def generate_calendar(start_date, end_date, calendar_type=calendar_type, monthly_offset=monthly_offset):
    current_date = start_date
    date_data = []

    print

    while current_date <= end_date:

        # Extract date components
        date = current_date.strftime('%Y-%m-%d')
        print("\nDate: ", date)
        weekday_name = current_date.strftime('%A')
        print("Weekday: ",weekday_name)
        day_of_week = current_date.strftime('%w')

        # Calcuate the Day of the week
        if start_day_of_week== "Sunday":
            if weekday_name == "Sunday":
                day_of_week = 1
            elif weekday_name == "Monday":
                day_of_week = 2
            elif weekday_name =="Tuesday":
                day_of_week = 3
            elif weekday_name == "Wednesday":
                day_of_week = 4
            elif weekday_name == "Thursday":
                day_of_week = 5
            elif weekday_name =="Friday":
                day_of_week = 6
            else:
                day_of_week = 7

        print("Day of week: ", day_of_week)
        month = current_date.strftime('%B')
        print("Current Date: ", weekday_name +" "+ date)

        # Determine week details
        is_weekend = 'Yes' if current_date.strftime('%w') in ['0', '6'] else 'No'
        # day_number_of_week = current_date.strftime('%w')

        print("\n-----\n")

        # Append data to date_data list
        date_data.append([
            date, weekday_name, day_of_week, month, quarter, year,
            day_number_of_week, week_number_of_month, week_number_of_quarter,
            week_number_of_year, is_weekend, day_number_of_month, day_number_of_quarter,
            day_number_of_year, month_number_of_quarter, month_number_of_year,
            absolute_week_number, start_of_week_epoch, end_of_week_epoch
        ])


        # Handle custom calendar types
        if calendar_type == '4-4-5':

            if current_date.month != end_date.month and current_date.day == 1:

                #Calendar Specific Calculations
                quarter = str((current_date.month - 1) // 3 + 1)
                year = current_date.strftime('%Y')
                week_number_of_month = (current_date.day - 1) // 7 + 1
                week_number_of_quarter = ((current_date.month - 1) * 3 + (current_date.day - 1) // 7) // 3 + 1
                week_number_of_year = current_date.strftime('%U')
                absolute_week_number = current_date.strftime('%W')

                # Determine day, month, quarter, year details
                day_number_of_month = current_date.day
                day_number_of_quarter = (current_date - datetime(year=current_date.year, month=(current_date.month - 1) // 3 * 3 + 1, day=1)).days + 1
                day_number_of_year = (current_date - datetime(year=current_date.year, month=1, day=1)).days + 1
                month_number_of_quarter = current_date.month % 3 or 3
                month_number_of_year = current_date.month

                # Determine start and end of week epoch
                start_of_week_epoch = (current_date - timedelta(days=current_date.weekday())).strftime('%Y-%m-%d')
                end_of_week_epoch = (current_date + timedelta(days=6 - current_date.weekday())).strftime('%Y-%m-%d')`
                while current_date.strftime('%w') != '1':  # Skip until we reach Monday
                    current_date += timedelta(days=1)
                    continue

        elif calendar_type == '4-5-4':
            if current_date.month in [1, 3, 5, 7, 8, 10, 12]:
                if current_date.day == 29:
                    current_date += timedelta(days=3)
            elif current_date.month == 2:
                if current_date.day == 29:
                    current_date += timedelta(days=2)
                elif current_date.day == 28:
                    current_date += timedelta(days=1)
        elif calendar_type == '5-4-4':
            if current_date.month in [1, 3, 5, 7, 8, 10, 12]:
                if current_date.day == 30:
                    current_date += timedelta(days=3)
                elif current_date.day == 31:
                    current_date += timedelta(days=2)
            elif current_date.month == 2:
                if current_date.day == 28:
                    current_date += timedelta(days=3)
                elif current_date.day == 29:
                    current_date += timedelta(days=2)

        # Handle monthly offset
        if current_date.month == datetime.strptime(monthly_offset, '%B').month:
            current_date += timedelta(days=1)

    return date_data

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([
            'Date', 'Weekday Name', 'Day of the Week', 'Month', 'Quarter', 'Year',
            'Day Number of Week', 'Week Number of Month', 'Week Number of Quarter',
            'Week Number of Year', 'Is Weekend', 'Day Number of Month', 'Day Number of Quarter',
            'Day Number of Year', 'Month Number of Quarter', 'Month Number of Year',
            'Absolute Week Number', 'Start of Week Epoch', 'End of Week Epoch'
        ])
        csv_writer.writerows(data)

def main():

    date_data = generate_calendar(start_date, end_date, calendar_type, monthly_offset)

    filename = f'{calendar_type}_calendar.csv'
    write_to_csv(filename, date_data)

    print(f'CSV file "{filename}" has been created successfully.')

if __name__ == '__main__':
    main()
