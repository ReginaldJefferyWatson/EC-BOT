import json

FILE = "data.json"

# Add a new student to the leaderboard
# Student = {name, id, fitness}
def add_student(name, username, score):
  new_student = {"name": name,
                 "username": username,
                 "score": score}
  
  with open(FILE, 'r') as file:
    leaderboard = json.load(file)
  
  #I have no idea why you need this line but you do
  students = leaderboard
  print(new_student)
  students.append(new_student)
  
  with open(FILE, 'w') as file:
    json.dump(students, file)

def overwrite_student(name, username, score):
  with open(FILE, 'r') as file:
    leaderboard = json.load(file)
  
  #I have no idea why you need this line but you do
  students = leaderboard
  
  for place, student in enumerate(students):
    if student["username"] == username:
      students.pop(place)
      student["name"] = name
      student["score"] = score
      student["username"] = username
  
  
  
  with open(FILE, 'w') as file:
    json.dump(students, file)

def sort():
  with open(FILE, 'r') as file:
    leaderboard = json.load(file)
    
    leaderboard.sort(key=lambda x: x["score"])
    return leaderboard


def format_leaderboard():
  leaderboard = sort()
  print(leaderboard)
  with open("leaderboard.txt", "w") as file:
    for place, student in enumerate(leaderboard):
      name = student["name"]
      fitness = student["score"]
      file.write(f"{place+1}. {name}: {fitness} \n")

def main():
  add_student("Drew", "test", "1")
  format_leaderboard()
  
if __name__ == "__main__":
  main()