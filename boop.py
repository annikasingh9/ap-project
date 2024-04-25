import random

def welcome_message():
    greetings = ["Yo bro", "Sup good lookin'", "Hey queen"]
    print(random.choice(greetings))

video_titles = ["I Love Minions - Here's Why",
    "Political Theory - Karl Marx",
    "Parallel Worlds Probably Exist",
    "A Tribute to Minecraft",
    "Funniest Pranks...(REAL! NOT FAKE!)",
    "Was President JFK Really Killed by the CIA",
    "TOP 10 paranormal activites caught in 4k"  
]
#these were all vids on my reccomended at one point or another haha

related_topics = {"I Love Minions - Here's Why": ["Dispicable Me", "Analysis", "Animated Films"],
    "Political Theory - Karl Marx": ["Social Justice", "Sociology", "Economics"],
    "Parallel Worlds Probably Exist": ["Physics", "Space Exploration", "Science"],
    "A Tribute to Minecraft": ["Video Games", "Minecraft", "Nostalgic Content"],
    "Funniest Pranks...(REAL! NOT FAKE!)": ["Stunts", "Humor", "Drama TV"],
    "Was President JFK Really Killed by the CIA": ["History", "Conspiracy", "Historical Mysteries"],
    "TOP 10 paranormal activites caught in 4k": ["Misinformation", "Scary Stories", "Suspense"]   
}

def get_user_choices():
    try:
        user_input = input("\nEnter your choices (comma-separated numbers): ")
        choices = [video_titles[int(choice.strip()) - 1] for choice in user_input.split(',')]
        return choices
    except ValueError:
        print("Oops! Numbers only buddy.")
        return get_user_choices()
    except IndexError:
        print("One or more of your choices are out of the valid range.")
        return get_user_choices()

def recommend_topics(choices):
    recommendations = set()
    for choice in choices: 
        if choice in related_topics:
            recommendations.update(related_topics[choice])
    return recommendations

def main():
    welcome_message()
    print("Pick any videos you want to watch from the list below:")
    for index, title in enumerate(video_titles, start=1):
        print(f"{index}. {title}") #thank you stack overflow
    
    user_choices = get_user_choices()
    if user_choices == "1":
        print("\nBased on your choice, you might also be interested in:")
        for topic in related_topics["I Love Minions - Here's Why"]:
            print(topic) #I wanted to demonstrate multiple ways to code a program like this.
            #this if-statement method is slightly tedious, but helpful if errors are occuring at a specific index.

    else:  
        print("\nAccording to my calculations, you might like these topics:")
        for topic in recommend_topics(user_choices): #but here, iterating across the entire function lets us skip the if statement process
            print(topic) 

if __name__ == "__main__":
    main() 
    #this allows the program to run.