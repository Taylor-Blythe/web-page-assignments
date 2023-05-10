import turtle as t
b = t.Turtle()
wn = t.Screen()
t.speed(0)
t.hideturtle()
t.Screen().bgcolor("black")
fontSetUp = ("Times New Roman",30,"normal")
fontSetUp2 = ("Times New Roman",80,"normal")
fontSetUP3 =  ("Times New Roman",0.5,"normal")
# writer = t.Turtle()
# writer.color("red")
# writer.penup()
# writer.goto(-160,210)
# writer.hideturtle()
circle = t.Turtle(shape="circle")
circle.shapesize(8)
circle.color("blue")
start = t.Turtle()
start.speed(0)
start.color("green")
start.shape("square")
start.penup()
start.goto(-120,140)
directions = t.Turtle()
directions.speed(0)
directions.color("yellow")
directions.shape("square")
directions.penup()
directions.goto(-120,180)

def draw_circle(x,y,r,color):
    t.speed(0)
    t.hideturtle()
    t.up()
    t.goto(x,y-r)
    t.seth(0)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r,360,150)
    t.end_fill()


# writer.fillcolor("red")
def writer1():
    writer = t.Turtle()
    writer.speed(0)
    writer.color("red")
    writer.penup()
    writer.goto(-200,210)
    writer.pendown()
    writer.write(" Connect 4! " , font=fontSetUp2)
    writer.penup()
    writer.goto(-300,-250)
    writer.pendown()
    writer.write("Created By: Charity Baylor and Taylor Blythe", font=fontSetUp)
    writer.penup()
    writer.goto(-110,160)
    writer.pendown()
    writer.write("Directions", font=fontSetUp)
    writer.penup()
    writer.goto(-110,120)
    writer.pendown()
    writer.write("Play", font=fontSetUp)
    writer.hideturtle()
def blueCircle():
    circle.penup()
    circle.goto(-10,-10)
    circle.pendown()
    circle.fillcolor("blue")
    circle.stamp()
    circle.penup()
    circle.goto(80,-10)
    circle.pendown()
    circle.fillcolor("red")
    circle.stamp()
def clearScreen():
    wn.clearscreen()
    t.Screen().bgcolor("black")
b.color("black")
b.speed(0)
def board():
  b.penup()
  b.goto(-300,300)
  b.pendown()
  b.color("blue")
  b.begin_fill()
  b.forward(700)
  b.setheading(270)
  b.forward(525)
  b.setheading(180)
  b.forward(700)
  b.setheading(90)
  b.forward(525)
  b.penup()
  b.end_fill()
#circles row 1
def row1():
  b.penup()
  b.goto(-210,240)
  b.pendown()
  b.color("white")
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-115,240)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-20,240)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.pendown()
  b.penup()
  b.goto(75,240)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(170,240)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(265,240)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(360,240)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
#row 2
def row2():
  b.penup()
  b.goto(-210,160)
  b.pendown()
  b.color("white")
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-115,160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-20,160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(75,160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(170,160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(265,160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(360,160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
def row3():
  b.penup()
  b.goto(-210,80)
  b.pendown()
  b.color("white")
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-115,80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-20,80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(75,80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(170,80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(265,80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(360,80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
def row4():
  b.penup()
  b.goto(-210,0)
  b.pendown()
  b.color("white")
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-115,0)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-20,0)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(75,0)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(170,0)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(265,0)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(360,0)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
def row5():
  b.penup()
  b.goto(-210,-80)
  b.pendown()
  b.color("white")
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-115,-80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-20,-80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(75,-80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(170,-80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(265,-80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(360,-80)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
def row6():
  b.penup()
  b.goto(-210,-160)
  b.pendown()
  b.color("white")
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-115,-160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(-20,-160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(75,-160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(170,-160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(265,-160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()
  b.penup()
  b.goto(360,-160)
  b.pendown()
  b.begin_fill()
  b.circle(30,360)
  b.end_fill()

def setupBoard():
    board = []
    for x in range(6):
        board.append([])
        for y in range(7):
            board[x].append(0)
    #printBoard(board)
    return board

def setupPlayer():
   return 1

#function to validate column
def validateMove(board, col):
    if board[0][col] != 0:
        return False
    return True 

def printBoard(board):
    for x in board:
        print(x)

#function to check for end of game
def endGame(board):
    #returns one of 4 states
    #player1 win = 1
    #player2 win = 2
    #stalemate = "draw"
    #not ended = "no"

    #vertical
    for y in range(len(board[0])):
        #print(x)
        player1counter = 0
        player2counter = 0
        for x in range(len(board)):
            #print(y)
            #print(player1counter,player2counter)
            position = board[x][y]
            if position == 1:
                #print("adding to player1")
                player1counter += 1
                player2counter = 0
                if player1counter >= 4:
                    return "p1 win"
                    b.color("white")
                    b.penup()
                    b.goto(-500,-300)
                    b.write("p1 wins", font=fontSetUp)
            elif position == 2:
                player2counter += 1
                player1counter = 0
                if player2counter >= 4:
                    return "p2 win"
                    b.write("p2 wins", font=fontSetUp)
            elif position == 0:
                player1counter = 0
                player2counter = 0


    #horizontal
    for x in board:
        #print(x)
        player1counter = 0
        player2counter = 0
        for y in x:
            #print(y)
            #print(player1counter,player2counter)
            if y == 1:
                #print("adding to player1")
                player1counter += 1
                player2counter = 0
                if player1counter >= 4:
                    return "p1 win"
                    b.write("p1 wins", font=fontSetUp)
            elif y == 2:
                player2counter += 1
                player1counter = 0
                if player2counter >= 4:
                    return "p2 win"
                    b.write("p2 wins", font=fontSetUp)
            elif y == 0:
                player1counter = 0
                player2counter = 0
    
    #diagonal
    for x in range(len(board[0])):
        player1counter = 0
        player2counter = 0
        for y in range(len(board)):
            position = board[y][x]
            if position == 1:
                player1counterur = 0
                player1counterdr = 0
                for c in range(4):
                    
                    if x+c < len(board[0]) and y-c > 0 and board[y-c][x+c] == 1:
                        player1counterur += 1
                        #print(f"x: {x+c}, y:{y-c} >", end=" ")
                        #print(f"count P1UR: {player1counterur}")
                    else:
                        player1counterur = 0
                    
                    if y+c < len(board) and x+c < len(board[0]) and board[y+c][x+c] == 1:
                        player1counterdr += 1
                        #print(f"x: {x+c}, y:{y+c} >", end=" ")
                        #print(f"count P1DR: {player1counterdr}")
                    else:
                        player1counterdr = 0
                    if player1counterur >= 4 or player1counterdr >=4:
                        return "p1 win"
                        b.write("p1 wins", font=fontSetUp)
            
            if position == 2:
                player2counterur = 0
                player2counterdr = 0
                for c in range(4):
                    
                    if x+c < len(board[0]) and y-c > 0 and board[y-c][x+c] == 2:
                        player2counterur += 1
                        #print(f"x: {x+c}, y:{y-c} >", end=" ")
                        #print(f"count P2UR: {player2counterur}")
                    else:
                        player2counterur = 0
                    
                    if y+c < len(board) and x+c < len(board[0]) and board[y+c][x+c] == 2:
                        player2counterdr += 1
                        #print(f"x: {x+c}, y:{y+c} >", end=" ")
                        #print(f"count P2DR: {player2counterdr}")
                    else:
                        player2counterdr = 0
                    
                    if player2counterur >= 4 or player2counterdr >=4:
                        return "p2 win"
                        b.write("p2 wins", font=fontSetUp)
    #stalemate
    stalemate = True
    for x in range(len(board[0])):
        for y in range(len(board)):
            if board[y][x] == 0:
                stalemate = False
                break;
    if stalemate:
        return "draw"
        b.write("draw", font=fontSetUp)

    return "ongoing"

def getRowHeight(p):
   p = (p-6) * -1
   h = -160 + 80 * p
   return h

def colSelect(x,y):
  global turn
  gameState = endGame(gameBoard)
  if gameState == "ongoing":
    if not turn == -1:
      if -270 < x < -210:
        if validateMove(gameBoard, 0):
          for p in range(len(gameBoard),-1,-1):
            if gameBoard[p-1][0] == 0:
                gameBoard[p-1][0] = (turn % 2) + 1
                if (turn % 2) + 1 == 1:
                  draw_circle(-240,getRowHeight(p),30, "black")
                  wn.update()
                else:
                  draw_circle(-240,getRowHeight(p),30, "red")
                  wn.update() 
                printBoard(gameBoard)
                turn += 1
                break;
          print("Draw move for col 1")
         
      elif -175 < x < -115:
        if validateMove(gameBoard, 1):
          for p in range(len(gameBoard),-1,-1):
            if gameBoard[p-1][1] == 0:
                gameBoard[p-1][1] = (turn % 2) + 1
                if (turn % 2) + 1 == 1:
                  draw_circle(-145,getRowHeight(p),30, "black")
                  wn.update()
                else:
                  draw_circle(-145,getRowHeight(p),30, "red")
                  wn.update()  
                printBoard(gameBoard)
                turn += 1
                break;
          print("Draw move for col 2")
      elif -80 < x < -20:
        if validateMove(gameBoard, 2):
          for p in range(len(gameBoard),-1,-1):
            if gameBoard[p-1][2] == 0:
                gameBoard[p-1][2] = (turn % 2) + 1
                if (turn % 2) + 1 == 1:
                  draw_circle(-50,getRowHeight(p),30, "black")
                  wn.update()
                else:
                  draw_circle(-50,getRowHeight(p),30, "red")
                  wn.update()  
                printBoard(gameBoard)
                turn += 1
                break;
          print("Draw move for col 3")
      elif 15 < x < 75:
        if validateMove(gameBoard, 3):
          for p in range(len(gameBoard),-1,-1):
            if gameBoard[p-1][3] == 0:
                gameBoard[p-1][3] = (turn % 2) + 1
                if (turn % 2) + 1 == 1:
                  draw_circle(45,getRowHeight(p),30, "black")
                  wn.update()
                else:
                  draw_circle(45,getRowHeight(p),30, "red")
                  wn.update()  
                printBoard(gameBoard)
                turn += 1
                break;
          print("Draw move for col 4")
      elif 110 < x < 170:
        if validateMove(gameBoard, 4):
          for p in range(len(gameBoard),-1,-1):
            if gameBoard[p-1][4] == 0:
                gameBoard[p-1][4] = (turn % 2) + 1
                if (turn % 2) + 1 == 1:
                  draw_circle(140,getRowHeight(p),30, "black")
                  wn.update()
                else:
                  draw_circle(140,getRowHeight(p),30, "red")
                  wn.update()  
                printBoard(gameBoard)
                turn += 1
                break;
          print("Draw move for col 5")
      elif 205 < x < 265:
        if validateMove(gameBoard, 5):
          for p in range(len(gameBoard),-1,-1):
            if gameBoard[p-1][5] == 0:
                gameBoard[p-1][5] = (turn % 2) + 1 
                if (turn % 2) + 1 == 1:
                  draw_circle(235,getRowHeight(p),30, "black")
                  wn.update()
                else:
                  draw_circle(235,getRowHeight(p),30, "red")
                  wn.update() 
                printBoard(gameBoard)
                turn += 1
                break;
          print("Draw move for col 6")
      elif 300 < x < 360:
        if validateMove(gameBoard, 6):
            for p in range(len(gameBoard),-1,-1):
              if gameBoard[p-1][6] == 0:
                  gameBoard[p-1][6] = (turn % 2) + 1 
                  if (turn % 2) + 1 == 1:
                    draw_circle(330,getRowHeight(p),30, "black")
                    wn.update()
                  else:
                    draw_circle(330,getRowHeight(p),30, "red")
                    wn.update() 
                  printBoard(gameBoard)
                  turn += 1
                  break;
            print("Draw move for col 7")
  
      print(endGame(gameBoard))
    else:
       turn += 1
  else:
     print("figure out how to write the end state on the screen")
gameBoard = setupBoard()
turn = -1

def game(x,y):
  clearScreen()
  board()
  row1()
  row2()
  row3()
  row4()
  row5()
  row6()
  
  wn.onclick(colSelect)
def dScreen(x,y):
   clearScreen()
   directions.penup()
   directions.goto(-750,300)
   directions.pendown()
   directions.write("First gamePlayer to connect four of their discs horizontally, vertically, or diagonally wins the game", font = fontSetUp)
   directions.penup()
   directions.goto(-325,200)
   directions.pendown()
   directions.color("blue")
   directions.write("Created by Charity Baylor and Taylor Blythe", font=fontSetUp)
   blueCircle()
   main = t.Turtle()
   main.color("yellow")
   main.shape("square")
   main.penup()
   main.goto(-150,-220)
   writes = t.Turtle()
   writes.penup()
   writes.goto(-140,-240)
   writes.pendown()
   writes.color("red")
   writes.write("Main Menu", font=fontSetUp)
  #  writes.penup()
  #  writes.goto(-150,-200)
  #  writes.pendown()
  #  writes.write("Play", font=fontSetUp)
  #  writes.hideturtle()
  #  main.write("Main M
  #  main.write("Main Menu", font=fontSetUp)
   main.onclick(mainMenu)
   start = t.Turtle()
   start.color("green")
   start.shape("square")
   start.penup()
   start.goto(-150,-160)
   start.pendown()
   writes.penup()
   writes.goto(-140,-180)
   writes.pendown()
   writes.write("Play", font=fontSetUp)
   writes.hideturtle()
   start.onclick(game)
def mainMenu(x,y):
   clearScreen()
   writer1()
   blueCircle()
   start = t.Turtle()
   start.color("green")
   start.shape("square")
   start.penup()
   start.goto(-120,140)
   start.onclick(game)
   directions = t.Turtle()
   directions.color("yellow")
   directions.shape("square")
   directions.penup()
   directions.goto(-120,180)
   directions.onclick(dScreen)
writer1()
blueCircle()
start.onclick(game)
directions.onclick(dScreen)
# directions.onclick(directionsScreen)
wn.onkeypress(writer1,"q")
wn.listen()
wn.mainloop()