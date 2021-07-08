# My Dictionary
meaning = {
    "Contrast": "The state of being strikingly different from something else in juxtaposition or close association.",
    "Tycoon": "a wealthy, powerful person in business or industry.",
    "Pledge": "a solemn promise or undertaking.",
    "OverWhelm": "bury or drown beneath a huge mass of something, especially water.",
    "Glove": "a covering for the hand worn for protection against cold or dirt and typically having separate parts "
             "for each finger and the thumb. "
}
print("Welcome to Python Dictionary -- By Jay\n")
print("Words Available: \n1)Contrast\n2)Tycoon\n3)Pledge\n4)OverWhelm\n5)Glove\n")
print("Select a word given above")
user_selection = input()
if user_selection == "Contrast":
    print("\nMeaning Of Contrast: " + str(meaning["Contrast"]))
elif user_selection == "Tycoon":
    print("\nMeaning Of Tycoon: " + str(meaning["Tycoon"]))
elif user_selection == "Pledge":
    print("\nMeaning Of Pledge: " + str(meaning["Pledge"]))
elif user_selection == "OverWhelm":
    print("\nMeaning Of OverWhelm: " + str(meaning["OverWhelm"]))
elif user_selection == "Glove":
    print("\nMeaning Of Glove: " + str(meaning["Glove"]))
else:
    print("Sorry! No Word Found")
