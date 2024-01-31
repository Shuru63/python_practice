from datetime import datetime,timedelta
current_datetime=datetime.now()
print("Current Date and Time:", current_datetime)


# Date object
date_obj = datetime.date(datetime(2024, 11, 25))
print("Date Object:", date_obj)

# String to datetime
date_string = "2024-11-25"
formatted_date = datetime.strptime(date_string, "%Y-%m-%d")
print("String to Datetime:", formatted_date)

# Datetime to string
formatted_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Datetime to String:", formatted_string)

# Timedelta
delta = timedelta(days=5, hours=3)
new_date = current_datetime + delta
print("New Date after timedelta:", new_date)