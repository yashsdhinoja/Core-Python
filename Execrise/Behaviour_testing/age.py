User_Age = {
'16': "High energy, highly peer-focused, experiencing identity exploration and occasional intense mood variability.",
    '17': "Focused on future planning (exams/college), balancing a desire for independence with lingering reliance on family.",
    '18': "Navigating major life transitions, experiencing freedom paired with new responsibilities and decision anxiety.",
    '19': "Adapting to emerging adulthood, exploring personal values, career paths, and building deeper self-reliance.",
    '20': "Balancing long-term goals, managing stress related to career or higher education, and solidifying a personal identity."
}

def get_age_mood(code):
    """Retrieves the psychological profile based on the age string provided."""
    return User_Age.get(code, "Try Again Wrong Input !!!")

if __name__ == "__main__":
    user_input = input("Enter age (16 to 20): ").strip()

    result = get_age_mood(user_input)
    print(result)