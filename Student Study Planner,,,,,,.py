# ================================================================
# SIMPLE STUDY PLANNER – NO ADVANCED LIBRARIES
# ================================================================

import time

# Data storage
subjects = []
time_table = {}
daily_goals = []
weekly_goals = []
study_sessions = []
points = 0
streak = 0
badges = []

quotes = [
    "Keep going, you're doing great!",
    "Small progress is still progress.",
    "Believe in yourself!",
    "One hour today is better than none."
]

# ================================================================
# SUBJECTS
# ================================================================

def add_subjects():
    while True:
        name = input("Enter subject name (or 'done'): ").strip()
        if name.lower() == "done":
            break
        if name and name not in subjects:
            subjects.append(name)
            print("Added:", name)
        else:
            print("Invalid or duplicate name.")


def allocate_time():
    if not subjects:
        print("Add subjects first.")
        return
    
    for sub in subjects:
        try:
            hrs = float(input(f"Hours per day for {sub}: ") or 0)
            time_table[sub] = hrs
        except:
            time_table[sub] = 0

    print("Time allocation saved.")

# ================================================================
# TIMETABLE
# ================================================================

def show_daily_table():
    print("\n--- Daily Timetable ---")
    if not time_table:
        print("No time allocated yet.")
        return
    for s, h in time_table.items():
        print(f"{s}: {h}h/day")


def show_weekly_table():
    print("\n--- Weekly Timetable ---")
    if not time_table:
        print("No time allocated yet.")
        return
    for s, h in time_table.items():
        print(f"{s}: {h*7}h/week")

# ================================================================
# GOALS
# ================================================================

def set_goals():
    d = input("Today's goal: ").strip()
    w = input("Weekly goal: ").strip()

    if d:
        daily_goals.append(d)
    if w:
        weekly_goals.append(w)

    print("Goals saved.")


def view_goals():
    print("\nYour Goals:")
    print("\nDaily Goals:")
    print(*daily_goals, sep="\n") if daily_goals else print("None")

    print("\nWeekly Goals:")
    print(*weekly_goals, sep="\n") if weekly_goals else print("None")

# ================================================================
# MOTIVATION + REWARDS
# ================================================================

def motivate():
    import random
    print("\nMotivation:", random.choice(quotes))


def give_rewards():
    global points, streak

    points += 10
    streak += 1

    print("\nYou earned 10 points! 🎉")
    print("Streak:", streak)

    if points >= 50 and "Bronze Badge" not in badges:
        badges.append("Bronze Badge")
        print("Unlocked: Bronze Badge")

    if points >= 150 and "Silver Badge" not in badges:
        badges.append("Silver Badge")
        print("Unlocked: Silver Badge")

# ================================================================
# STUDY SESSION
# ================================================================

def log_session():
    if not subjects:
        print("Add subjects first.")
        return
    
    print("Subjects:", subjects)
    s = input("What did you study? ").strip()
    
    if s not in subjects:
        print("Invalid subject.")
        return

    try:
        hrs = float(input("How many hours? "))
    except:
        print("Invalid input.")
        return

    t = time.strftime("%Y-%m-%d")
    study_sessions.append({"subject": s, "hours": hrs, "date": t})
    print("Session saved.")

def view_history():
    if not study_sessions:
        print("No history yet.")
        return
    
    total = 0
    for i, s in enumerate(study_sessions, 1):
        print(f"{i}. {s['subject']} — {s['hours']}h on {s['date']}")
        total += s['hours']
    print("Total hours studied:", total)

# ================================================================
# DELETE FUNCTIONS
# ================================================================

def delete_subject():
    name = input("Enter subject to delete: ").strip()
    if name in subjects:
        subjects.remove(name)
        time_table.pop(name, None)
        print("Deleted:", name)
    else:
        print("Not found.")


def delete_goal():
    print("1. Delete daily goal")
    print("2. Delete weekly goal")
    choice = input("Choose: ")

    if choice == "1" and daily_goals:
        for i, g in enumerate(daily_goals, 1):
            print(i, g)
        idx = int(input("Delete which? ")) - 1
        if 0 <= idx < len(daily_goals):
            print("Deleted:", daily_goals.pop(idx))

    elif choice == "2" and weekly_goals:
        for i, g in enumerate(weekly_goals, 1):
            print(i, g)
        idx = int(input("Delete which? ")) - 1
        if 0 <= idx < len(weekly_goals):
            print("Deleted:", weekly_goals.pop(idx))

    else:
        print("Nothing to delete.")

# ================================================================
# PERFORMANCE + HABITS
# ================================================================

def predict_performance():
    if len(study_sessions) < 3:
        print("Need at least 3 sessions.")
        return

    avg = sum(s["hours"] for s in study_sessions) / len(study_sessions)

    if avg >= 3:
        print("Estimated grade: A — Excellent!")
    elif avg >= 2:
        print("Estimated grade: B — Good work!")
    elif avg >= 1:
        print("Estimated grade: C — Needs improvement.")
    else:
        print("Estimated grade: D — Study more!")


def classify_habits():
    if not study_sessions:
        print("No sessions yet.")
        return
    
    avg = sum(s["hours"] for s in study_sessions) / len(study_sessions)

    if avg < 1:
        print("Habit Type: Short bursts")
    elif avg > 3:
        print("Habit Type: Deep focus")
    else:
        print("Habit Type: Balanced")

# ================================================================
# MENU + MAIN LOOP
# ================================================================

def menu():
    print("""
==============================
        STUDY PLANNER
==============================
1. Add Subjects
2. Allocate Time
3. Daily Timetable
4. Weekly Timetable
5. Set Goals
6. View Goals
7. Motivation + Rewards
8. Log Study Session
9. View Study History
10. Delete Subject
11. Delete Goal
12. Predict Performance
13. Classify Habits
0. Exit
==============================
""")


def main():
    while True:
        menu()
        choice = input("Choose: ").strip()

        if choice == "1": add_subjects()
        elif choice == "2": allocate_time()
        elif choice == "3": show_daily_table()
        elif choice == "4": show_weekly_table()
        elif choice == "5": set_goals()
        elif choice == "6": view_goals()
        elif choice == "7": motivate(); give_rewards()
        elif choice == "8": log_session()
        elif choice == "9": view_history()
        elif choice == "10": delete_subject()
        elif choice == "11": delete_goal()
        elif choice == "12": predict_performance()
        elif choice == "13": classify_habits()
        elif choice == "0":
            print("Goodbye! Keep studying!")
            break
        else:
            print("Invalid choice.")

# Run program
main()
