#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      samch
#
# Created:     11/07/2025
# Copyright:   (c) samch 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def get_user_info():
    print("Welcome to Smart Health Recommender!")
    name = input("Enter your name: ")
    age = int (input("Enter your age: "))
    weight = float(input("Enter your weight(kg): "))
    height = float(input("Enter your height(cm): "))
    goal = input("Health goal (e.g. stay healthy, lose weight): ")
    water = float(input("How much water did you drink today(liters): "))
    sleep = float(input("How many hours did you sleep last night: "))

    return{
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "goal": goal,
        "water": water,
        "sleep": sleep
    }

def calculate_bmi(weight,height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi,2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def give_badges(water,sleep):
    badges = []
    if water >= 2:
        badges.append("💧 Water Drinker Badge")
    if sleep >= 7:
        badges.append("😴 Sleep Master Badge")
    return badges

def recommend_schedule(goal):
    if goal.lower() == "lose weight":
        return [
            "8.00 AM - 30 min exercise",
            "12:00 PM - Light health lunch",
            "6.00 PM - Evening walk"
        ]
    else:
        return [
            "8.00 AM - Morning stretching",
            "1.00 PM - Balanced meal",
            "10.00 PM - Sleep"
        ]

def main():
    user = get_user_info()

    bmi = calculate_bmi(user["weight"], user["height"])
    category = interpret_bmi(bmi)
    print(f"\nYour BMI is {bmi} ({category}")

    badges = give_badges(user["water"], user["sleep"])
    print("\n🎯 You earned the following badge(s): ")
    if badges:
        for badge in badges:
            print(" -", badge)
        else:
            print("No badges yet, keep going!")

    schedule = recommend_schedule(user["goal"])
    print("\n🗓  Your Recommended Daily Schedule:")
    for task in schedule:
        print(" -", task)


if __name__ == "__main__":
    main()