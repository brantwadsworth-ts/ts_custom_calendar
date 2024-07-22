import csv
from datetime import datetime, timedelta
import calendar


#change these parameters to create different calendars
fiscal_start_date = datetime(year=2023, month=2, day=1)
fiscal_end_date = datetime(year=2025, month=3, day=31)
calendar_type = ''
quarter_prefix = "Q"
fiscal_year_prefix = "YR"

year = int(fiscal_start_date.strftime('%Y'))
first_day_of_year = datetime(fiscal_start_date.year, 1, 1)

# leap_week_year = 5
# leap_week_quarter = 4

# Sunday = 1, Monday =2
start_day_of_week = 2

def generate_calendar(fiscal_start_date, fiscal_end_date, calendar_type=calendar_type,year = year):
    date_data = []
    current_date = fiscal_start_date

    if calendar_type == "445":
        m1 = 5
        m2 = 9
        m3 = 14
    elif calendar_type == '454':
        m1 = 5
        m2 = 10
        m3 = 14
    elif calendar_type == '544':
        m1 = 6
        m2 = 11
        m3 = 14

    if current_date > first_day_of_year:
        year = year +1

    quarter = 1
    adjusted_weekday_number = 1
    day_number_of_month = 0
    day_number_of_quarter = 0
    day_number_of_year = 0
    week_of_month = 0
    week_of_quarter = 0
    week_of_year = 0
    month_number_of_quarter = 1
    month_number_of_year = 1
    increment = 0
    quarter_weeks = 13

    while current_date <= fiscal_end_date:

        # Get the day details
        date = current_date.strftime('%Y-%m-%d')

        # Get the Standard Calendar Week number
        absolute_week_number = current_date.strftime('%W')

        # Get the weekday name
        weekday_name = current_date.strftime('%A')

        #Is weekend?
        is_weekend = 'Yes' if current_date.strftime('%w') in ['0', '6'] else 'No'

        # Get the Original Weekday Number 0: Monday - 6 Sunday
        weekday_number = current_date.weekday()

        if start_day_of_week == 1:  #Sunday

            # Daily Calculations
            day_number_of_month +=1
            day_number_of_quarter += 1
            day_number_of_year += 1

            if weekday_number == 6: #Default Value of Sunday
                adjusted_weekday_number = 1  #set Sunday to 1
                start_of_week_epoch = current_date.strftime('%Y-%m-%d')
                end_of_week_epoch = (current_date + timedelta(days=6 - current_date.weekday())).strftime('%Y-%m-%d')

                # todo Turn this into a function that can be called

                if calendar_type != "":
                    # Calculate Weekly changes
                    if week_of_year <53 and weekday_number == 6:
                        week_of_year +=1
                        week_of_quarter += 1
                        week_of_month +=1

                        # Calculate the Quarter
                        if week_of_quarter <= 13:

                            # Calculate the weeks of the month
                            if week_of_quarter == m1: #end of month 1
                                day_number_of_month =1
                                week_of_month = 1
                                month_number_of_quarter = 2
                                month_number_of_year += 1
                                month = current_date.strftime('%B')

                            elif week_of_quarter == m2: # end of month 2
                                day_number_of_month =1
                                week_of_month = 1
                                month_number_of_quarter = 3
                                month_number_of_year += 1
                                month = current_date.strftime('%B')

                            elif week_of_quarter == m3: #end of month3 & start of new quarter
                                quarter +=1 #new quarter and Month
                                day_number_of_month =1
                                week_of_month = 1
                                month_number_of_quarter = 1
                                month_number_of_year += 1
                                month = current_date.strftime('%B')


                            elif week_of_quarter == 1:
                                month = current_date.strftime('%B')

                        else:
                            quarter +=1
                            month_number_of_quarter = 1
                            week_of_quarter = 1
                            week_of_month = 1
                            day_number_of_month =1
                            day_number_of_quarter = 1
                            month = current_date.strftime('%B')

                    elif weekday_number == 6:
                        week_of_year = 1
                        year +=1

                else:
                    day_number_of_month +=1
                    day_number_of_quarter += 1
                    day_number_of_year += 1

            else:
                adjusted_weekday_number = weekday_number +2

        else: # Start of week is Monday
            adjusted_weekday_number = weekday_number +1
            start_of_week_epoch = current_date.strftime('%Y-%m-%d')
            end_of_week_epoch = (current_date + timedelta(days=6 - current_date.weekday())).strftime('%Y-%m-%d')
            month = current_date.strftime('%B')

        quarter_fiscal = quarter_prefix + str(quarter)
        year_fiscal = fiscal_year_prefix + str(year)


        # if (adjusted_weekday_number == 1 or adjusted_weekday_number == 7): # For testing
        #     date_data.append([
        #         date, weekday_name, adjusted_weekday_number, month, quarter_fiscal, year_fiscal,
        #         week_of_month, week_of_quarter,
        #         week_of_year, is_weekend, day_number_of_month, day_number_of_quarter,
        #         day_number_of_year, month_number_of_quarter, month_number_of_year,
        #         absolute_week_number, start_of_week_epoch, end_of_week_epoch
        #     ])
        #
        # increment +=1
        #
        date_data.append([
            date, weekday_name, adjusted_weekday_number, month, quarter_fiscal, year_fiscal,
            week_of_month, week_of_quarter,
            week_of_year, is_weekend, day_number_of_month, day_number_of_quarter,
            day_number_of_year, month_number_of_quarter, month_number_of_year,
            absolute_week_number, start_of_week_epoch, end_of_week_epoch
        ])

        #get the next day
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

    date_data = generate_calendar(fiscal_start_date, fiscal_end_date, calendar_type)

    filename = f'{calendar_type}_calendar.csv'
    write_to_csv(filename, date_data)

    print(f'CSV file "{filename}" has been created successfully.')

if __name__ == '__main__':
    main()
