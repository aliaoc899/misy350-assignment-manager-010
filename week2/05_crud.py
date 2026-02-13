#CRUD

#create
next_assignment_id = 1

new_id = "HW" + str(next_assignment_id)
print(new_id)

assignments = [
    {"id":new_id ,
     "title" :  "Intro to DB",
     "description" : "basics"
     }
]
next_assignment_id +=1

new_id = "HW" + str(next_assignment_id)
assignments.append(
    {"id": new_id,
     "title": "case study",
     "description": "ER Design"}
)

print(assignments)


#Read

## Query: Display all assignment information
#input 

#process

#output
for assignmnet in assignments:
    print(assignmnet)



## Query: find assignment with a title = Intro to DB and display its information
print("Query: find assignment with a title = Intro to DB and display its information")
#input 


#process

# Find an assignmnet
exists = False
found_assignment = None
for assignment in assignments:
    if assignment["title"] == "Intro to DB":
        exists = True
        found_assignment = assignment
        break

#output
#Display assignment
if exists:
    print(found_assignment)
else:
    print("Assignmnet does not exist.")


# Query = Update the title of an assignment with the tile = Intro to DB to Introduction to database

#input

##process


##output
