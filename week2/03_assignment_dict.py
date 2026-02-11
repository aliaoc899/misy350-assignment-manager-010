assignment = {
    "id": "HW1",
    "title" :  "Homework1: Intro to Database Design",
    "description": "Create an ER Model",
    "due_date": "2026-01-10",
    "available": False,
    "questions":[]
}
print(assignment)
print("----")
if "title" in assignment:
    print(f"Title: {assignment["title"]}")

assignment["additonal_notes"] = "basics of database" #add new key to the dictionary

print(assignment)