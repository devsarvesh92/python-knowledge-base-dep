

def get_expenses():
    """
    Get exepenses
    """
    return zip(['JAN','FEB','MAR','APR','MAY'],[2200,2350,2600,2130,2190])

def add_expenses(expenses:list,spent,month):
    expenses.append((month,spent))
    return expenses

def update_expenses(expenses:list,month,amount):
    find_expense = [expense for expense in expenses if expense[0]==month][0]
    expenses.remove(find_expense)
    updated_expense = (find_expense[0],find_expense[1]+amount)
    expenses.append(updated_expense)


def compare_expenses(month_a,month_b,expenses):
    month_a_expense = [expense[1] for expense in expenses if expense[0]==month_a][0]
    month_b_expense = [expense[1] for expense in expenses if expense[0]==month_b][0]

    return month_a_expense - month_b_expense

def expense_in_first_quarter(expenses):
    return sum([expense[1] for expense in expenses[:3]])

def exact_spent_month(spent,expenses):
    return [expense[0] for expense in expenses if expense[1]==spent]

def sort_expense(expenses):
    return sorted(expenses,key=lambda x:x[1],reverse=True)

expenses = list(get_expenses())
print(compare_expenses('JAN','FEB',expenses=expenses))
print(expense_in_first_quarter(expenses))
print(exact_spent_month(2000,expenses=expenses))
print(add_expenses(expenses,2000,'JUN'))
print(update_expenses(expenses,'APR',-200))
print(sort_expense(expenses))