import random

print("QUIZ COMPETITION")

yn = input("Do you want to play the quiz? (Yes/No)")

if yn == "No" or yn == "no":
    print("Okay! Maybe next time. Goodbye!")

elif yn == "Yes" or yn == "yes":

    while yn == "Yes" or yn == "yes":

        points = 0

        ques_dict = [
            {
                "q": "Which planet in our solar system currently holds the record for the most confirmed moons?\na) Jupiter\nb) Uranus\nc) Saturn\nd) Neptune\n",
                "a": "c"
            },

            {
                "q": "Which African country currently has the largest population?\na) Egypt\nb) Ethiopia\nc) South Africa\nd) Nigeria\n",
                "a": "d"
            },

            {
                "q": "Which is the largest ocean on Planet Earth?\na) Atlantic Ocean\nb) Indian Ocean\nc) Pacific Ocean\nd) Arctic Ocean\n",
                "a": "c"
            },

            {
                "q": "What gas do humans need to breathe in to survive?\na) Oxygen\nb) Carbon Dioxide\nc) Nitrogen\nd) Hydrogen\n",
                "a": "a"
            },

            {
                "q": "Which animal is famously known as the King of the Jungle?\na) Tiger\nb) Elephant\nc) Lion\nd) Gorilla\n",
                "a": "c"
            }
        ]

        random.shuffle(ques_dict)

        for i, question in enumerate(ques_dict, start=1):

            print(i, question["q"])

            ans = input("ans:- ")

            if ans == question["a"]:
                print("Correct Answer")
                points += 1
                print(f"Points Earned = {points}")
            else:
                print("Incorrect")
                print(f"Points Earned = {points}")

            print()

        print("CONGRATULATIONS!! YOUR QUIZ IS COMPLETED")
        print("TOTAL SCORE IS :-", points, "/ 5")

        yn = input("Do you want to play the quiz again? (Yes/No)")

        if yn == "No" or yn == "no":
            print("Okay! Maybe next time. Goodbye!")

else:
    print("Invalid input")