import matplotlib.pyplot as plt
import random
import datetime
import logging
import numpy as np
from collections import defaultdict

# ========== LOGGING SETUP ==========
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='study_planner.log',
    filemode='a'
)

def log_activity(action, details=""):
    """Log user activities for monitoring"""
    log_message = f"User {action}"
    if details:
        log_message += f" - {details}"
    logging.info(log_message)
    print(f"📝 Activity logged: {action}")

# Global variables
subjects = []
time_allocation = {}
daily_goals = []
weekly_goals = []
points = 0
streak = 0
study_sessions = []
quotes = [
    "I can do it!",
    "I believe in myself — I can do this!",
    "I will study today to rest tomorrow"
]
badges = []

def add_subjects():
    print("<<<< Add Subjects >>>>")
    while True:
        s = input("Enter the subject name (or 'done' to stop): ").strip()
        if s.lower() == "done":
            break
        if s:
            if s in subjects:
                print(f"Subject '{s}' already exists!")
            else:
                subjects.append(s)
                print("Added:", s)
                log_activity("added subject", f"'{s}'")
        else:
            print("Please enter a valid subject name.")

def allocate_time():
    print("**** Time Allocation ****")
    if not subjects:
        print("No subjects added! Please add subjects first.")
        return
        
    for s in subjects:
        try:
            hrs_input = input(f"Hours to spend on {s} per day: ").strip()
            if not hrs_input:  # Handle empty input
                print("No input provided. Setting to 0 hours.")
                time_allocation[s] = 0
                continue
                
            hrs = float(hrs_input)
            if hrs < 0:
                print("Hours cannot be negative. Setting to 0.")
                hrs = 0
            time_allocation[s] = hrs
        except ValueError:
            print("Invalid input! Please enter a number. Setting to 0 hours.")
            time_allocation[s] = 0
    
    log_activity("allocated study time", f"for {len(subjects)} subjects")
    print("**** Time allocation completed. ****")

def daily_timetable():
    print("--- Daily Timetable ---")
    if not time_allocation:
        print("No time allocation set! Please allocate time first.")
        return
    for s, t in time_allocation.items():
        print(f"{s}: {t} hours/day")

def weekly_timetable():
    print("*** Weekly Timetable ***")
    if not time_allocation:
        print("No time allocation set! Please allocate time first.")
        return
    for s, t in time_allocation.items():
        print(f"{s}: {t * 7} hours/week")

def set_goals():
    print("<--- Set Goals --->")
    daily = input("Enter today's goal: ").strip()
    weekly = input("Enter weekly goal: ").strip()

    if daily:
        daily_goals.append(daily)
    if weekly:
        weekly_goals.append(weekly)
    
    if daily or weekly:
        log_activity("set goals", f"Daily: '{daily[:20]}...', Weekly: '{weekly[:20]}...'")
        print("Goals set successfully!")
    else:
        print("No goals were set.")

def show_goals():
    print("--- Your Goals ---")
    if not daily_goals and not weekly_goals:
        print("No goals set yet!")
        return
        
    print("Daily Goals:")
    if daily_goals:
        for i, g in enumerate(daily_goals, 1):
            print(f"{i}. {g}")
    else:
        print("- No daily goals set")
    
    print("\nWeekly Goals:")
    if weekly_goals:
        for i, g in enumerate(weekly_goals, 1):
            print(f"{i}. {g}")
    else:
        print("- No weekly goals set")

def motivational_quote():
    print("\nMotivation Boost →", random.choice(quotes))

def give_rewards():
    global points, streak
    points += 10
    streak += 1

    print("\n🎉 You earned 10 points!")
    print("🔥 Streak:", streak)
    log_activity("earned rewards", f"Points: {points}, Streak: {streak}")

    if points >= 50 and "Bronze Student" not in badges:
        badges.append("Bronze Student")
        print("🏅 You unlocked badge: Bronze Student")
        log_activity("unlocked badge", "Bronze Student")

    if points >= 150 and "Silver Learner" not in badges:
        badges.append("Silver Learner")
        print("🏅 You unlocked badge: Silver Learner")
        log_activity("unlocked badge", "Silver Learner")

def show_weekly_time_graph():
    print("\nShowing time spent per subject per week graph...")

    if not time_allocation:
        print("No subjects or time allocation added yet!")
        return

    subjects_list = list(time_allocation.keys())
    weekly_hours = [t * 7 for t in time_allocation.values()]

    plt.figure(figsize=(10, 6))
    plt.bar(subjects_list, weekly_hours, color='skyblue')
    plt.title("Time Spent per Subject (Weekly)")
    plt.xlabel("Subjects")
    plt.ylabel("Hours per Week")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def log_study_session():
    print("\n📚 Log Study Session")
    if not subjects:
        print("No subjects added yet! Add subjects first.")
        return
    
    print("Available subjects:", subjects)
    subject = input("Enter subject you studied: ").strip()
    if subject not in subjects:
        print("Subject not found! Please choose from available subjects.")
        return
    
    try:
        hours_input = input("How many hours did you study? ").strip()
        if not hours_input:
            print("No input provided. Cancelling session log.")
            return
            
        hours = float(hours_input)
        if hours < 0:
            print("Hours cannot be negative!")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    current_time = datetime.datetime.now()
    session = {
        'subject': subject,
        'hours': hours,
        'date': current_time.strftime("%Y-%m-%d"),
        'time': current_time.strftime("%H:%M:%S")
    }
    
    study_sessions.append(session)
    log_activity("logged study session", f"'{subject}' for {hours} hours")
    print(f"✅ Study session logged: {subject} for {hours} hours on {session['date']} at {session['time']}")

def view_study_history():
    print("\n📊 Study History")
    if not study_sessions:
        print("No study sessions logged yet!")
        return
    
    total_hours = 0
    for i, session in enumerate(study_sessions, 1):
        print(f"{i}. {session['subject']} - {session['hours']} hours on {session['date']} at {session['time']}")
        total_hours += session['hours']
    
    print(f"\n📈 Total study time: {total_hours:.2f} hours across {len(study_sessions)} sessions")

# ========== DELETE FUNCTIONS ==========
def delete_subject():
    print("\n🗑️ Delete Subject")
    if not subjects:
        print("No subjects to delete!")
        return
    
    print("Current subjects:", subjects)
    subject = input("Enter subject name to delete: ").strip()
    
    if subject in subjects:
        subjects.remove(subject)
        if subject in time_allocation:
            del time_allocation[subject]
        print(f"✅ Deleted subject: {subject}")
        log_activity("deleted subject", f"'{subject}'")
    else:
        print("Subject not found!")

def delete_goal():
    print("\n🗑️ Delete Goal")
    if not daily_goals and not weekly_goals:
        print("No goals to delete!")
        return
    
    print("1. Delete Daily Goal")
    print("2. Delete Weekly Goal")
    choice = input("Choose option: ").strip()
    
    if choice == "1" and daily_goals:
        print("\nDaily Goals:")
        for i, goal in enumerate(daily_goals, 1):
            print(f"{i}. {goal}")
        try:
            idx = int(input("Enter goal number to delete: ")) - 1
            if 0 <= idx < len(daily_goals):
                removed = daily_goals.pop(idx)
                print(f"✅ Deleted: {removed}")
                log_activity("deleted daily goal", f"'{removed}'")
            else:
                print("Invalid goal number!")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid number.")
    
    elif choice == "2" and weekly_goals:
        print("\nWeekly Goals:")
        for i, goal in enumerate(weekly_goals, 1):
            print(f"{i}. {goal}")
        try:
            idx = int(input("Enter goal number to delete: ")) - 1
            if 0 <= idx < len(weekly_goals):
                removed = weekly_goals.pop(idx)
                print(f"✅ Deleted: {removed}")
                log_activity("deleted weekly goal", f"'{removed}'")
            else:
                print("Invalid goal number!")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid number.")
    else:
        print("No goals available to delete or invalid choice!")

def delete_study_session():
    print("\n🗑️ Delete Study Session")
    if not study_sessions:
        print("No study sessions to delete!")
        return
    
    print("Study Sessions:")
    for i, session in enumerate(study_sessions, 1):
        print(f"{i}. {session['subject']} - {session['hours']} hours on {session['date']}")
    
    try:
        idx_input = input("Enter session number to delete: ").strip()
        if not idx_input:
            print("No input provided. Cancelling deletion.")
            return
            
        idx = int(idx_input) - 1
        if 0 <= idx < len(study_sessions):
            removed = study_sessions.pop(idx)
            print(f"✅ Deleted session: {removed['subject']} on {removed['date']}")
            log_activity("deleted study session", f"'{removed['subject']}' on {removed['date']}")
        else:
            print("Invalid session number!")
    except ValueError:
        print("Invalid input! Please enter a number.")

def clear_all_data():
    print("\n⚠️ CLEAR ALL DATA")
    confirm = input("Are you sure you want to delete ALL data? (yes/no): ").strip().lower()
    if confirm == 'yes':
        global subjects, time_allocation, daily_goals, weekly_goals, points, streak, study_sessions, badges
        subjects.clear()
        time_allocation.clear()
        daily_goals.clear()
        weekly_goals.clear()
        study_sessions.clear()
        badges.clear()
        points = 0
        streak = 0
        print("✅ All data has been cleared!")
        log_activity("cleared all data", "User reset entire application")
    else:
        print("Data clearance cancelled.")

def view_recent_logs():
    """Display recent activity logs"""
    print("\n📋 Recent Activity Logs")
    try:
        with open('study_planner.log', 'r') as log_file:
            lines = log_file.readlines()
            if not lines:
                print("No logs available yet.")
                return
            
            # Show last 10 log entries
            recent_logs = lines[-10:]
            print("Last 10 activities:")
            for log in recent_logs:
                print(f"  📄 {log.strip()}")
    except FileNotFoundError:
        print("No log file found. Start using the planner to generate logs!")

# ========== ML PREDICTION FUNCTIONS ==========
def predict_performance():
    print("\n🤖 ML Performance Prediction")
    if len(study_sessions) < 3:
        print("Need at least 3 study sessions for prediction!")
        return
    
    # Simple prediction based on study patterns
    total_hours = sum(session['hours'] for session in study_sessions)
    avg_hours_per_session = total_hours / len(study_sessions)
    
    # Simple performance estimation
    if avg_hours_per_session >= 3:
        prediction = "Excellent! You're putting in great effort."
        estimated_grade = "A"
    elif avg_hours_per_session >= 2:
        prediction = "Good! Consistent studying will pay off."
        estimated_grade = "B"
    elif avg_hours_per_session >= 1:
        prediction = "Fair. Consider increasing study time for better results."
        estimated_grade = "C"
    else:
        prediction = "Need more study time to see improvement."
        estimated_grade = "D"
    
    print(f"📊 Based on your study patterns:")
    print(f"📈 Average study session: {avg_hours_per_session:.1f} hours")
    print(f"🎯 Prediction: {prediction}")
    print(f"📝 Estimated performance: {estimated_grade}")
    log_activity("used performance prediction", f"avg {avg_hours_per_session:.1f}h/session")

def classify_study_habits():
    print("\n🔍 Study Habits Classification")
    if not study_sessions:
        print("No study data available!")
        return
    
    total_hours = sum(session['hours'] for session in study_sessions)
    avg_session_length = total_hours / len(study_sessions)
    
    # Classification logic
    if avg_session_length < 1:
        habit_type = "SHORT_BURST"
        description = "You prefer short, frequent study sessions"
    elif avg_session_length > 3:
        habit_type = "DEEP_FOCUS" 
        description = "You prefer long, intensive study sessions"
    else:
        habit_type = "BALANCED"
        description = "You have balanced study session lengths"
    
    print(f"📊 Study Habit Analysis:")
    print(f"🔸 Type: {habit_type} - {description}")
    print(f"🔸 Average session: {avg_session_length:.1f} hours")
    print(f"🔸 Total sessions: {len(study_sessions)}")
    log_activity("classified study habits", f"Type: {habit_type}")

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
    print("10. Log Study Session")
    print("11. View Study History")
    print("12. Delete Subject")
    print("13. Delete Goal")
    print("14. Delete Study Session")
    print("15. Clear All Data")
    print("16. 📋 View Activity Logs")
    print("17. 🤖 Predict Performance")
    print("18. 🔍 Classify Study Habits")
    print("0. Exit")
    print("==================================")

# Main program loop
def main():
    print("🎓 Welcome to the Study Planner! 🎓")
    
    while True:
        show_menu()
        try:
            choice = input("💡 What do you want to do next? Enter your option number: ").strip()
            
            if not choice:  # Handle empty input
                print("Please enter a choice.")
                continue
                
            log_activity("menu selection", f"Option {choice}")
            
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
                print("Current Streak:", streak)
            elif choice == "9":
                show_weekly_time_graph()
            elif choice == "10":
                log_study_session()
            elif choice == "11":
                view_study_history()
            elif choice == "12":
                delete_subject()
            elif choice == "13":
                delete_goal()
            elif choice == "14":
                delete_study_session()
            elif choice == "15":
                clear_all_data()
            elif choice == "16":
                view_recent_logs()
            elif choice == "17":
                predict_performance()
            elif choice == "18":
                classify_study_habits()
            elif choice == "0":
                log_activity("exited application", "User ended session")
                print("Goodbye! Keep studying 😊")
                break
            else:
                print("Invalid choice. Please enter a number between 0-18.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logging.error(error_msg)
            print(f"An unexpected error occurred: {e}. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
