print("\nWelcome to Python Quiz Game Developed -- By Jay")

# Topics
topics = ["About World", "Current Affairs", "Computer Science"]

# Questions
aboutWorldQ = ["Which one is the smallest ocean in the World?",
               "Which country gifted the 'Statue of Liberty' to USA in 1886?",
               "Dead Sea is located between which two countries?",
               "Total number of oceans in the World is", "Which country is known as playground of europe"]

currentAffairsQ = ["Which Union Ministry has notified the standards for Safety Evaluation of Hydrogen Fuels?",
                   "Which E-commerce platform launched a Start-up promotion and mentoring programme named ‘Leap’?",
                   "Which Indian airport has partnered with Virgin Hyperloop for Hyperloop corridor?",
                   "When was the Indian Meteorological Department established?",
                   "India has provided around 3000 vials of Remdisvir to which country?"]

computerScienceQ = ["Which are the common languages used in Web Development?",
                    "What was the first name given to \"JavaScript\" when it was developed?",
                    "Which of the following Java Classes belongs to \"io\" package?",
                    "Where is Python Programming Language used?",
                    "Which is the modern language used in Android Development"]

# Answers
aboutWorldA = ["france", "central arctic ocean", "israel and jordan", "switzerland", "5 oceans"]
currentAffairsA = ["ministry of road transport and highways", "bangalore international airport", "flipkart", "1875",
                   "myanmar"]
computerScienceA = ["html, css and javascript", "data science", "kotlin", "mocha", "buffered reader"]

point = 0


# Methods
def correct():
    global point
    print("Correct!")
    point += 1

def wrong():
    global point
    print("Wrong!")
    point -= 1

def opt1(answer):
    if answer.lower() == aboutWorldA[0] or answer.lower() == currentAffairsA[0] or answer.lower() == computerScienceA[0] or answer == "1":
        correct()
    else:
        wrong()

def opt2(answer):
    if answer.lower() == aboutWorldA[1] or answer.lower() == currentAffairsA[1] or answer.lower() == computerScienceA[1] or answer == "2":
        correct()
    else:
        wrong()

def opt3(answer):
    if answer.lower() == aboutWorldA[2] or answer.lower() == currentAffairsA[2] or answer.lower() == computerScienceA[2] or answer == "3":
        correct()
    else:
        wrong()

def opt4(answer):
    if answer.lower() == aboutWorldA[3] or answer.lower() == currentAffairsA[3] or answer.lower() == computerScienceA[3] or answer == "4":
        correct()
    else:
        wrong()

def opt5(answer):
    if answer.lower() == aboutWorldA[4] or answer.lower() == currentAffairsA[4] or answer.lower() == computerScienceA[4] or answer == "5":
        correct()
    else:
        wrong()


play = input("\nDo you want to play? ")

if play.lower() == "yes":
    select = input(f"\nSelect a Topic: \n\n1) {topics[0]} \n2) {topics[1]} \n3) {topics[2]}\n")

    if select == "1" or select.lower() == "about world":
        print("Questions ", topics[0])

        print(f"\nQ-1: {aboutWorldQ[0]}")
        print(f"1) Atlantic Ocean\n2) Central Arctic Ocean\n3) Pacific Ocean\n4) Indian Ocean\n5) Southern Oceans")
        ans1 = input()
        opt2(ans1)

        print("\nQ-2: ", aboutWorldQ[1])
        print("1) France\n2) Britain\n3) America\n4) India\n5) Norway")
        ans2 = input()
        opt1(ans2)

        print("\nQ-3: ", aboutWorldQ[2])
        print("1) US and Canada\n2) China and Mongolia\n3) Spain and France\n4) Israel and Jordan\n5) Iran and Iraq")
        ans3 = input()
        opt4(ans3)

        print("\nQ-4: ", aboutWorldQ[3])
        print("1) 12 Oceans\n2) 2 Oceans\n3) 7 Oceans\n4) 3 Oceans\n5) 5 Oceans")
        ans4 = input()
        opt5(ans4)

        print("\nQ-5: ", aboutWorldQ[4])
        print("1) Germany\n2) Italy\n3) Switzerland\n4) France\n5) Greece")
        ans5 = input()
        opt3(ans5)

        print(
            f"\nAnswers: \nA-1: {aboutWorldA[1]}, \nA-2: {aboutWorldA[0]}, \nA-3: {aboutWorldA[2]}, \nA-4: {aboutWorldA[4]}, \nA-5: {aboutWorldA[3]}")
    elif select == "2" or select.lower() == "current affairs":
        print("Questions ", topics[1])

        print(f"\nQ-1: {currentAffairsQ[0]}")
        print(
            "1) Ministry of Road Transport and Highways\n2) Ministry of Power\n3) Ministry of MSME\n4) state ministry\n5) ] Ministry of Renewable Energy")
        ans1 = input()
        opt1(ans1)

        print("\nQ-2: ", currentAffairsQ[1])
        print("1) Amazon\n2) E-Bay\n3) Flipkart\n4) Snapdeal\n5) Shopclues")
        ans2 = input()
        opt3(ans2)

        print("\nQ-3: ", currentAffairsQ[2])
        print(
            "1) Delhi International Airport\n2) Bangalore International Airport\n3) Cochin International Airport\n4) Mumbai International Airport\n5) Ahmedabad International Airport")
        ans3 = input()
        opt2(ans3)

        print("\nQ-4: ", currentAffairsQ[3])
        print("1) 1975\n2) 1990\n3) 1950\n4) 1875\n5) 1947")
        ans4 = input()
        opt4(ans4)

        print("\nQ-5: ", currentAffairsQ[4])
        print("1) Bangladesh\n2) Sri Lanka\n3) Thailand\n4) Nepal\n5) Myanmar")
        ans5 = input()
        opt5(ans5)

        print(
            f"\nAnswers: \nA-1: {currentAffairsA[0]}, \nA-2: {currentAffairsA[2]}, \nA-3: {currentAffairsA[1]}, \nA-4: {currentAffairsA[3]}, \nA-5: {currentAffairsA[4]}")
    elif select == "3" or select.lower() == "computer science":
        print("Questions ", topics[2])

        print(f"\nQ-1: {computerScienceQ[0]}")
        print(
            "1) HTML, CSS and Javascript\n2) C\C++\n3) Turbo C++\n4) Only JavaScript\n5) HTML and CSS")
        ans1 = input()
        opt1(ans1)

        print("\nQ-2: ", computerScienceQ[1])
        print("1) TypeScript\n2) EcmaScript\n3) LiveScript\n4) Mocha\n5) Ecma")
        ans2 = input()
        opt4(ans2)

        print("\nQ-3: ", computerScienceQ[2])
        print(
            "1) Scanner\n2) String\n3) InetAddress\n4) Component\n5) Buffered Reader")
        ans3 = input()
        opt5(ans3)

        print("\nQ-4: ", computerScienceQ[3])
        print(
            "1) Web Development\n2) Data Science\n3) Android Development\n4) Server-Side Development\n5) Front-End Development")
        ans4 = input()
        opt2(ans4)

        print("\nQ-5: ", computerScienceQ[4])
        print("1) Python\n2) Java\n3) Kotlin\n4) C\n5) C#")
        ans5 = input()
        opt3(ans5)

        print(
            f"\nAnswers: \nA-1: {computerScienceA[0]},\nA-2: {computerScienceA[3]}, \nA-3: {computerScienceA[4]}, \nA-4: {computerScienceA[1]}, \nA-5: {computerScienceA[2]}")

        print(f"\nYou scored {str(point)} / 5!")
        print(f"Your Percentage: {(point * 100) / 5}%")
else:
    quit()
