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
name = input("Name: ")
while True:
    mark = input("enter mark (or q to exit) ")

    if mark == "q":
        break

    try:
        mark = int(mark)

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
            continue

        total += mark
        count += 1

    except ValueError:
        print("Please enter a valid number.")
        continue

average = average_cal(total,count)
grade = grade_cal(average)
print("\nResults")
print(f"{name}")
print(f"{average}")
print(f"{grade}")
       


    