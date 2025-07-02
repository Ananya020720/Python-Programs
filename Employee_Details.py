employee_details =[]
num = int(input("Enter the number of Employees: "))

for i in range(1,num+1):
  temp = {}
  print(f"Enter Employee {i} Details")
  temp["id"] = int(input("Enter Employee ID: "))
  temp["name"] = input("Enter Employee Name: ")
  temp["age"] = int(input("Enter Employee Age: "))
  temp["dept"] = input("Enter Department: ")
  temp["salary"] = int(input("Enter Salary: "))
  employee_details.append(temp)

print("\n--- Employee Details ---")
print(f"{'ID':<10} {'NAME':<15} {'AGE':<5} {'DEPARTMENT':<15} {'SALARY':<10}")
print("-" * 60)

for emp in employee_details:
    print(f"{emp['id']:<10} {emp['name']:<15} {emp['age']:<5} {emp['dept']:<15} {emp['salary']:<10.2f}")
