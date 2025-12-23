def grade_cal(average):
    if average >= 70:
        return("A,super!!!")
    elif average >= 60:
        return("B,well done")
    elif average >= 50:
        return("C,good")
    elif average >= 40:
        return("D,not bad")
    else:
        return("E,better luck next time")
    
def average_cal(total,count):
    return total/count

total = 0
count = 0
while True:
 mark = (input("enter mark (or q to exiit ) "))
 if mark == "q":
      break
 total += int(mark)
 count += 1

 average = average_cal(total,count)
 grade = grade_cal(average)
 print(f"{average}")
 print(f"{grade}")
       


    