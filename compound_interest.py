#All your base are belong to us!

print("What is your starting balance?")

starting_balance = float(input())
print("How much will you be contributing monthly?")

monthly_contribution = float(input())

print("What is your expected annual rate of return in decimal form?")

expected_interest = float(input())

print("How many years will you be investing?")

time = float(input())

compounded_starting_balance = starting_balance * (1 + (expected_interest / 12)) ** (12 * time)

compounded_monthly_contribution = monthly_contribution * (((1 + expected_interest / 12) ** (12 * time) - 1) / (expected_interest / 12)) * (1 + expected_interest / 12)

future_balance = compounded_starting_balance + compounded_monthly_contribution

print("Your expected future balance is $" + str(int(future_balance)))

input("Press Enter to exit...")
