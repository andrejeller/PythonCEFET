import random
HANGMANPICS = [ '''


 +---+
 |   |
     |
     |
     |
     |
=========''','''

 +---+
 |   |
 O   |
     |
     |
     |
=========''','''

 +---+
 |   |
 O   |
 |   |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''','''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
words= 'formiga babuino texugomorcego urso castor camelo cobra puma coiote corvo veado cachorro burro pato aguia furao raposa sapo ganso falcao leao lagarto lhama toupeira macaco alce mula tritao lontra coruja panda papagaio ponbo coelho carneiro rato corvo rinoceronte salmao tubarao ovelha preguiça cobra aranha cegonha cisne tigre sapo truta peru tartarura fuinha baleia lobo zebra'.split()

def getRandomWors(wordList):
    #Esta funçao retorna uma string aleatoria da lista de strings
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList [wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:' , end=' ')
    for letters in missedLetters:
        print(letter, end=' ')
        print()

        blanks = '_' * len(secretWord)

        for i in range(len(secretWord)): # subistitui os espaços em branco pelas letras adivinhadas corretamente
            if secretWord[i] in correctLetters:
                blanks = blanks[:i] + secretWord[i] + blanks[i+l:]

        for letter in blanks: # mostra a palavra secreta com esoaços entre cada letra
            print(letter, end =' ')
            print()

def getGuess(alreadyGuessed):
    #retorna a letra que o jogador escolheu.Esta funçao garante que o jogador digitou uma unica letra e nada mais.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Pleas enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that latter.Choose again.')
        elif guess not in ' abcdefghijklmnopqrstuvwxyz':
            print('Pleas enter a LETTER.')
        else:
            return guess

def playAgain():
    #Esta funçao retorna Trua se o jogador quiser jogar novamente.Do contrario, retorna False.
    print('Do you wnt to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWors(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    #Permite que o jogador digite uma letra
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Verifica se o jogador venceu
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Yes! The sicret word is ''' + secretWord + '!You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            #Verifica so o jogador perdeu
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(correctLetters)) + ' correct guesses, the word was '+ secretWord + '')
            gameIsDone = True

        #Pergunta ao jogador que ele gostaria de jogar novamente(apenas se o jogo foi encerrado).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
