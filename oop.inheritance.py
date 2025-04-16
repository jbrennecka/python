'''
Name: Jesse Brennecka
Object Oriented Programming, inheritance

Notes:
    -Commented out lines are for testing purposes, it was to ensure that the program was changing the variables.
'''
class Employee():
    def __init__(self, employeeName=None, employeeNum=None):
        self.employeeName = employeeName
        self.employeeNum = employeeNum
        pass
    def setName(self, inputName):
        #oldName = self.employeeName
        self.employeeName = inputName
        #print(f"name changed {self.employeeName}, from {oldName}.")
        pass
    def setNum(self, inputNum):
        #oldNum = self.employeeNum
        self.employeeNum = inputNum
        #print(f"Number changed {self.employeeNum}, from {oldNum}.")
        pass
class ProductionWorker(Employee):
    def __init__(self, shiftNum, payPerHr):
        super().__init__()
        self.shiftNum = shiftNum
        self.payPerHr = payPerHr
        pass
    def setShift(self, inputShift):
        #oldShift = self.shiftNum
        self.shiftNum = inputShift
        #print(f"Shift changed {self.shiftNum}, from {oldShift}.")
        pass
    def setPay(self, inputPay):
        #oldPay = self.payPerHr
        self.payPerHr = inputPay
        #print(f"Pay changed {self.payPerHr}, from {oldPay}.")
        pass
    def printData(self):
        print(f"\n\t\tDETAILS OF EMPLOYEE\nName: {self.employeeName}\nNumber: {self.employeeNum}\nShift: {self.shiftNum}\nPay Rate: {self.payPerHr}")
    pass
obj = ProductionWorker('n', 'n')
obj.setName(input("Please enter the employee's name:\n"))
obj.setNum(input("Please enter the employee's number:\n"))
obj.setShift(input("Please enter the employee's shift:\n"))
obj.setPay(input("Please enter the employee's rate of pay:\n"))
obj.printData()