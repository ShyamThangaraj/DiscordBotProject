import keep_alive
import random
import os
import discord #imports discord library
import json
import requests
import time
from datetime import datetime
import pytz
import math
from PIL import Image

intents = discord.Intents.all()
client = discord.Client(intents=intents)


client = discord.Client(intents=intents)
#client = discord.Client() #creates a client object named client


rpsWins = 0
rpsLosses = 0
rpsTies = 0
Letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * - + = ~ ? : ; < >"
RobotCharacterChoice = Letters.split(" ")
RobotCharacter = random.choice(RobotCharacterChoice)
Character = " "
TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
RobotSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def TrigIntro():
  return("```Hi! Welcome to Scaltron's trigonometric functions calculator! (All answers will be in radians)``` ```Please enter one of the follow commands: \n Sin(x): '!scaltronSin(num)' \n Cos(x): '!scaltronCos(num' \n Tan(x): '!scaltronTan(num)'  \n ArcSin(x): '!scaltronAsin(num)' \n ArcCos(x): '!scaltronAcos(num)' \n ArcTan(x): '!scaltronAtan(num)'```")

def calcIntro():
  return("```Hi! Welcome to Scaltron's calculator experience!``` ```Please enter one of the following commands: \n To add: '!scaltronAdd(3, 56)' \n To subtract: '!scaltronSubtract(100, 3)' \n To multiply: '!scaltronMultiply(5, 7, 54, 3)' \n To divide: '!scaltronDivide(5876, 5, 67)' \n To apply an exponent to a number: '!scaltronExp(num, exponent)' \n To square root: '!scaltronSqrt(num)' \n To explore trig functions: '!scaltronTrig'```")

def AddCalc(equation):
  equationInt = equation.split(", ")
  Sum = 0
  for char in equationInt:
    Sum = Sum + float(char)
  return(str(round(Sum, 2)))

def SubtractCalc(equation):
  equationInt = equation.split(", ")
  equationIntReal = []
  for char in equationInt:
    equationIntReal.append(float(char))
  Subtraction = equationIntReal[0]
  equationIntReal.remove(Subtraction)
  for char in equationIntReal:
    Subtraction -= float(char)
    Subtraction = round(Subtraction, 2)
  return(str(Subtraction))

def MultiplyCalc(equation):
  equationInt = equation.split(", ")
  equationIntReal = []
  for char in equationInt:
    equationIntReal.append(float(char))
  Multiplication = equationIntReal[0]
  equationIntReal.remove(Multiplication)
  for char in equationIntReal:
    Multiplication = Multiplication * float(char)
  Multiplication = round(Multiplication, 2)
  return(str(Multiplication))

def DivideCalc(equation):
  equationInt = equation.split(", ")
  equationIntReal = []
  for char in equationInt:
    equationIntReal.append(float(char))
  Division = equationIntReal[0]
  equationIntReal.remove(Division)
  for char in equationIntReal:
    Division = Division / float(char)
  DivisionRound = round(Division, 3)
  return(str(DivisionRound))

def Exponent(equation):
  equationInt = equation.split(", ")
  equationIntReal = []
  for char in equationInt:
    equationIntReal.append(float(char))
  return(str(equationIntReal[0]) + " to the power of " + str(equationIntReal[1]) + " is --> " + str(round(equationIntReal[0]**equationIntReal[1], 2)))



def Alarm(Hours, Minutes):
  timeZone = pytz.timezone("US/Pacific")
  while True:
    if int(Hours) == int(datetime.now(timeZone).hour) and int(Minutes) == int(datetime.now(timeZone).minute):
      now = datetime.now(timeZone)
      current_time = now.strftime("%H:%M:%S")
      return("It's (" + str(current_time) + ") Time to ")


def CheckWinnerTrue():
  global TicTacToeBoard
  global RobotCharacter
  global Character
  global RobotSpots
  if RobotCharacter == checkWinner(TicTacToeBoard):
    Character = " "
    TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    RobotSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    RobotCharacter = random.choice(RobotCharacterChoice)
    return "V"
  elif Character == checkWinner(TicTacToeBoard):
    Character = " "
    TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    RobotSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    RobotCharacter = random.choice(RobotCharacterChoice)
    return "F"

def allSame(str1, str2, str3):
  return str1==str2==str3 and str1!="-"

def checkWinner(TicTacToeBoard):
  if(allSame(TicTacToeBoard[0],TicTacToeBoard[1],TicTacToeBoard[2])):
    return TicTacToeBoard[0]
  elif(allSame(TicTacToeBoard[3],TicTacToeBoard[4],TicTacToeBoard[5])):
    return TicTacToeBoard[3]
  elif(allSame(TicTacToeBoard[6],TicTacToeBoard[7],TicTacToeBoard[8])):
    return TicTacToeBoard[6]
  elif(allSame(TicTacToeBoard[0],TicTacToeBoard[3],TicTacToeBoard[6])):
    return TicTacToeBoard[0]
  elif(allSame(TicTacToeBoard[1],TicTacToeBoard[4],TicTacToeBoard[7])):
    return TicTacToeBoard[1]
  elif(allSame(TicTacToeBoard[2],TicTacToeBoard[5],TicTacToeBoard[8])):
    return TicTacToeBoard[2]
  elif(allSame(TicTacToeBoard[0],TicTacToeBoard[4],TicTacToeBoard[8])):
    return TicTacToeBoard[0]
  elif(allSame(TicTacToeBoard[2],TicTacToeBoard[4],TicTacToeBoard[6])):
    return TicTacToeBoard[2]
  else:
    return False


def GameOver(TicTacToeBoard):
  if(allSame(TicTacToeBoard[0],TicTacToeBoard[1],TicTacToeBoard[2])):
    return True
  elif(allSame(TicTacToeBoard[3],TicTacToeBoard[4],TicTacToeBoard[5])):
    return True
  elif(allSame(TicTacToeBoard[6],TicTacToeBoard[7],TicTacToeBoard[8])):
    return True
  elif(allSame(TicTacToeBoard[0],TicTacToeBoard[3],TicTacToeBoard[6])):
    return True
  elif(allSame(TicTacToeBoard[1],TicTacToeBoard[4],TicTacToeBoard[7])):
    return True
  elif(allSame(TicTacToeBoard[2],TicTacToeBoard[5],TicTacToeBoard[8])):
    return True
  elif(allSame(TicTacToeBoard[0],TicTacToeBoard[4],TicTacToeBoard[8])):
    return True
  elif(allSame(TicTacToeBoard[2],TicTacToeBoard[4],TicTacToeBoard[6])):
    return True
  else:
    return False


def PrintTicTacToe(TicTacToeBoard):
  #TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
  BoardFormatted = "```"
  for i in range(9):
    if i%3 == 0 and i>0:
      BoardFormatted += "\n---------------------------------\n|   " + TicTacToeBoard[i] + "   |   "
    else:
      BoardFormatted += "|   "  + TicTacToeBoard[i] + "   |   "
  return(BoardFormatted + "```")


def TicTacToeIntro():
  TicTacToeBoardIntro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  Example = PrintTicTacToe(TicTacToeBoardIntro)
  return("```Welcome! to Scaltron's Tic Tac Toe experience! \n Game Information --> \n 1. First of all you will be battling against Scaltron's most powerful bot! \n 2. You will be getting the first turn!  \n 3. Choose a spot when it's your turn (spot numbers are shown below) \n 4. To choose your spot --> Enter !scaltronTTTS(spot number) \n 5. Don't sweat it! and have fun!``` \n" + Example)

def ChangeSpot(Spot, Character):
  CorrectSpot = int(Spot) - 1
  global TicTacToeBoard
  TicTacToeBoard[CorrectSpot] = Character

def RobotTurn(CharacterRobot):
  global TicTacToeBoard
  global RobotSpots
  SpotChoice = random.choice(RobotSpots)
  RobotSpots.remove(SpotChoice)
  TicTacToeBoard[SpotChoice-1] = CharacterRobot

def TieChecker(TicTacToeBoard):
  if TicTacToeBoard[0]!="-" and TicTacToeBoard[1]!="-" and TicTacToeBoard[2]!="-" and TicTacToeBoard[3]!="-" and TicTacToeBoard[4]!="-" and TicTacToeBoard[5]!="-" and TicTacToeBoard[6]!="-" and TicTacToeBoard[7]!="-" and TicTacToeBoard[8]!="-" and not GameOver(TicTacToeBoard):
    return True
  else:
    return False

def timer(sec):
  for i in range(sec):
    time.sleep(1)
  return(" It's time to ")


def GuessIt():
  response = requests.get("https://w0.peakpx.com/wallpaper/123/54/HD-wallpaper-scenery-lake-nature-sky-tree-water.jpg")
  left = 0
  top = 50
  right = 510
  bottom = 292
  print(response)
  img_res = response.crop((left, top, right, bottom)) 
  return(img_res)


def getWeather(zipcode):
  my_secret = os.environ['WeatherAPI']

  url = "https://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + ",&appid=" + my_secret

  req = requests.get(url)

  jsonData = req.json()

  temp=jsonData["main"]["temp"]
  
  #Kelvins into Fahrenheit degrees is (K − 273.15) × 9/5 + 32 = °F.
  
  
  tempf = ((temp) - 273.15) * (9/5) + 32.0
  tempfrounded = round(tempf,2) 

  description = jsonData["weather"][0]["description"]


  
  return str(tempfrounded) + " degrees and it's " + description



def RPS(pChoice):
  global rpsWins, rpsLosses, rpsTies
  rpsList = ["rock", "paper", "scissors"]
  botChoice = random.choice(rpsList)
  if pChoice == botChoice:
    rpsTies+=1
    return "Tie!!! \n" + str(rpsWins) + "-" + str(rpsLosses) + "-" + str(rpsTies)
  else: #someone won
    if pChoice == "rock":
      if botChoice=="scissors":
        rpsWins+=1
        return "You win!, 🗿 beats ✂" + "\n" + str(rpsWins) + "-" + str(rpsLosses) + "-" + str(rpsTies)
      else:
        rpsLosses +=1
        return "You lose, 🗿 loses to 📄" + "\n" + str(rpsWins) + "-" + str(rpsLosses) + "-" + str(rpsTies)
    elif pChoice=="paper":
      if botChoice == "rock":
        rpsWins+=1
        return "You win!, 📄 beats 🗿" + "\n" + str(rpsWins) + "-" + str(rpsLosses) + "-" + str(rpsTies)
      else:
        rpsLosses +=1
        return "You lose, 📄 loses to ✂" + "\n" + str(rpsWins) + "-" + str(rpsLosses) + "-" + str(rpsTies)
    elif pChoice == "scissors":
      if botChoice == "paper":
        rpsWins+=1
        return "You win, ✂ beats 📄" + "\n" + str(rpsWins) + "-" + str(rpsLosses) + "-" + str(rpsTies)
      else:
        rpsLosses +=1
        return "You lose, ✂ loses to 🗿" + "\n" + str(rpsWins) + "-" + str(rpsLosses) + "-" + str(rpsTies)

ClashRoyaleCharacters = ["https://www.seekpng.com/png/detail/31-313562_enter-ammount-of-gold-prince-from-clash-royale.png", "https://cdnb.artstation.com/p/assets/images/images/041/900/891/large/ocellus-services-skeletonarmy-zoom.jpg?1633012193&dl=1", "https://d.newsweek.com/en/full/895534/clash-royale-balance-changes-2018-april-barbarian-barrel-update-lightning-dark-prince.png?w=790&f=36971af0248ffafb787d09f22f809074", "https://external-preview.redd.it/4wFwL4A7eBgLe3qEaCbQyzjIOMqlRG4rEPksRYHLLEw.png?auto=webp&s=98a3c63f7b5316df155dd2499a56ccd1413b70f4", "https://i1.wp.com/clashroyalekingdom.com/wp-content/uploads/2017/11/Kingdoms-File-Inferno-Tower-Clash-Royale-Kingdom.jpg?fit=1024%2C533&ssl=1", "https://i.redd.it/1vfw2cdlr8871.jpg", "https://static.wikia.nocookie.net/clashofclans/images/3/35/Giant_info.png/revision/latest/scale-to-width-down/500?cb=20170927232347", "https://www.seekpng.com/png/detail/36-361810_barbarians-png-clash-royale-barbarians-png.png", "https://static.wikia.nocookie.net/clashofclans/images/5/54/P.E.K.K.A_info.png/revision/latest?cb=20170927230947", "https://cdnb.artstation.com/p/assets/covers/images/038/649/051/large/ocellus-art-amp-production-services-ocellus-art-amp-production-services-wizard-thumbnails.jpg?1623685302", "https://preview.redd.it/tu1oidicy7uy.png?auto=webp&s=ed3790ecf54887c12a119666f732b025aed7c406", "https://c4.wallpaperflare.com/wallpaper/305/589/67/hog-rider-clash-of-clans-supercell-games-wallpaper-thumb.jpg", "https://i.imgur.com/uU3Ue81.png", "http://i.imgur.com/Qe0cI8v.png", "https://external-preview.redd.it/DDN0FuQ5LI9Xz1EsCsc02JIPYHU1AdkAgio9T_TkCDY.png?auto=webp&s=04235f90ddd47eba9df3011851a4512474c2d11b", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5a6af839-076e-448b-b7e8-47dcfb1f1af3/d9q4dm3-041c88c2-5738-463b-93de-02d9e8deb4e3.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzVhNmFmODM5LTA3NmUtNDQ4Yi1iN2U4LTQ3ZGNmYjFmMWFmM1wvZDlxNGRtMy0wNDFjODhjMi01NzM4LTQ2M2ItOTNkZS0wMmQ5ZThkZWI0ZTMuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.inrWF_XB88c7Kh8mBNKMyMpUuohle2wxtI9OvtnbHuY", "https://cdnb.artstation.com/p/assets/covers/images/036/488/991/large/ocellus-art-amp-production-services-ocellus-art-amp-production-services-icewizard-thumbnails.jpg?1617809314", "https://static.wikia.nocookie.net/clashroyale/images/f/ff/Infero_dragon.jpg/revision/latest?cb=20200612094318", "https://static.wikia.nocookie.net/clashofclans/images/c/c2/Golem_info.png/revision/latest/scale-to-width-down/500?cb=20170927231256", "https://wallpapercave.com/wp/wp2310024.jpg", "https://cdna.artstation.com/p/assets/images/images/030/835/470/4k/brice-laville-saint-martin-electro-giant-006.jpg?1601815481", "https://cdn.wallpapersafari.com/34/76/PTsCIF.jpg", "https://preview.redd.it/1t3ef3m1fc141.jpg?auto=webp&s=f29a42cfb7c1f6cb587a7d12c6ecf57723fb7a5e", "https://cdna.artstation.com/p/assets/images/images/021/057/352/4k/brice-laville-saint-martin-elixir-golem-05.jpg?1570210900&dl=1", "https://cdna.artstation.com/p/assets/covers/images/034/237/032/medium/ocellus-art-amp-production-services-ocellus-art-amp-production-services-lumberjack-project-cover.jpg?1611765908", "https://cdna.artstation.com/p/assets/covers/images/043/644/558/smaller_square/ocellus-services-ocellus-services-skeletonking-thumbnails.jpg?1637851529", "https://cdna.artstation.com/p/assets/covers/images/043/547/056/large/ocellus-services-ocellus-services-archerqueen-thumbnails.jpg?1637596425", "https://cdna.artstation.com/p/assets/images/images/043/832/038/large/ocellus-services-goldenknight-uipose.jpg?1638373830"]

vids = ["https://www.youtube.com/watch?v=XmtXC_n6X6Q", "https://www.youtube.com/watch?v=um2Q9aUecy0", "https://www.youtube.com/watch?v=9FqwhW0B3tY", "https://www.youtube.com/watch?v=GfO-3Oir-qM", "https://www.youtube.com/watch?v=r9PeYPHdpNo", "https://www.youtube.com/watch?v=JkaxUblCGz0", "https://www.youtube.com/watch?v=R2DU85qLfJQ", "https://www.youtube.com/watch?v=cTQ3Ko9ZKg8", "https://www.youtube.com/watch?v=LuH-6VhD12s", "https://www.youtube.com/watch?v=gZKhP1bUTnk", "https://www.youtube.com/watch?v=7F6t1Az2SGU", "https://www.youtube.com/watch?v=0yydrU7TCbk", "https://www.youtube.com/watch?v=rjPRPiBoSJM", "https://www.youtube.com/watch?v=LBjv5Le2KqY", "https://www.youtube.com/watch?v=XdXgs-kxxFU", "https://www.youtube.com/watch?v=O4LXW2rPN64", "https://www.youtube.com/watch?v=xViXR2I65nI"]

QuoteList = ["What’s the best thing about Switzerland? -- I don’t know, but the flag is a big plus.", "Did you hear about the mathematician who’s afraid of negative numbers -- He’ll stop at nothing to avoid them.", "Hear about the new restaurant called Karma? -- There’s no menu: You get what you deserve.", "Why don’t scientists trust atoms? -- Because they make up everything.", "Where are average things manufactured? -- The satisfactory.", "A man tells his doctor, Doc, help me. I’m addicted to Twitter! -- The doctor replies, Sorry, I don’t follow you …", "What do you call a fake noodle? -- An impasta.", "Why did the frog take the bus to work today? -- His car got toad away.", "The numbers 19 and 20 got into a fight. -- 21.", "Why did it get so hot in the baseball stadium after the game? -- All of the fans left.", "I have a fear of speed bumps. -- But I am slowly getting over it."]

@client.event 
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(msg): #msg is the parameter
  if msg.author==client.user:
    return
  if msg.content == ("!scaltronHelp"):
    await msg.channel.send(">>> ```!scaltronJokes --> Random jokes```  ```!scaltronActivities --> Activities to do when bored (using APIs)```  ```!scaltronClashRoyalePic --> Random Clash Royale pictures```  ```!scaltronGreet Your-name-here --> To chat with scaltron's bot```  ```!scaltronVids --> Interesting documentaries/videos```  ```!scaltronRPS --> Play rock, paper, scissors!```  ```!scaltronHello --> Say hello```  ```!scaltronEncryptYour-message-here --> Encrypt a message```  ```!scaltronDecryptYour-message-here --> Decrypt an encrypted message```  ```!scaltronWeatherYour-zipcode-here (Don't seperate zipcode with a space) --> Get the weather information with a zipcode```  ```!scaltronTimer(00:00)'Your task' --> To start a timer  --> Ex. format: !scaltronTimer(05:07)'start homework'  --> (00:00) --> (mins, secs) ```  ```!scaltronAlarm(00:00)'Your Task' --> To start an alarm (PST)  --> (Ex. format: !scaltronAlarm(18:41)'Do Homework' --> (00:00) --> (Hour, Minute) Note: 24 hrs. format``` ```!scaltronCurrentTime --> Get current time in PST``` \n ```!scaltronCalc --> To activate the calculator``` \n ```!scaltronTTT --> To play Tic Tac Toe with Scaltron's most powerful bot!```")
  
  if msg.content == ("!scaltronJokes"):
    await msg.channel.send(random.choice(QuoteList))
  if msg.content==("!scaltronHello"):
    await msg.channel.send("Hello from scaltronMC!")
  if msg.content==("!scaltronClashRoyalePic"):
    await msg.channel.send(random.choice(ClashRoyaleCharacters))
  if msg.content[:14] == ("!scaltronGreet"):
    name = msg.content[15:]
    await msg.channel.send("Greetings " + name + ", hope you are doing well :)")  
  if msg.content==("!scaltronFacts"):
    await msg.channel.send("Nathan is bad \n Nehum is bald")  
  if msg.content.startswith("Happy birthday Scaltron's bot"):
    await msg.channel.send(msg.author.mention + " Thank you for remembering my birthday, I love potatoes")
  if msg.content==("!scaltronVids"):
    await msg.channel.send(random.choice(vids))
  if msg.content.startswith("!scaltronEncrypt"):
    length = len("!scaltronEncrypt")
    Message = msg.content[length:]
    EncMsg = ""
    for char in Message:
      newChar = ord(char) + 1
      EncMsg += chr(newChar)
    await msg.channel.send("Encrypted message --> " + EncMsg)
  if msg.content.startswith("!scaltronDecrypt"):
    length1 = len("!scaltronDecrypt")
    Message1 = msg.content[length1:]
    DecMsg = ""
    for char in Message1:
      newChar1 = ord(char) - 1
      DecMsg += chr(newChar1)
    await msg.channel.send("Decrypted Messsage --> " + DecMsg)
  if msg.content.startswith("!scaltronWeather"):
    length=len("!scaltronWeather")
    zipcode = msg.content[length:]
    response = getWeather(zipcode)
    await msg.channel.send(response)
  if msg.content.startswith("!scaltronRPS"):
    resp= "Lets play 🗿📄✂: Choose '!scaltronRock', '!scaltronPaper', '!scaltronScissors'"
    await msg.channel.send(resp)
  if msg.content.startswith("!scaltronRock"):
    await msg.channel.send(RPS("rock"))
  elif msg.content.startswith("!scaltronPaper"):
    await msg.channel.send(RPS("paper"))
  elif msg.content.startswith("!scaltronScissors"):
    await msg.channel.send(RPS("scissors"))
  if msg.content.startswith("!scaltronTimer"):
    Minutes = int(msg.content[15:17])
    Minutes = Minutes*60
    Seconds = int(msg.content[18:20])
    TotalTime = Minutes + Seconds
    reminder = msg.content[21:]
    reminder = reminder.replace("'", "")
    await msg.channel.send(msg.author.mention + " your timer is officially running!")
    response = timer(TotalTime)
    await msg.channel.send(msg.author.mention + response + reminder + "!")
  if msg.content.startswith("!scaltronCurrentTime"):
    timeZone = pytz.timezone("US/Pacific")
    now = datetime.now(timeZone)
    current_time = now.strftime("%H:%M:%S")
    await msg.channel.send("It's (" + str(current_time) + ") PST 24 hrs. format ")
  if msg.content.startswith("!scaltronAlarm"):
    length = len(msg.content)
    Activity = msg.content[22:length-1]
    Hour = msg.content[15:17]
    Minutes = msg.content[18:20]
    if int(Hour) > 23:
      await msg.channel.send("You can't have hours greater than 23! for 12am input (00) Please try again!")
    if int(Minutes) > 60:
      await msg.channel.send("You can't have minutes greater than 60! Please try again!")
    if int(Hour) <= 23 and int(Minutes) <= 60:
      await msg.channel.send(msg.author.mention + " Your alarm is officially on!")
      Response = Alarm(Hour, Minutes)
      await msg.channel.send(msg.author.mention + Response + Activity + "!")
  if msg.content.startswith("!scaltronCalc"):
    await msg.channel.send(calcIntro())
  if msg.content.startswith("!scaltronAdd"):
    length = len("!scaltronAdd(")
    Equation = msg.content[length: len(msg.content)-1]
    await msg.channel.send("The sum of " + str(Equation) + " --> " + AddCalc(Equation))
  if msg.content.startswith("!scaltronSubtract"):
    length = len("!scaltronSubtract(")
    Equation = msg.content[length: len(msg.content)-1]
    await msg.channel.send("The subtraction of " + str(Equation) + " --> " + SubtractCalc(Equation))
  if msg.content.startswith("!scaltronDivide"):
    length = len("!scaltronDivide(")
    Equation = msg.content[length: len(msg.content)-1]
    await msg.channel.send("The division of " + str(Equation) + " --> " + DivideCalc(Equation))
  if msg.content.startswith("!scaltronMultiply"):
    length = len("!scaltronMultiply(")
    Equation = msg.content[length: len(msg.content)-1]
    await msg.channel.send("The multiplication of " + str(Equation) + " --> " + MultiplyCalc(Equation))
  if msg.content.startswith("!scaltronExp"):
    length = len("!scaltronExp(")
    Equation = msg.content[length: len(msg.content)-1]
    await msg.channel.send(Exponent(Equation))
  if msg.content.startswith("!scaltronSqrt"):
    length = len("!scaltronSqrt(")
    Num = msg.content[length: len(msg.content)-1]
    Sqrt = round(math.sqrt(int(Num)), 4)
    await msg.channel.send("The square root of " + Num + " is --> " + str(Sqrt))
  if msg.content.startswith("!scaltronTrig"):
    await msg.channel.send(TrigIntro())
  if msg.content.startswith("!scaltronSin"):
    length = len("!scaltronSin(")
    Num = msg.content[length: len(msg.content)-1]
    Answer = math.sin(float(Num))
    Answer = round(Answer, 5)
    await msg.channel.send("The sine of " + str(Num) + " is --> " + str(Answer))
  if msg.content.startswith("!scaltronCos"):
    length = len("!scaltronCos(")
    Num = msg.content[length: len(msg.content)-1]
    Answer = math.cos(float(Num))
    Answer = round(Answer, 5)
    await msg.channel.send("The cosine of " + str(Num) + " is --> " + str(Answer))
  if msg.content.startswith("!scaltronTan"):
    length = len("!scaltronTan(")
    Num = msg.content[length: len(msg.content)-1]
    Answer = math.tan(float(Num))
    Answer = round(Answer, 5)
    await msg.channel.send("The tangent of " + str(Num) + " is --> " + str(Answer))
  if msg.content.startswith("!scaltronAcos"):
    length = len("!scaltronAcos(")
    Num = msg.content[length: len(msg.content)-1]
    Answer = math.acos(float(Num))
    Answer = round(Answer, 5)
    await msg.channel.send("The arc cosine of " + str(Num) + " is --> " + str(Answer))
  if msg.content.startswith("!scaltronAsin"):
    length = len("!scaltronAsin(")
    Num = msg.content[length: len(msg.content)-1]
    Answer = math.asin(float(Num))
    Answer = round(Answer, 5)
    await msg.channel.send("The arc sine of " + str(Num) + " is --> " + str(Answer))
  if msg.content.startswith("!scaltronAtan"):
    length = len("!scaltronAtan(")
    Num = msg.content[length: len(msg.content)-1]
    Answer = math.atan(float(Num))
    Answer = round(Answer, 5)
    await msg.channel.send("The arc tangent of " + str(Num) + " is --> " + str(Answer))
  if msg.content.startswith("!scaltronGuessIt"):
    await msg.channel.send(GuessIt())
  if msg.content.startswith("!scaltronTTT"):
    global RobotCharacter
    global Character
    global TicTacToeBoard
    global RobotSpots
    for i in range(1):
      if msg.content == "!scaltronTTT":
        await msg.channel.send("Hi! " + msg.author.mention + " it's time for...")
        await msg.channel.send("https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Tic_tac_toe.svg/1200px-Tic_tac_toe.svg.png")
        await msg.channel.send(TicTacToeIntro())
        time.sleep(5)
        await msg.channel.send("```To start please choose your character --> '!scaltronTTT(Your character here(not an emoji))'```")
      if msg.content.startswith("!scaltronTTT("):
        Length = len("!scaltronTTT(")
        Character = msg.content[Length: len(msg.content)-1]
        await msg.channel.send("```Thank you for choosing your character! \nStart the game by entering !scaltronTTTS(spot number) --> Spot# should be between 1-9```")
        await msg.channel.send("```Scaltron's bot chose '" + RobotCharacter + "'```")
      if msg.content.startswith("!scaltronTTTS("):
        if not GameOver(TicTacToeBoard):
          Length = len("!scaltronTTTS(")
          SpotNumber = msg.content[Length: len(msg.content)-1]
          if int(SpotNumber) not in RobotSpots:
            await msg.channel.send("```Hmm... \nSeems like that spot has occupied!\nPlease enter a new spot...```")
            break
          RobotSpots.remove(int(SpotNumber))
          ChangeSpot(SpotNumber, Character)
          BoardChangedPrinted = PrintTicTacToe(TicTacToeBoard)
          await msg.channel.send("Current Board --> \n")
          await msg.channel.send(BoardChangedPrinted)
        if GameOver(TicTacToeBoard):
          if CheckWinnerTrue() == "F":
            await msg.channel.send("```There is a winner...\nCalculating...\nPlease stand by...```")
            time.sleep(3)
            await msg.channel.send("```Results are in...```")
            time.sleep(1)
            await msg.channel.send("```You have defeated Scaltron's bot!\nYou have achieved greatness...\nEnjoy your victory...\nThanks for playing Tic Tac Toe!\nEnter '!scaltronTTT' to play again!```")
            break
        if TieChecker(TicTacToeBoard):
          await msg.channel.send("```The game board is full...\nCalculating...\nPlease stand by...```")
          time.sleep(2)
          await msg.channel.send("```Results are in...```")
          time.sleep(1)
          await msg.channel.send("```You and Scaltron's bot are tied!\nBoth of you are equally matched...\nAnother battle is required to determine who is better...\nBetter luck next time...\nThanks for playing Tic Tac Toe!\nEnter '!scaltronTTT' to rematch another game with Scaltron's bot!```")
          Character = " "
          TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
          RobotSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
          RobotCharacter = random.choice(RobotCharacterChoice)
          break
        if not GameOver(TicTacToeBoard):
          RobotTurn(RobotCharacter)
          await msg.channel.send("Scaltron's bot is thinking...")
          time.sleep(1)
          BoardChangedPrinted = PrintTicTacToe(TicTacToeBoard)
          await msg.channel.send("Current Board --> \n")
          await msg.channel.send(BoardChangedPrinted)
        if GameOver(TicTacToeBoard):
          if CheckWinnerTrue() == "V":
            await msg.channel.send("```There is a winner...\nCalculating...\nPlease stand by...```")
            time.sleep(3)
            await msg.channel.send("```Results are in...```")
            time.sleep(1)
            await msg.channel.send("```You have been destroyed by Scaltron's bot!\nYou have failed to do your duty...\nBetter luck next time...\nThanks for playing Tic Tac Toe!\nEnter '!scaltronTTT' to play again!```")
            break
        if TieChecker(TicTacToeBoard):
            await msg.channel.send("```The game board is full...\nCalculating...\nPlease stand by...```")
            time.sleep(2)
            await msg.channel.send("```Results are in...```")
            time.sleep(1)
            await msg.channel.send("```You and Scaltron's bot are tied!\nBoth of you are equally matched...\nAnother battle is required to determine who is better...\nBetter luck next time...\nThanks for playing Tic Tac Toe!\nEnter '!scaltronTTT' to rematch another game with Scaltron's bot!```")
            Character = " "
            TicTacToeBoard = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
            RobotSpots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            RobotCharacter = random.choice(RobotCharacterChoice)
            break

keep_alive.keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)