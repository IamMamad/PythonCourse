import random
import os


def gameOver(country, rightGuesses, wrongGuesses):
    isGameOver = False   # this indicates whether the game is over or not
    if rightGuesses == country:
        isGameOver = True
    if len(wrongGuesses) >= len(country):
        isGameOver = True
    return isGameOver


def finish(gameList):
    country = gameList[0]   # loads country name from list
    rightGuesses = gameList[1]   # loads right Guesses from list
    wrongGuesses = gameList[2]   # loads wrong Guesses from list
    print("Game Over!")
    print("Correct Answer="+country)
    print("Your Right Guesses:"+rightGuesses)
    print("Your Wrong Guesses:"+wrongGuesses)
    choice = input("Do you want to play Again?(y/n)")
    if choice == 'y':
        startGame()


def helpMe(gameList):
    country = gameList[0]   # loads country name from list
    rightGuesses = gameList[1]   # loads right Guesses from list
    wrongGuesses = gameList[2]   # loads wrong Guesses from list
    i = 0   # counter
    possibleHelps = []
    while i < len(country):
        if country[i] != rightGuesses[i]:
            possibleHelps.append(i)
        i += 1
    i = random.choice(possibleHelps)
    check(country, rightGuesses, wrongGuesses, country[i])


def check(country, rightGuesses, wrongGuesses, guess):
    i = 0   # this is a counter
    isAGoodGuess = False   # we use it later to decide whether or not add the guess to wrong guesses string
    while i < len(country):
        if country[i] == guess:   # this checks whether each letter of 'country' is equal to our guess 
            isAGoodGuess = True   # if guess is a letter in word country, it is a good guess
            rg = list(rightGuesses)   # convert string to list
            rg[i] = country[i]   # reveals the correctly guessed letter
            rightGuesses = "".join(rg)
        i += 1
    if not isAGoodGuess: 
        wrongGuesses += guess   # adds guess to wrong guesses
        if not gameOver(country, rightGuesses, wrongGuesses):
            newList = [country, rightGuesses, wrongGuesses]
            playTurn(newList)
        else:
            newList = [country, rightGuesses, wrongGuesses]
            finish(newList)
    else:
        if not gameOver(country, rightGuesses, wrongGuesses):
            newList = [country, rightGuesses, wrongGuesses]
            playTurn(newList)
        else:
            newList = [country, rightGuesses, wrongGuesses]
            finish(newList)


def playTurn(gameList):
    country = gameList[0]   #  loads country name from list
    rightGuesses = gameList[1]   # loads right Guesses from list
    wrongGuesses = gameList[2]   # loads wrong Guesses from list
    os.system('cls')   # cleans up the screen
    print("<<<GUESS THE COUNTRY!>>>")
    print(rightGuesses)
    print(wrongGuesses)
    guess = input("Guess a letter, or type '?' for a hint:")
    guess = guess[0]  # chooses only the first letter
    guess = guess.lower()
    if guess == '?':
        wrongGuesses += '**'
        if not gameOver(country, rightGuesses, wrongGuesses):
            newList = [country, rightGuesses, wrongGuesses]
            helpMe(newList)
        else:
            newList = [country, rightGuesses, wrongGuesses]
            finish(newList)
    else:
        check(country, rightGuesses, wrongGuesses, guess)


def startGame():
    countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguilla", "Antarctica", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahrain", "Bahamas", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bonaire", "Botswana", "Brazil", "Bulgaria", "Burundi", "Cambodia", "Cameroon", "Canada", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Congo", "Croatia", "Cuba", "Cyprus", "Denmark", "Djibouti", "Dominica", "Ecuador", "Egypt", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guyana", "Haiti", "Vatican", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea", "Kuwait", "Kyrgyzstan", "Lao", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Nicaragua", "Niger", "Nigeria", "Niue", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Samoa", "Arabia", "Senegal", "Serbia", "Seychelles", "Singapore", "Slovakia", "Slovenia", "Somalia", "Spain", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tokelau", "Tonga", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "Emirates", "England", "America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Yemen", "Zambia", "Zimbabwe"]
    country = random.choice(countries)  # choosing a random country from 'countries' list 
    country = country.lower()
    rightGuesses = ""
    for letter in country:  # with this loop we can create a string that has '-' as much as the number of letters in country
        rightGuesses += "-"
    wrongGuesses = ""  # since we have not made a guess yet
    gameList = [country, rightGuesses, wrongGuesses]  # this list is all of important data that our game needs
    playTurn(gameList)


startGame()

