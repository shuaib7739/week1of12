total = 0
count = 0

while True:
    print("\nmenu")
    print("1.enter mark")
    print("2.calculate average")
    print("3.exit")

    choice = input("choose an option ")

    if choice == "1":
        mark = int(input("enter your marks "))
        if mark<0 or mark>100:
            print("invalid mark")
        else:
            total += mark
            count += 1
    elif choice == "2":
        average = total/count
        if count == 0:
            print("no marks entered")
        else:
            print(f"{average}")
    elif choice == "3":
        print("bye bye")
        break
    else:
        print("invalid choice")
