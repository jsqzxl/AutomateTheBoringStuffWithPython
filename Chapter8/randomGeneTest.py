import random
import americaCapitals

if __name__ == '__main__':

    print(americaCapitals.capitals)
    capitals = americaCapitals.capitals
    # Generate 35 quiz files
    filesNum = 35
    stateNum = len(capitals)
    for quizNum in range(filesNum):

        # TODO: Create the quize and answer key files.
        quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
        answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

        # Write out the heaser for the quiz
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizFile.write('\n\n')

        # Shuffle the order of the states
        states = list(capitals.keys())
        random.shuffle(states)

        # Loop through all 50 states, making a question for each.
        for questionNum in range(stateNum):
            #Get right and wrong answers.
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            # Write the question and the answer options to the quiz file
            quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
            for i in range(4):
                quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

            # write the answer key to a file.
            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizFile.close()
        answerKeyFile.close()
