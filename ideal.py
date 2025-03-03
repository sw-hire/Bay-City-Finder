from filter import findcity


def idealcity():
    print("Alright! Let's get started!")
    budget = int(input("What is your budget for a home ($): "))
    while budget < 453000:
        print ("Sorry! Median house prices as of 2021 start at 453000. Please enter a value at or above 453000.")
        budget = int(input("What is your budget for a home ($): "))

    choice = input("How do you prefer to commute? (Please spell as they are below!)\nYour options are:\nTransit"
                   "\nCarpool\nDrive Alone\nBicycle\nWalk\nWork From Home\nNow enter here as spelled above: ")
    while (choice != "Carpool" and choice != "Drive Alone" and choice != "Bicycle"
           and choice != "Walk" and choice != "Work From Home" and choice != "Transit"):
        print("Looks like there is a spelling error or extra space somewhere! Try copy pasting from the menu we gave you.")
        choice = input("How do you prefer to commute? (Please spell as they are below!)\nYour options are:\nTransit"
                       "\nCarpool\nDrive Alone\nBicycle\nWalk\nWork From Home\nNow enter here as spelled above: ")
    time = float(input("What is your ideal commute time? (minutes): "))
    while time < 17.34:
        print ("Sorry! Average commute times as of 2018 start at 17.34 minutes. Please enter a value at or above 17.34.")
        time = float(input("What is your ideal commute time? (minutes): "))

    pref = input("Please rank your budget, mode of commute, and ideal commute time. Follow the format below:\n"
                 "If budget > mode > time, then enter 'BMT'\n"
                 "Now enter your ranking!: ")
    while (pref != "BMT" and pref != "BTM"
           and pref != "MBT" and pref != "MTB"
           and pref != "TBM" and pref != "TMB"):
        print("Looks like there is a spelling error! Please follow the format with all caps and no spaces!")
        pref = input("Please rank your budget, mode of commute, and ideal commute time. Follow the format below:\n"
                     "If budget > mode > time, then enter 'BMT'\n"
                     "Now enter your ranking!: ")

    findcity(budget, choice, time, pref)
