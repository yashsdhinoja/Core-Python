import time

# other file import variables
from age import get_age_mood

def run_behavior_assessment():
    print("==================================================")
    print("   Behavioral Assessment & Counseling Assistant   ")
    print("==================================================")
    
    # 1. Collect user age and validate
    user_name = input("Please enter your name : ")
    user_input = input("Please enter your age (Choose between 16 to 20): ").strip()
    profile = get_age_mood(user_input)
    
    if user_input not in ['16', '17', '18', '19', '20']:
        print(f"\n Hello, {user_name}")
        print(f"\n Result: {profile}")
        return

    print(f"\nAge Group Profile ({user_input} yrs): {profile}\n")
    print("-" * 50)
    print("Starting Behavioral Questionnaire...")
    print("Options: [1] Rarely  [2] Sometimes  [3] Often\n")

    # Define a small question bank with points
    questions = [
        "How often do you feel overwhelmed by your daily tasks or future plans?",
        "How often do you find it difficult to get a restful night of sleep?",
        "How often do you feel supported by your friends or family?"
    ]

    total_score = 0

    # 2. START THE TIMER (Math calculation: current epoch time)
    start_time = time.time()

    # Loop through questions interactively
    for i, q in enumerate(questions, start=1):
        while True:
            try:
                print(f"Question {i}: {q}")
                choice = int(input("Enter your choice (1, 2, or 3): "))
                if choice in [1, 2, 3]:
                    total_score += choice
                    break
                else:
                    print("Please enter only 1, 2, or 3.\n")
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
        print("-" * 30)

    # 3. END THE TIMER (Math calculation: duration elapsed)
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)  # Rounded to 2 decimal places

    # 4. Generate Counseling Feedback based on Score
    print("\n================ Assessment Summary ================")
    print(f"⏱️ Total Time Taken: {elapsed_time} seconds")
    print(f"📊 Final Behavioral Score: {total_score} / 9")
    
    print("\nCounseling Recommendation:")
    if total_score <= 4:
        print("-> Low stress levels detected. You are coping remarkably well with your current routine!")
    elif total_score <= 7:
        print("-> Moderate stress detected. Consider incorporating short mindful breaks or physical activity into your day.")
    else:
        print("-> High stress detected. It may be beneficial to talk through your concerns with a trusted mentor or professional counselor.")
    print("=====================================================")


if __name__ == "__main__":
    run_behavior_assessment()