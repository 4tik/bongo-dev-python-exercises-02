# Write conditional statements to identify the student’s average marks. If any subject’s mark is less than 40, 
# you should print FAILED instead of making average marks

def student_mark_status(marks):
    for mark in marks:
        if(mark<40):
            return "FAILED"
    return f"Average Mark : {sum(marks)/len(marks)}"

student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]
student_3 = [57, 55, 80, 98, 46]

print(student_mark_status(student_1))
print(student_mark_status(student_2))
print(student_mark_status(student_3))

# print(get_avg_num(student_1))
