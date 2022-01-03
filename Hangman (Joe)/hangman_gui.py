import tkinter as tk
import wordPicker

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Hangman!")
        self.configure(background = "#427787")#6ABFD8

        self.titleFont = ("Helvetica", 22, "bold", "italic") # Big thick italic font
        self.buttonFont  = ("Helvetica", 12, "bold")
        self.textFont  = ("Helvetica", 19, "bold")
        self.resultFont = ("Helvetica", 28, "bold", "italic")

        self.containerFrame = tk.Frame(self)
        self.containerFrame.pack(side = "top", fill = "both", expand = True, padx = 7, pady = 7)
        self.containerFrame.grid_rowconfigure(0, weight=1)
        self.containerFrame.grid_columnconfigure(0, weight=1)


        self.frames = {}

        #---Setting up start pages---#

        for F in (startPage, optionScreen, botDiffScreen, userwordScreen):
            pageName = F.__name__
            frame = F(self.containerFrame, self)
            self.frames[pageName] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("startPage")


    def makegameFrame(self, *args):

        
        frame = gameFrame(self.containerFrame, self, args)
        self.frames["gameFrame"] = frame
        frame.grid(row=0, column=0, sticky="nsew")
            
        self.showFrame("gameFrame")

    def makeresultFrame(self, result):

        
        for F in (deathScreen, winScreen):
            pageName = F.__name__
            frame = F(self.containerFrame, self)
            self.frames[pageName] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.showFrame(result)

    def showFrame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()


class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller


        hangmanLabel = tk.Label(self, text = "Hangman!", font = self.controller.titleFont)
        hangmanLabel.pack(side = "top", expand = True, padx = 50, pady = 40)


        playButton = tk.Button(self, text = "Play!", font = self.controller.buttonFont, command = lambda: self.controller.showFrame("optionScreen"))
        playButton.pack(side = "top", expand = True, padx = 30, pady = 20)

        quitButton = tk.Button(self, text = "Quit", font = self.controller.buttonFont, command = lambda: self.controller.destroy())
        quitButton.pack(side = "top", expand = True, padx = 30, pady = (20, 30))

class optionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.backButton = tk.Button(self, text = "< Back", font = ("Helvetica", 7, "bold"), command = lambda: self.controller.showFrame("startPage"))
        self.backButton.pack(side = "top", anchor = tk.E)

        self.singleplayerButton = tk.Button(self, text = "Single Player", font = self.controller.buttonFont, command = lambda: self.controller.showFrame("botDiffScreen"))
        self.singleplayerButton.pack(side = "top", expand = True)

        self.twoplayerButton = tk.Button(self, text = "Two Players", font = self.controller.buttonFont, command = lambda: self.controller.showFrame("userwordScreen"))
        self.twoplayerButton.pack(side = "top", expand = True)

class botDiffScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.backButton = tk.Button(self, text = "< Back", font = ("Helvetica", 7, "bold"), command = lambda: self.controller.showFrame("optionScreen"))
        self.backButton.pack(side = "top", anchor = tk.E)

        self.diffLabel = tk.Label(self, text = "Choose bot\ndifficulty:", font = self.controller.textFont)
        self.diffLabel.pack(side = "top", pady = 10)

        self.easyButton = tk.Button(self, text = "Easy", font = self.controller.buttonFont, command = lambda: self.controller.makegameFrame(5))
        self.easyButton.pack(side = "top", expand = True)

        self.mediumButton = tk.Button(self, text = "Medium", font = self.controller.buttonFont, command = lambda: self.controller.makegameFrame(6))
        self.mediumButton.pack(side = "top", expand = True)

        self.hardButton = tk.Button(self, text = "Hard", font = self.controller.buttonFont, command = lambda: self.controller.makegameFrame(7))
        self.hardButton.pack(side = "top", expand = True)

class userwordScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.entryText = tk.StringVar()

        self.backButton = tk.Button(self, text = "< Back", font = ("Helvetica", 7, "bold"), command = lambda: self.controller.showFrame("optionScreen"))
        self.backButton.pack(side = "top", anchor = tk.E)


        self.enterwordLabel = tk.Label(self, text = "Enter a word:", font = self.controller.titleFont)
        self.enterwordLabel.pack(side = "top", pady = 10)

        self.wordEntry = tk.Entry(self, textvariable = self.entryText)
        self.wordEntry.pack(side = "top", pady = 10)
        self.wordEntry.configure(show = "*")
        self.controller.bind('<Return>',lambda event:self.getEntry())

        self.showtextButton = tk.Button(self, text = "Show text", font = ("Helvetica", 10, "bold"))
        self.showtextButton.bind("<ButtonPress-1>", lambda event:self.entryShow())
        self.showtextButton.bind("<ButtonRelease-1>", lambda event:self.entryHide())
        self.showtextButton.pack(side = "top", pady = 10)

        self.enterButton = tk.Button(self, text = "Enter", font = ("Helvetica", 15, "bold"), command = lambda: self.getEntry())
        self.enterButton.pack(side = "top", pady = 10)

    def entryShow(self):
        self.wordEntry.configure(show = "")
    def entryHide(self):
        self.wordEntry.configure(show = "*")

    def getEntry(self):
        self.userWord = self.entryText.get()
        setWord(self.userWord)
        self.entryText.set("")
        self.controller.makegameFrame()

class gameFrame(tk.Frame):
    def __init__(self, parent, controller, diff):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        if diff:
            self.difficulty = diff[0]
            self.botWord = pickbotWord(self.difficulty)
            #print(self.botWord)
            setWord(self.botWord)

        self.rightFrame = tk.Frame(self)
        self.rightFrame.pack(side = "right", fill = "both", expand = True, padx = 5, pady = 5)

        #---Hangman draw box---#

        self.canvas1 = tk.Canvas(self, bg = "#B8CCD2", width = 300, height = 400)
        self.canvas1.pack(side = "left", fill = "both")#,  expand = True)

        self.hangmanLevel = 0

        self.hangmanParts = []
        self.hanCoords = [(70, 350, 70, 100), (20, 350, 125, 350), (50, 100, 220, 100), (70, 150, 115, 100), (217, 100, 217, 165), 
                          (202, 163, 232, 196), (217, 196, 217, 250), (217, 248, 190, 285), (217, 248, 244, 285),
                          (217, 223, 187, 223), (217, 223, 249, 223)]
        self.hanWidth = 5

        #---Guess entry box---#

        self.drawKeyboard()


    def drawKeyboard(self):
        global wordGuesses

        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
                         'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alphabetEnu = dict((c, i) for i, c in enumerate(self.alphabet))

        self.frameRows = []
        self.alphabetButtons = []

        self.letterNum = 0

        for f in range(4):
            self.frameRows.append(tk.Frame(self.rightFrame))
            self.frameRows[f].pack(side = "top", fill = "both")
            for l in range(7):
                try:
                    letter = self.alphabet[self.letterNum]
                    self.alphabetButtons.append(tk.Button(self.frameRows[f], text = letter, font = self.controller.buttonFont,
                                                     relief = "groove", command = lambda letter = letter: self.enterLetter(letter)))
                    self.alphabetButtons[self.letterNum].pack(side = "left", fill = "both", expand = True, padx = 1, pady = 1)    
                    self.letterNum += 1 
                except IndexError:
                    break

        self.guessLabel = tk.Label(self.rightFrame, text = wordGuesses, font = self.controller.textFont)
        self.guessLabel.pack(side = "top", pady = 50)
    
    def drawHangman(self):
        if self.hangmanLevel != 4 and self.hangmanLevel != 5:
            self.hangmanParts.append(self.canvas1.create_line(self.hanCoords[self.hangmanLevel][0], self.hanCoords[self.hangmanLevel][1], 
                                     self.hanCoords[self.hangmanLevel][2], self.hanCoords[self.hangmanLevel][3], width = self.hanWidth))
        elif self.hangmanLevel == 4:
            self.hangmanParts.append(self.canvas1.create_line(self.hanCoords[self.hangmanLevel][0], self.hanCoords[self.hangmanLevel][1], 
                                     self.hanCoords[self.hangmanLevel][2], self.hanCoords[self.hangmanLevel][3], width = self.hanWidth - 2, dash = 4))
        elif self.hangmanLevel == 5:
            self.hangmanParts.append(self.canvas1.create_oval(self.hanCoords[self.hangmanLevel][0], self.hanCoords[self.hangmanLevel][1], 
                                     self.hanCoords[self.hangmanLevel][2], self.hanCoords[self.hangmanLevel][3], width = self.hanWidth - 1))
        self.hangmanLevel += 1
        

    def enterLetter(self, letter):
        global wordGuesses, lives, wordSplit, guesses

        self.letterCode = self.alphabetEnu[letter]
        self.alphabetButtons[self.letterCode].config(state = "disabled")

        self.wordGuess, self.guessState = userGuess(letter)

        if self.guessState == "incorrect":
            self.drawHangman()
            lives -= 1
        
        else:
            self.guessLabel.configure(text = wordGuesses)
        
        if lives <= 0:
            self.controller.makeresultFrame("deathScreen")
            lives = 11
            guesses = 0
        
        if wordSplit == wordGuesses:
            self.controller.makeresultFrame("winScreen")
            lives = 11
            guesses = 0
    

class deathScreen(tk.Frame):
    def __init__(self, parent, controller):
        global word

        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.lossLabel = tk.Label(self, text = "You lose!", font = self.controller.resultFont)
        self.lossLabel.pack(side = "top", pady = 30)

        self.wordLabel = tk.Label(self, text = f"The word was '{word}'", font = self.controller.textFont, fg = "#427787")
        self.wordLabel.pack(side = "top", pady = 15)

        self.guessLabel = tk.Label(self, text = f"You took {guesses} guesses", font = self.controller.textFont, fg = "#427787")
        self.guessLabel.pack(side = "top", pady = 15)

        self.continueButton = tk.Button(self, text = "Continue", font = self.controller.buttonFont, command = lambda: self.controller.showFrame("optionScreen"))
        self.continueButton.pack(side = "top", expand = True)

class winScreen(tk.Frame):
    def __init__(self, parent, controller):
        global word, guesses

        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.winLabel = tk.Label(self, text = "You win!", font = self.controller.resultFont)
        self.winLabel.pack(side = "top", pady = 30)

        self.wordLabel = tk.Label(self, text = f"The word was '{word}'", font = self.controller.textFont, fg = "#427787")
        self.wordLabel.pack(side = "top", pady = 15)

        self.guessLabel = tk.Label(self, text = f"It took you {guesses} guesses", font = self.controller.textFont, fg = "#427787")
        self.guessLabel.pack(side = "top", pady = 15)

        self.continueButton = tk.Button(self, text = "Continue", font = self.controller.buttonFont, command = lambda: self.controller.showFrame("optionScreen"))
        self.continueButton.pack(side = "top", expand = True)



#---Game Logic---#

word = ""
wordSplit = []
wordGuesses = []

lives = 11
guesses = 0

def userGuess(letter):
    global wordSplit, wordGuesses, guesses

    guesses += 1

    state = "incorrect"

    for l in range(len(wordSplit)):
        if  letter.lower() == wordSplit[l].lower():
            wordGuesses[l] = wordSplit[l]

            state = "correct"
    

    return wordGuesses, state

def pickbotWord(diff):
    botWord = wordPicker.pickWord(diff)
    return botWord

def setWord(newWord):
    global word, wordSplit, wordGuesses

    word = newWord
    wordSplit = [c for c in word]
    wordGuesses = ["_" for c in wordSplit]


if __name__ == "__main__":
    app = Application()
    app.mainloop()