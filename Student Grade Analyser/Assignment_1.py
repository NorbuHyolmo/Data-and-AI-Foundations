def letter_grade(score):
    if not (0 <= score <= 100):
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"


def analyse(students):
    return {
        name: {"score": score, "grade": letter_grade(score)}
        for name, score in students.items()
    }


def summary(results):
    avg = sum(v["score"] for v in results.values()) / len(results)
    highest = max(results, key=lambda k: results[k]["score"])
    lowest  = min(results, key=lambda k: results[k]["score"])

    counts = {}
    for v in results.values():
        grade = v["grade"]
        counts[grade] = counts.get(grade, 0) + 1

    print(f"\nClass Average : {avg:.2f}")
    print(f"Highest Score : {highest} ({results[highest]['score']})")
    print(f"Lowest Score  : {lowest} ({results[lowest]['score']})")

    grade_line = "  ".join(f"{g}={counts.get(g, 0)}" for g in ["A", "B", "C", "D", "F"])
    print(f"Grade Counts  : {grade_line}")


# --- Main ---
students = {
    "Ram": 92, "Shyam": 78, "Justin": 85,
    "Dave": 61, "Eve": 55, "Frank": 99
}

try:
    results = analyse(students)
    for name, data in sorted(results.items()):
        print(f"{name:<7}: {data['score']} → {data['grade']}")
    summary(results)
except ValueError as e:
    print(f"Error: {e}")


print("\n--- Invalid Score Test ---")
try:
    analyse({"Charan": 110})
except ValueError as e:
    print(f"Caught ValueError → {e}")