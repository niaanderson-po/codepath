#iterate through dict adding vaues together
def total_sales(ticket_sales):
    sum = 0
    for key in ticket_sales:
        sum += ticket_sales[key]
    return sum

    #or

    sum = 0
    for key in ticket_sales:
        sum += ticket_sales.get(key)
    return sum

    #or

    sum = 0
    for _, values in ticket_sales.items():
        sum += values
    return sum 

    #or

    return sum(ticket_sales.values())

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))