import matplotlib.pyplot as plt
import random

subjects = []
time_allocation = {}     # daily hours
daily_goals = []
weekly_goals = []
points = 0
streak = 0
quotes = [
    "I can do it!",
    "I believe in myself — I can do this!",
    "I will study today to rest tomorrow"
]
badges = []


def add_subjects():
    print("<<<< Add Subjects >>>>")
    while True:
        s = input("Enter the subject name (or 'done' to stop): ")
        if s.lower() == "done":
            break
        subjects.append(s)
        print("Added:", s)


def allocate_time():
    print("**** Time Allocation ****")
    for s in subjects:
        hrs = int(input(f"Hours to spend on {s} per day: "))
        time_allocation[s] = hrs
    print("**** Time allocation completed. ****")


def daily_timetable():
    print("--- Daily Timetable ---")
    for s, t in time_allocation.items():
        print(f"{s}: {t} hours/day")


def weekly_timetable():
    print("*** Weekly Timetable ***")
    for s, t in time_allocation.items():
        print(f"{s}: {t * 7} hours/week")


def set_goals():
    print("<--- Set Goals --->")
    daily = input("Enter today's goal: ")
    weekly = input("Enter weekly goal: ")

    daily_goals.append(daily)
    weekly_goals.append(weekly)


def show_goals():
    print("--- Your Goals ---")
    print("Daily Goals:")
    for g in daily_goals:
        print("-", g)

    print("Weekly Goals:")
    for g in weekly_goals:
        print("-", g)


def motivational_quote():
    print("\nMotivation Boost →", random.choice(quotes))


def give_rewards():
    global points, streak
    points += 10
    streak += 1

    print("\n🎉 You earned 10 points!")
    print("🔥 Streak:", streak)

    if points >= 50 and "Bronze Student" not in badges:
        badges.append("Bronze Student")
        print("🏅 You unlocked badge: Bronze Student")

    if points >= 150 and "Silver Learner" not in badges:
        badges.append("Silver Learner")
        print("🏅 You unlocked badge: Silver Learner")


def show_weekly_time_graph():
    print("\nShowing time spent per subject per week graph...")

    if not time_allocation:
        print("No subjects or time allocation added yet!")
        return

    subjects_list = list(time_allocation.keys())
    weekly_hours = [t * 7 for t in time_allocation.values()]  # weekly hours

    plt.plot(subjects_list, weekly_hours, marker="o")
    plt.title("Time Spent per Subject (Weekly)")
    plt.xlabel("Subjects")
    plt.ylabel("Hours per Week")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def show_menu():
    print("\n========== STUDY PLANNER ==========")
    print("1. Add Subjects")
    print("2. Allocate Time")
    print("3. Daily Timetable")
    print("4. Weekly Timetable")
    print("5. Set Goals")
    print("6. View Goals")
    print("7. Motivational Quote (Earn Rewards)")
    print("8. Show Rewards / Badges")
    print("9. Weekly Time Spent Graph")
    print("0. Exit")
    print("==================================")


while True:
    show_menu()
    choice = input("💡 What do you want to do next? Enter your option number: ")

    if choice == "1":
        add_subjects()
    elif choice == "2":
        allocate_time()
    elif choice == "3":
        daily_timetable()
    elif choice == "4":
        weekly_timetable()
    elif choice == "5":
        set_goals()
    elif choice == "6":
        show_goals()
    elif choice == "7":
        motivational_quote()
        give_rewards()
    elif choice == "8":
        print("Points:", points)
        print("Badges:", badges)
    elif choice == "9":
        show_weekly_time_graph()
    elif choice == "0":
        print("Goodbye! Keep studying 😊")
        break
    else:
        print("Invalid choice.")

