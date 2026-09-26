from datetime import datetime


# function to get current date and time in (ss:mm:hh , day/month/year) format
def get_current_datetime():
    # get current date and time
    current_datetime = datetime.now()

    # convert current date and time to (ss:mm:hh , day/month/year)
    ssmmhhdmy = current_datetime.strftime("(%S:%M:%H, %d/%m/%Y)")

    return ssmmhhdmy


# function to get fibonacci series based on current minute
def get_fibonacci_series():
    # get current minute
    current_minute = datetime.now().minute

    # get total fibonacci number count
    fibonacci_number_count = current_minute * 2

    # generate fibonacci series
    fibonacci_series = []
    for i in range(fibonacci_number_count):
        if i == 0:
            fibonacci_series.append(0)
        elif i == 1:
            fibonacci_series.append(1)
        else:
            fibonacci_series.append(
                fibonacci_series[i - 1] + fibonacci_series[i - 2])

    return fibonacci_series


print(get_current_datetime())
print(get_fibonacci_series())
