emp_no = int(input())

worked_hours = int(input())

receives_per_worked_hour = float(input())

# complete
salary = receives_per_worked_hour * worked_hours

print(f"NUMBER = {emp_no}")
print(f"SALARY = U$ {salary:.2f}")

# print("NUMBER =",emp_no,end="\n")
# print("SALARY = U$ %0.2f"%salary,end="\n")