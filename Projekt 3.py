import datetime
birth_date_str = input ("Zadej datum narození ve formátu YYYY-MM-DD:\n")
given_date=datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")
current_date=datetime.datetime.now()
difference = current_date - given_date
formatted_days = f"{difference.days:,}"
print ("Jsi stary " + str(formatted_days) + " dnu")
days_count = difference.days

if (days_count) >=6575:
    print("V CR uz muzes pit")
else:
    print("Jeste nechlastej")
