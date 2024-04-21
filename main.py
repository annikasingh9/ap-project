import sys, random, math

# There will be lists with certain videos or foods idk and they will display for user to pick two, iterate thru multple lists. Then, after they've made selections, they recieve reccomendations for their next watch or purcahse. List of their reccomendations based on what they had picked displays.

#youtubes rec algorithm 

#need another user interface and def function

yt_options = ["top 10 rollarcoasters", "scary stories to tell your friends (REAL)", "top 10 feminist destroyed compilation","DIY friendship bracelet", "5-min Craft (for girls)"]


choice1 = input("Pick 1 or 2 to watch")
for option in options:
        if choice1 == "1":
            print(options[0][0])


for i in range(2):
      print(options)



video_titles = [
    "The Secret Life of Cats",
    "Cooking with Fire: BBQ Mastery",
    "Exploring the Cosmos: A Journey Through Space",
    "DIY Home Improvement: Transform Your Space",
    "The Art of Photography: Capturing Moments",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Building a Stronger You"
]

related_topics = {
    "The Secret Life of Cats": ["Pets", "Animal Behavior", "Cat Care Tips"],
    "Cooking with Fire: BBQ Mastery": ["Grilling Techniques", "Outdoor Cooking", "Barbecue Recipes"],
    "Exploring the Cosmos: A Journey Through Space": ["Astronomy", "Space Exploration", "Cosmology"],
    "DIY Home Improvement: Transform Your Space": ["Home Renovation", "Interior Design", "DIY Projects"],
    "The Art of Photography: Capturing Moments": ["Photography Tips", "Composition Techniques", "Camera Gear Reviews"],
    "History Uncovered: Ancient Civilizations": ["Ancient History", "Archaeology", "Historical Mysteries"],
    "Fitness Fundamentals: Building a Stronger You": ["Exercise Techniques", "Nutrition Tips", "Healthy Lifestyle"]
}

print("Welcome to our video recommendation system!")
print("Please select your favorite videos from the list below (separated by commas):")
for index, title in enumerate(video_titles, start=1):
    print(f"{index}. {title}")

user_choices = input("\nEnter your choices: ").split(',')

print("\nBased on your choices, you might also\be interested in:")
for choice in user_choices:
    choice = choice.strip()
    if choice in related_topics:
        print(f"For '{choice}':")
        for topic in related_topics[choice]:
            print(f"- {topic}")
