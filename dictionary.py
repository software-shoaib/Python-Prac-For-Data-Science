marks= {
    'maths': 60,
    'science': 70,
    'history': 80,
    'english': 40,
    'python': 90,
    'physics': 20
}

print (f"Marks: {marks}")

#print(marks.keys())
#print(marks.values())

for subject in marks.keys():
    print(subject)

for score in marks.values():
    print(score)

print("\nPASS AND FAIL REPORT\n")

for subject, score in marks.items():
    print(f"{subject}: {score}/100")

for subject, score in marks.items():
    if score>=50:
        print(f"{subject} is passed")
    else:
        print(f"{subject} is failed!!!!!")


print(f" lous got marks in python: {marks['python']}")