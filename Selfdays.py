#SayDays.py

class SayDays:
    def __init__(self, year: int,  month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
        
        def is_leap(self):
            y = self.year
            # leap year? February = 29 : not = 28
            # leap year? Year = 366 : not 365
            # using in 2 places -> let's return bool
            return (
                (y % 4 == 0 and y % 100 != 0) or
                (y % 400 == 0)
                )
        
        def days(self):
            #From jan1, how many days until now?
            days_in_month = [
                31, 29 if self.is_leap() else 28, 31, 30, 31, 30, 31, 31,
                30, 31, 30, 31
                
                ] # 31 + 28 = 59 + 31 = 90 + 16 = 116
            
            total = 0
            m = 0
            
            while m < self.month -1:
                total += days_in_month[m]
                m += 1
                
                total += self.day
                return total
            
            def days_left(self) -> int:  
                #until Dec31, how many days left?
            total_days = 366 if self.is_leap() else 365
            return total_days - self.days() # not 16th, but
            

                def weekdays(self):
                    # Use ZELLER's formula to find the day of the week
                    y = self.year
                    m = self.month
                    d = self.day
                    
                    if m < 3:
                        m += 12
                        y -= 1
                        
                    k = y % 100
                    J = y // 100
                    
                    h = (d + (13 * (m + 1)) //
                    5 + K + K // 4 + J // 4 + 5 * J) % 7
                    return h
                    
                    
                    def weekday_name(self): => str:
                        # print english name of the week day
                        names = [
                            "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
                            ]
                        return names[self.weekday()] # 5 -> "Thursday"
            

while True:
    year = int(input("What year is it? "))
    month = int(input("What year is it? "))
    day = int(input("What day is it ? "))
    
    date = SayDays(year, month, day)
    
    print("Days after Jan 1: ", date.days())
    print("Days until Dec 31: ", date.days_left())
    print("Numeric day of the week: ", date.weekday())
    print("English day of the week: ", date.weekday_name())
    