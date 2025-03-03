from ideal import idealcity

print ("Welcome to the Bay Area City Finder!")
print("-------------------------------------")
print ("Picking the right place to live in the Bay Area is tough—prices are high, commutes are long, and every city is different. This tool makes it easier!\nJust enter your budget, commute preferences, and what matters most to you. \nWe’ll match you with a city that fits your life.")
print("\n")
check = input("Are you ready to find your new city? (Yes/No): ")
while check == 'Yes':
    idealcity()
    check = input("Looking to find another city? (Yes/No): ")

print("Thank you for using Bay Area City Finder")
