# Dictionary storing age-based psychological/behavioral traits
User_Age = {
    "16": {
        "introvert": "Observant, highly reflective, values close 1-on-1 bonds, can feel overwhelmed in large social settings.",
        "extrovert": "Energetic, highly influenced by peer groups, expressive, seeks constant connection and validation.",
        "general_mood": "Navigating self-identity, high emotional intensity, and social awareness."
    },
    "17": {
        "introvert": "Independent thinker, deeply focused on personal interests, cautious about opening up to new people.",
        "extrovert": "Outspoken, active in group dynamics, thrives on social activities, ambitious about future plans.",
        "general_mood": "Transition stress (school to future planning), seeking autonomy and validation."
    },
    "18": {
        "introvert": "Selective with social energy, calm in personal space, thoughtful about major life choices.",
        "extrovert": "Enthusiastic about independence, eager to explore new environments, assertive in social circles.",
        "general_mood": "Adulthood entry, mix of exciting freedom and anxiety over independence."
    },
    "19": {
        "introvert": "Self-reliant, internalizes stress, prefers focused low-key routines and deep conversations.",
        "extrovert": "Network-oriented, driven by shared experiences, channels stress into social outings.",
        "general_mood": "Focusing on personal growth, career direction, and adapting to real-world responsibilities."
    },
    "20": {
        "introvert": "Pragmatic, strong personal boundaries, recharge through solitary reflection, highly self-aware.",
        "extrovert": "Goal-driven connector, confident in expressing needs, comfortable leading or collaborating.",
        "general_mood": "Early adulthood stabilization, balancing ambitions, relationship stability, and life goals."
    }
}


def get_age_mood(code):
    """
    Fetches behavioral data based on the age code string passed from main.py.
    """
    return User_Age.get(code, "Try Again Wrong Input !!!")


# Example call when testing age.py directly:
if __name__ == "__main__":
    sample_input = "18"
    print(get_age_mood(sample_input))

# main.py
from age import get_age_mood

user_input = input("Enter age (16-20): ")
result = get_age_mood(user_input)

if isinstance(result, dict):
    print(f"\n--- Behavioral Insight for Age {user_input} ---")
    print(f"General Mood: {result['general_mood']}")
    print(f"Introvert Trait: {result['introvert']}")
    print(f"Extrovert Trait: {result['extrovert']}")
else:
    print(result)