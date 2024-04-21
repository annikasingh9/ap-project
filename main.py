import random

video_titles = [
    "I Love Minions - Here's Why",
    "Political Theory - Karl Marx",
    "Parallel Worlds Probably Exist",
    "A Tribute to Minecraft",
    "Funniest Pranks...(REAL! NOT FAKE!)",
    "Was President JFK Really Killed by the CIA",
    "TOP 10 paranormal activites caught in 4k" ]

related_topics = {
    "I Love 'Minions' - Here's Why": ["Dispicable Me", "Analysis", "Animated Films"],
    "Political Theory - Karl Marx": ["Economics", "Communist theory", "Society"],
    "Parallel Worlds Probably Exist": ["Physics", "Space Exploration", "Science"],
    "A Tribute to Minecraft": ["Video Games", "Minecraft", "Nostalgic Content"],
    "Funniest Pranks...(REAL! NOT FAKE!)": ["Stunts", "Humor", "Drama TV"],
    "Was President JFK Really Killed by the CIA": ["History", "Conspiracy", "Historical Mysteries"],
    "TOP 10 paranormal activites caught in 4k": ["Misinformation", "Scary Stories", "Suspense"]}

def get_recommendations(choices):
    recommendations = set()
    for choice in choices:
        choice = choice.strip()
        if choice in related_topics:
            recommendations.update(related_topics[choice])
    return recommendations

print("Hi! Welcome to this topic recommendation system.")
print("Pick as many videos as you want from below to watch from the list (write numbers & seperate by comma):")

for index, title in enumerate(video_titles, start=1):
    print(f"{index}. {title}")

user_choices = input("\nPut 'em here (comma-separated numbers): ")
user_choices = [video_titles[int(choice) - 1] for choice in user_choices.split(',')]

print("\nAccording to my calculations, you'd like these topics:")
recommendations = get_recommendations(user_choices)
for topic in recommendations:
    print(topic)

