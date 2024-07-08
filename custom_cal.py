import csv
from datetime import datetime, timedelta

#change these parameters to create different calendars
start_date = datetime(year=2023, month=4, day=1)
end_date = datetime(year=2023, month=4, day=15)
calendar_type = '4-4-5'
monthly_offset = 'April'
start_day_of_week = 1
# 1 = Mon


print(int(start_date.strftime('%w')) + start_day_of_week)



print("************* Default Variables ************* \n",
      "Calendar Type:",calendar_type,
      "\n Start day of week: " , start_day_of_week,
      "\n******************************************* ")


def generate_calendar(start_date, end_date, calendar_type=calendar_type, monthly_offset=monthly_offset):
    current_date = start_date
    date_data = []
    week_counter = 0
    starting_week_number = int(start_date.strftime('%W')) -1
    quarter = 1
    starting_week_quarter = 1
    week_number_of_quarter = 1
    print

    while current_date <= end_date:

        # Extract basic date components
        date = current_date.strftime('%Y-%m-%d')
        weekday_name = current_date.strftime('%A')
        day_of_week = current_date.strftime('%w')

        # Calculate the Day of the week
        if start_day_of_week == "Sunday":
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

        month = current_date.strftime('%B')
        is_weekend = 'Yes' if current_date.strftime('%w') in ['0', '6'] else 'No'
        absolute_week_number = current_date.strftime('%W')

        #fixme - this is not calculating corrently because of the starting weekday
        week_number_of_month = (current_date.day - 1) // 7 + 1
        week_number_of_year =int(current_date.strftime('%W')) - int(starting_week_number)
        year = current_date.strftime('%Y')

        # Handle custom calendar types
        if calendar_type == '4-4-5':
            print("\n-----\n")
            print("** Date: ",  date)
            print("** Weekday: ",weekday_name)
            print("** Day of Week: ", day_of_week)

            if week_number_of_year > 38:
                if week_number_of_year == 39:
                    week_number_of_quarter = 1
                quarter = 4

            elif week_number_of_year > 25:
                if week_number_of_year == 26:
                    week_number_of_quarter = 1
                quarter = 3
            elif week_number_of_year > 12:
                if week_number_of_year == 13:
                    week_number_of_quarter = 1
                quarter = 2
            else:
                if week_number_of_year == 1:
                    week_number_of_quarter = 1
                quarter = 1


            # Determine day, month, quarter, year details
            day_number_of_month = current_date.day
            day_number_of_quarter = (current_date - datetime(year=current_date.year, month=(current_date.month - 1) // 3 * 3 + 1, day=1)).days + 1
            day_number_of_year = (current_date - datetime(year=current_date.year, month=1, day=1)).days + 1
            month_number_of_quarter = current_date.month % 3 or 3
            month_number_of_year = current_date.month

            # Determine start and end of week epoch
            start_of_week_epoch = (current_date - timedelta(days=current_date.weekday())).strftime('%Y-%m-%d')
            end_of_week_epoch = (current_date + timedelta(days=6 - current_date.weekday())).strftime('%Y-%m-%d')

            print("** Month: ", month)
            print("** Week of Month: ",week_number_of_month)
            print("** Week of Year: ", week_number_of_year)
            print("** Quarter: ", quarter)
            print("** Week of Quarter: ", week_number_of_quarter)

            week_number_of_quarter += 1


            date_data.append([
                date, weekday_name, day_of_week, month, quarter, year,
                week_number_of_month, week_number_of_quarter,
                week_number_of_year, is_weekend, day_number_of_month, day_number_of_quarter,
                day_number_of_year, month_number_of_quarter, month_number_of_year,
                absolute_week_number, start_of_week_epoch, end_of_week_epoch
            ])

            # while current_date.strftime('%w') != '1':  # Skip until we reach Monday
            current_date += timedelta(days=1)
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
        # if current_date.month == datetime.strptime(monthly_offset, '%B').month:
        #     current_date += timedelta(days=1)

    return date_data

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([
            'date', 'weekday_name', 'day_of_week', 'month', 'quarter', 'year',
            'week_number_of_month', 'week_number_of_quarter',
            'week_number_of_year', 'is_weekend', 'day_number_of_month', 'day_number_of_quarter',
            'day_number_of_year', 'month_number_of_quarter', 'month_number_of_year',
            'absolute_week_number', 'start_of_week_epoch', 'end_of_week_epoch'
        ])
        csv_writer.writerows(data)

def main():

    date_data = generate_calendar(start_date, end_date, calendar_type, monthly_offset)

    filename = f'{calendar_type}_calendar.csv'
    write_to_csv(filename, date_data)

    print(f'CSV file "{filename}" has been created successfully.')

if __name__ == '__main__':
    main()
