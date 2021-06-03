from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if question["answer"] == answer:
        return True
    else:
        return False

def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    print("Erasing two incorrect options...")
    print("Options remaining:")
    i = 1
    while i<=4:
        if i == ques["answer"]:
            print(f'\tOption',i,':',ques["option"+str(i)])
            break
        i+=1
    print(f'\tOption',i%4+1,':',ques["option"+str((i%4)+1)])


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    print("Welcome to the game")
    min_amount = 0
    amount = 0
    ll = True
    i = 0
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    while i < 15:
        print(f'\tQuestion',i+1 ,':',QUESTIONS[i]["name"])
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice (1-4):')
        # check for the input validations
        if ans == 'lifeline':
            if ll:
                if i!=14:
                    lifeLine(QUESTIONS[i])
                    ans = input('Your choice from remaining options:')
                else:
                    while ans == 'lifeline':
                        print("No lifeline for this question!")
                        ans = input('Your choice (1-4):')
                ll = False
            else:
                while ans == 'lifeline':
                    print("No lifeline available")
                    ans = input('Your choice (1-4):')
        if ans == 'quit':
            break
        if isAnswerCorrect(QUESTIONS[i], int(ans)):
            print('Correct!')
            # print the total money won.
            amount = QUESTIONS[i]["money"]
            print("Amount won until now: Rs. ",amount)
            # See if the user has crossed a level, print that if yes
            if i == 4:
                print("Level 1 cleared!")
                min_amount = 10000
            if i == 9:
                print("Level 2 cleared!")
                min_amount = 320000
        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect Answer!')
            print('The correct answer is option',QUESTIONS[i]["answer"])
            amount = min_amount
            break
        i += 1
    #print the total money won in the end
    print("Final amount: Rs.", amount)
kbc()
