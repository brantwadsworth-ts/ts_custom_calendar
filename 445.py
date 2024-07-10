import pandas as pd
import datetime as dt

def create_445_calender(start_date: str, years: int, leap_week_year = 5, leap_week_quarter = 4):

    date_data = []
    tmp_datetime = dt.datetime.strptime(start_date,'%d/%m/%Y')

    for year in range(1,years+1):
        month_of_year = 1
        week_of_year = 1
        # 4 quarters
        for quarters in range(1,5):
            # 4 weeks
            for weeks in range(1,5):
                # 7 days
                for days in range(1,8):
                    tmp_datestr = dt.datetime.strftime(tmp_datetime,'%d/%m/%Y')
                    tmp_weekday = dt.datetime.strftime(tmp_datetime,'%A')
                    tmp_monthstr = str(month_of_year) if month_of_year >=  10 else '0' + str(month_of_year)
                    tmp_yyyy_mm = dt.datetime.strftime(tmp_datetime,'%Y') + '-' + tmp_monthstr
                    tmp_quarter = 'Q' + str(quarters) + ' ' + dt.datetime.strftime(tmp_datetime,'%Y')

                    date_data.append([tmp_datestr,tmp_weekday, week_of_year, tmp_yyyy_mm, tmp_quarter])
                    tmp_datetime = tmp_datetime + dt.timedelta(days=1)
                week_of_year += 1
            month_of_year += 1
            # 4 weeks
            for weeks in range(1,5):
                # 7 days
                for days in range(1,8):
                    tmp_datestr = dt.datetime.strftime(tmp_datetime,'%d/%m/%Y')
                    tmp_weekday = dt.datetime.strftime(tmp_datetime,'%A')
                    tmp_monthstr = str(month_of_year) if month_of_year >=  10 else '0' + str(month_of_year)
                    tmp_yyyy_mm = dt.datetime.strftime(tmp_datetime,'%Y') + '-' + tmp_monthstr
                    tmp_quarter = 'Q' + str(quarters) + ' ' + dt.datetime.strftime(tmp_datetime,'%Y')

                    date_data.append([tmp_datestr,tmp_weekday, week_of_year, tmp_yyyy_mm, tmp_quarter])
                    tmp_datetime = tmp_datetime + dt.timedelta(days=1)
                week_of_year += 1
            month_of_year += 1
            # 5 / 6 weeks
            # 5 years
            if (year % leap_week_year == 0 ) and (quarters == leap_week_quarter):
                tmp_weeks = 6
            else:
                tmp_weeks = 5
            for weeks in range(1,tmp_weeks+1):
                # 7 days
                for days in range(1,8):
                    tmp_datestr = dt.datetime.strftime(tmp_datetime,'%d/%m/%Y')
                    tmp_weekday = dt.datetime.strftime(tmp_datetime,'%A')
                    tmp_monthstr = str(month_of_year) if month_of_year >=  10 else '0' + str(month_of_year)
                    tmp_yyyy_mm = dt.datetime.strftime(tmp_datetime,'%Y') + '-' + tmp_monthstr
                    tmp_quarter = 'Q' + str(quarters) + ' ' + dt.datetime.strftime(tmp_datetime,'%Y')

                    date_data.append([tmp_datestr,tmp_weekday, week_of_year, tmp_yyyy_mm, tmp_quarter])
                    tmp_datetime = tmp_datetime + dt.timedelta(days=1)
                week_of_year += 1
            month_of_year += 1

    return date_data


# my445calender = create_445_calender('06/04/2020', 6, 5, 4)
def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([
            'date','day','week_no','yyyy-mm','quarter'
            # 'date', 'weekday_name', 'day_of_week', 'month', 'quarter', 'year',
            # 'week_number_of_month', 'week_number_of_quarter',
            # 'week_number_of_year', 'is_weekend', 'day_number_of_month', 'day_number_of_quarter',
            # 'day_number_of_year', 'month_number_of_quarter', 'month_number_of_year',
            # 'absolute_week_number', 'start_of_week_epoch', 'end_of_week_epoch'
        ])
        csv_writer.writerows(data)

def main():

    date_data = create_445_calender('06/04/2020', 6, 5, 4)
    filename = f'new-calendar.csv'
    write_to_csv(filename, date_data)

    print(f'CSV file "{filename}" has been created successfully.')

if __name__ == '__main__':
    main()