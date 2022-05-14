percentage = int(input("Enter The Student Percentage % Marks:- "))
if 80 <= percentage <= 100:
    print("Excellent Percentage")
elif 70 <= percentage <= 79:
    print("Good Percentage")
elif 50 <= percentage <= 69:
    print("Average Percentage")
elif 33 <= percentage <= 49:
    print("Low Percentage")
elif percentage > 100:
    print("Invalid Percentage")
else:
    print("Fail Percentage")
