"""
initalize list 
add id to lst when action is schedule
when cancel remove last added id
store last added id in lst rep cancelled
when reschedule n times append n ele last added to cancelled back to schedule
return scheduled

question: is id always 1 charc last and seperated by whitespace
"""


def manage_stage_changes(changes):
    schedule = []
    cancelled = []

    for change in changes:
        if change == "Cancel":
           cancelled.append(schedule.pop())
        elif change == "Reschedule":
            schedule.append(cancelled.pop())
        else:
            ID = change[-1]
            schedule.append(ID)

    return schedule

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

#learned strategically think abouut grouping contionals/decision logic. Dont instictually go in order of how the problem was presented

