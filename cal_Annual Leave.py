from datetime import datetime

class AnnualLeaveCalculator:
    def __init__(self, initial_leave_count=0, accrual_day=27, accrual_start_date_str="24-01-01"):
        self.initial_leave_count = initial_leave_count-1
        self.accrual_day = accrual_day
        self.accrual_start_date = datetime.strptime(accrual_start_date_str, '%y-%m-%d')
        self.used_leaves = []

    def add_used_leave(self, date_str, leave_amount):
        date = datetime.strptime(date_str, '%y-%m-%d')
        self.used_leaves.append((date, leave_amount))

    def calculate_accrued_leaves(self, check_date):
        accrued_leaves = 0
        current_date = self.accrual_start_date.replace(day=self.accrual_day)
        
        while current_date <= check_date:
            accrued_leaves += 1
        
            if current_date.month == 12:
                current_date = current_date.replace(year=current_date.year + 1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + 1)
        
        return accrued_leaves

    def get_remaining_leaves(self, check_date_str):
        check_date = datetime.strptime(check_date_str, '%y-%m-%d')
        
        total_accrued_leaves = self.initial_leave_count + self.calculate_accrued_leaves(check_date)
        
        total_used_leaves = sum(leave_amount for date, leave_amount in self.used_leaves if date <= check_date)
        
        remaining_leaves = total_accrued_leaves - total_used_leaves
        return remaining_leaves
    

leave_calculator = AnnualLeaveCalculator(accrual_day=27, accrual_start_date_str="24-05-27")

# yy-mm-dd
leave_schedule = [
    ('24-08-09', 0.5),
    ('24-10-23', 0.5),
    ('24-11-08', 0.5),
    ('24-11-15', 0.5),
    ('24-11-20', 1.0),
    ('24-11-26', 1.0),
    ('24-12-01', 1.0),
    ('25-01-27', 1.0)
]

for leaves in leave_schedule:
    leave_calculator.add_used_leave(*leaves)

date_to_check = ['24-11-24', '24-11-26', '24-12-10', '24-12-27', '25-1-26', '25-1-27']
for date in date_to_check:
    remaining_leaves = leave_calculator.get_remaining_leaves(date)
    print(f'{date} 기준 잔여 연차: {remaining_leaves} 개')
