## Student-Study-Planner
## Description  -
a student study planner is used to organise a student's life and help them balance all the subjects effectively. 

## Overview of the Project 
1. Many students want to study but cannot utilize that opportunity effectively due to poor management of time and unclear goals .
The student planner is a useful program that helps students to devise a study plan keeping in check the goals of a student and ensures wise management of time . 
It also helps the students to decide the time they want spend on each domain of subjects respectively and helps to  improve their academic performance .

## OBJECTIVES - STUDENT STUDY PLANNER 
1. To set a routine to be followed 
2. Setting clear goals 
3. Improving time management 
4. Increasing productivity with proper goals


## **Functional Requirements**
- Subject management (add/delete) with validation
- Time allocation with input validation
- Goal setting (daily/weekly) with tracking
- Study session logging with timestamps
- Reward system with points, streaks, badges
- Data visualization using matplotlib
- Analytics (performance prediction, habit classification)
- CRUD operations with data integrity
- Activity logging and audit trail

## **Non-functional Requirements**
- Console-based UI with intuitive navigation
- Comprehensive error handling and input validation
- Fast response times with efficient data structures
- Modular code for maintainability and extensibility
- File-based logging for persistence
- Input sanitization and safe operations

## **System Architecture Diagram**
```
Presentation Layer → Business Logic Layer → Data Layer
       ↓                    ↓                    ↓
Console UI +        Study Planning +      In-memory +
Visualization       Analytics Engine      File Logging
```

## **Process Flow Diagram**
- **Main Flow**: Start → Initialize → Menu Loop → Function Execution → Log → Repeat
- **Session Logging**: Check subjects → Input hours → Validate → Timestamp → Store → Log

## **UML Diagrams**

### **Use Case Diagram**
- **Actor**: Student
- **Use Cases**: Manage subjects, Allocate time, Set goals, Log sessions, View analytics, Earn rewards

### **Component Diagram**
- **Core**: Menu Controller, Subject Manager, Goal Manager, Session Logger
- **Support**: Reward System, Analytics Engine, Visualization, Activity Logger

### **Sequence Diagram**
```
User → System: Select Option
System → Function: Execute
Function → Data: Process
Data → Function: Return Result
Function → Logger: Record
System → User: Display Output
```

## **Database/Storage Design**

### **ER Diagram** (In-memory)
```
Subjects (name)
TimeAllocation (subject, hours)
Goals (daily[], weekly[])
Sessions (subject, hours, date, time)
UserStats (points, streak, badges[])
```

### **Schema Design**
- **Lists/Dicts**: subjects[], time_allocation{}, daily_goals[], weekly_goals[]
- **Session Objects**: {subject, hours, date, time}
- **Global Variables**: points, streak, badges[]

## **ML/Analytics Components**

### **Dataset Description**
- **Source**: User-generated study sessions
- **Features**: session hours, subject, timestamp, frequency
- **Size**: Dynamic, grows with user activity

### **Model Selection Rationale**
- **Performance Prediction**: Rule-based using average hours/session
- **Habit Classification**: Threshold-based (Short-burst <1h, Balanced 1-3h, Deep-focus >3h)
- **Rationale**: Simple, interpretable, no training data required

### **Evaluation Methodology**
- **Metrics**: Average session hours, total study time, consistency patterns
- **Validation**: User feedback on classification accuracy
- **Testing**: Boundary testing for habit thresholds

## Features 
1. we can add multiple subjects 
2. Delete individual subjects
3. Clear all subjects data
4.Set daily study hours per subject
5.Automatic weekly hour calculation (daily × 7)
6.Set daily study goals
7.Set weekly achievement goals

## Tools used-
I have used python language using it's standard libraries. some of the used modules are -
1. Matplotlib.pyplot 
2.random
3.datetime
4.numpy

## Techniques used-
CRUD - create, read, update, delete 
Model View Controller - it is used to access subjects, sessions, goals etc 

## Steps to install and run the program- 
1. Install Python 3.6+ on your system
2. Copy the entire python code
3. Create a new file called study_planer.py
4. Paste the code into the file
5. Save the file
6. Install the required libraries mentioned above
## Run the program
1. Open python idle
2. Open the file , select study_planner.py
3. Click on run button

## Testing Instructions-
1. Checking subjects 
Steps:
1. Choose Option 1 "Add Subjects"
2. Enter: "SUBJECT NAME 1 "
3. Enter: "SUBJECT NAME 2" 
4. Enter: "SUBJECT NAME 3"
5. Enter: "done"

## Expected Results:
"Added: SUBJECT NAME 1"
"Added: SUBJECT NAME 2" 
"Added: SUBJECT NAME 3"
Subjects list contains all three subjects

2. Allocate Time to Subjects
   Steps:
1. Choose Option 2 "Allocate Time"
2. For Mathematics: Enter "2"
3. For Physics: Enter "1.5" 
4. For Chemistry: Enter "1"

## Expected Results:
 All subjects get time allocations
"Time allocation completed" message
Numbers stored as floats.

