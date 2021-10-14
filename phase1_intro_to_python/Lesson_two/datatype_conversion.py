# Type and Type Conversion
# You have seen four data types so far: int float bool string
# You got a quick look at type() from an earlier video, and 
# it can be used to check the data type of any variable you are working with.

print(type(633))
# int
print(type(633.0))
# float
print(type('633'))
# str
print(type(True))
# bool

#Total Sales
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

sales_sum = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print("This week's total sales: " + str(sales_sum))
