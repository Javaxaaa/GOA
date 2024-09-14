def get_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a valid score (between 0 and 100).")
        except ValueError:
            print("Please enter a number.")


midterm_score = get_score("Enter the midterm exam score (0-100): ")
final_score = get_score("Enter the final exam score (0-100): ")
project_score = get_score("Enter the project score (0-100): ")


average_score = (midterm_score * 0.2) + (final_score * 0.4) + (project_score * 0.4)


if average_score >= 70:
    status = "passed"
else:
    status = "failed"


print(f"Your average score is: {average_score:.2f}. You have {status} the course.")