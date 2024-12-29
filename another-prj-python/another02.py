from prettytable import prettytable

def genrate_math_table(rule,start,end):
    """ generate a mathematical table based on a given rule.

    parameters:
    -rule :A callable that defines the matimatical rule(e.g., lambda x:x**2 for squares).
    -start:the starting number for the table.
    -end: the ending number for the table .
    """
    table=prettytable()
    table.field_names=["Number","Result"]


    for i in range(start,end+1):
        table.add_row([i,rule(i)])

    return table
# example usage 
if __name__=="__main__":
    print("choose a mathematical rule:")
    print("1.square of a number")
    print("2.cube of a number")
    print("3.Double of a number.")

    choice=int(input("enter your choice (1/2/3):"))
    if choice ==1:
        rule= lambda x:x**2
    elif choice==2:
        rule= lambda x:x**3
    elif choice==3:
        rule=lambda x:x*2
    else:
        print("Invalid choice. defaulitng to square of a number.")
        rule= lambda x:x**2

    start=int(input("enter the starting number:"))
    end=int(input("enter the ending number:"))

    table=genrate_math_table(rule,start,end)
    print(table)