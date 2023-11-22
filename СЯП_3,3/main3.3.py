with open("учебные_предметы.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

subject_dict = {}

for line in lines:
    parts = line.split(":")
    subject = parts[0].strip()
    activities = parts[1].split()

    total_lectures = total_pracricals = total_labs = 0

    for activity in activities:
        count, activity_type = activity.strip("()").split("(")
        count = int(count)
        if activity_type == "л":
            total_lectures += count
        elif activity_type == "пр":
            total_pracricals += count
        elif activity_type == "лаб":
            total_labs += count

    total = total_lectures + total_labs + total_pracricals

    subject_dict[subject] = total

print(subject_dict)