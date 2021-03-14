"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee = self.getEmployee(employees, id)
        total = employee.importance
        for uniqueId in employee.subordinates:
            total += self.getImportance(employees, uniqueId)
        return total
    def getEmployee(self, employees: List['Employee'], id: int) -> 'Employee':
        for employee in employees:
            if employee.id == id:
                return employee
        