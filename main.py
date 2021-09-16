"""
Eemil Soisalo
Juoksulenkkilaskuri
Tampere Uni Hervanta
16.09.2021
"""


def main():
    overallday = int(input("Enter the number of days: "))
    day = int(1)
    mean = float(0)
    zero_counter = float(0)
    loop = True

    while loop:

        for i in range(0, overallday):
            run = float(input(f"Enter day {day} running length: "))
            mean = float(mean + run)
            day = int(day + 1)

            if run == 0:
                zero_counter = float(zero_counter + 1)
                print(zero_counter)

                if zero_counter == 3:
                    print()
                    print("You had too many consecutive lazy days!")
                    break
            else:
                zero_counter = float(0.00)

            if day == overallday:
                loop = False


    average = mean / overallday
    if average > 3.00:
        print()
        print(f"You were persistent runner! With a mean of {average:.2f} km.")
    else:
        print()
        print(f"Your running mean of {average:.2f} km was too low!")


if __name__ == "__main__":
    main()
