def calculatePay(rate,holidayPay,hoursWorked,unpaidBreak):
    hoursUnpaidBreaks = unpaidBreak / 60
    totalHours = (hoursWorked - hoursUnpaidBreaks)
    holidayPayCal = (rate + holidayPay)
    pay = (holidayPayCal * totalHours)
    return pay

hoursWorked = input('How many hours did you work today: ')
hoursWorked = int(hoursWorked)

rate = input('How much is the hourly rate: ')
rate = float(rate)

holidayPay = input('How much is the holiday pay: ')
holidayPay = float(holidayPay)

unpaidBreak = input('How long will the break be: \
Please give your answer in minutes: ')
unpaidBreak = float(unpaidBreak)

salary = calculatePay(rate,holidayPay,hoursWorked,unpaidBreak)

print('For this shift you will be paid:', round(salary,2), 'pounds', 'spend wisely!!!')