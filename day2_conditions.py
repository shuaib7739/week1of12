Mark = int(input("what marks did you get in the exams? "))
if Mark < 0 or Mark > 100:
    print("invalid mark")
elif Mark >= 70:
    print("A,super!!!")
elif Mark >= 60:
    print("B,well done")
elif Mark >= 50:
    print("C,good")
elif Mark >= 40:
    print("D,not bad")
else:
    print("E,better luck next time")
