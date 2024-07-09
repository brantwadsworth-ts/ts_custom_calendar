import csv
from datetime import datetime, timedelta
import calendar

#change these parameters to create different calendars
start_date = datetime(year=2023, month=1, day=29)
end_date = datetime(year=2024, month=2, day=28)



calendar_type = '4-4-5'


# Sunday = 1, Monday =2
start_day_of_week = 1


def generate_calendar(start_date, end_date, calendar_type=calendar_type):
    current_date = start_date

    last_year_date = start_date - timedelta(days=1)
    last_year = last_year_date.strftime('%Y')

    date_data = []
    week_of_year = 0
    week_of_quarter = 0
    week_of_month = 0
    quarter = 1
    year = int(last_year) +1
    day_number_of_month = current_date.day
    day_number_of_quarter = 0
    day_number_of_year = 0

    while current_date <= end_date:
        date = current_date.strftime('%Y-%m-%d')
        day_number_of_quarter +=1
        day_number_of_year +=1

        # Make day of week and start of week adjustments
        weekday_name = current_date.strftime('%A')

        # Get the weekday number (Monday is 0 and Sunday is 6)
        weekday_number = current_date.weekday()

        # Adjust the weekday number for Sunday Start: weekday = 0
        if start_day_of_week == 1:
            if weekday_number == 6:
                adjusted_weekday_number = 1
                week_of_year +=1
                week_of_quarter  += 1
                week_of_month +=1
                month = current_date.strftime('%B')

            elif weekday_number == 0:
                adjusted_weekday_number = 2
            else:
                adjusted_weekday_number +=1

        # Adjust the weekday number for Monday Start:  weekday = 1
        elif start_day_of_week ==2:
            if weekday_number == 1:
                week_of_year +=1
                week_of_quarter  +=1
                week_of_month +=1
                month = current_date.strftime('%B')

        # Calculate the quarter and week of quarter. All Calendars have 4 quarters with 13 weeks
        if week_of_year == 53:
            quarter = 1
            week_of_year =1
            day_number_of_year = 0
            week_of_quarter = 1
            week_of_month = 1
            year +=1
        elif week_of_year == 40:
            quarter = 4
            week_of_quarter = 1
            week_of_month = 1
            day_number_of_quarter =1
        elif week_of_year == 27:
            quarter = 3
            week_of_quarter = 1
            week_of_month = 1
            day_number_of_quarter =1
        elif week_of_year == 14:
            quarter = 2
            week_of_quarter = 1
            week_of_month = 1
            day_number_of_quarter =1

        # Calculate the week of month by calendar type
        if week_of_quarter == 9:
            week_of_month = 1
        elif week_of_quarter == 5 :
            week_of_month = 1



        is_weekend = 'Yes' if current_date.strftime('%w') in ['0', '6'] else 'No'
        absolute_week_number = current_date.strftime('%W')


        # year = current_date.strftime('%Y')

        # Handle custom calendar types
        if calendar_type == '4-4-5':
            # Determine day, month, quarter, year details

            day_number_of_year = (current_date - datetime(year=current_date.year, month=1, day=1)).days + 1
            month_number_of_quarter = current_date.month % 3 or 3
            month_number_of_year = current_date.month

            # Determine start and end of week epoch
            start_of_week_epoch = (current_date - timedelta(days=current_date.weekday())).strftime('%Y-%m-%d')
            end_of_week_epoch = (current_date + timedelta(days=6 - current_date.weekday())).strftime('%Y-%m-%d')


            if adjusted_weekday_number == 1:
                date_data.append([
                    date, weekday_name, adjusted_weekday_number, month, quarter, year,
                    week_of_month, week_of_quarter,
                    week_of_year, is_weekend, day_number_of_month, day_number_of_quarter,
                    day_number_of_year, month_number_of_quarter, month_number_of_year,
                    absolute_week_number, start_of_week_epoch, end_of_week_epoch
                ])
            # date_data.append([
            #     increment,date, weekday_name, adjusted_weekday_number, month, quarter, year,
            #     week_of_month, week_of_quarter,
            #     week_of_year, is_weekend, day_number_of_month, day_number_of_quarter,
            #     day_number_of_year, month_number_of_quarter, month_number_of_year,
            #     absolute_week_number, start_of_week_epoch, end_of_week_epoch
            # ])
            current_date += timedelta(days=1)

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

    date_data = generate_calendar(start_date, end_date, calendar_type)

    filename = f'{calendar_type}_calendar.csv'
    write_to_csv(filename, date_data)

    print(f'CSV file "{filename}" has been created successfully.')

if __name__ == '__main__':
    main()
