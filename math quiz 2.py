print("Hello! This is a math game to test your skill! (numbers only, no letters)")
Question1 = str(input("Question 1, 367+832=?"))

if Question1 == "1199":
    print("Perfect! Let's move on to the next question.")
else:
    print("It's okay, you can still move on.")

Question2 = str(input("Question 2, 9312-6390=?"))

if Question2 == "2922":
    print("Great job, if you did the last question wrong, this time you have improved!")
else:
    print("It is okay to make mistakes.")

Question3 = str(input("Okay! Last question, 10^2 is..."))

if Question3 == "100":
    print("Amazing! You did the math quiz! I will update sometimes for more questions, but for now, that's all!")
else:
    print("Even if you got Question 1, Question 2, or Question 3, you still tried your best!")

input("Type anything to leave . . .")