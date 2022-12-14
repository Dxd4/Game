import tkinter as tk
from functools import partial
import random
import time

width = 5
height = 5
playground = [[0]*width for i in range(height)]
colors = ["#BBBBBB","#BB5555","#55BBBB","#55BB55"] # ["empty","blocked","bonus","player"]
window = tk.Tk()
window.geometry(f"{width*48}x{height*51}")
window.resizable(False, False)

def change_field(playground,x,y,number):
    colors = ["#BBBBBB","#BB5555","#55BBBB","#55BB55"]
    playground[x][y]["bg"] = colors[number]

def move(way,playground,player_field,colors):
    x, y = player_field
    if way == "up":
        if (-1<(player_field[0]-1)<width) and not (playground[x-1][y]["bg"] == colors[1]):
            change_field(playground,x-1,y,3)
            change_field(playground,x,y,0)
    elif way == "left":
        if (-1<(player_field[1]-1)<width) and not (playground[x][y-1]["bg"] == colors[1]):
            change_field(playground,x,y-1,3)
            change_field(playground,x,y,0)
    elif way == "down":
        if (-1<(player_field[0]+1)<width) and not (playground[x+1][y]["bg"] == colors[1]):
            change_field(playground,x+1,y,3)
            change_field(playground,x,y,0)
    elif way == "right":
        if (-1<(player_field[1]+1)<width) and not (playground[x][y+1]["bg"] == colors[1]):
            change_field(playground,x,y+1,3)
            change_field(playground,x,y,0)
    if find_field(playground,colors,2) == None:
        for i in range(width):
            for j in range(height):
                change_field(playground,i,j,3)
                window.update()
                time.sleep(0.1)
                


def find_field(playground,colors,number):
    for x in range(width):
        for y in range(height):
            if playground[x][y]["bg"] == colors[number]:
                return [x,y]
    return None
def chance(chance_num):
    if random.randint(0,100) <=chance_num:
        return True
    return False


def pressed(event,playground):
    player_field = find_field(playground,colors,3)
    if event.char == "w":
        move("up",playground,player_field,colors)
    elif event.char == "a":
        move("left",playground,player_field,colors)
    elif event.char == "s":
        move("down",playground,player_field,colors)
    elif event.char == "d":
        move("right",playground,player_field,colors)


def main():
    for x in range(width):
        for y in range(height):
            if (x==0 and y==0):
                playground[x][y] = (tk.Label(window,bg=colors[3],width=6,height=3))
                playground[x][y].grid(row=x,column=y)
                continue
            if chance(60):
                playground[x][y]= (tk.Label(window,bg=colors[0],width=6,height=3))
                playground[x][y].grid(row=x,column=y)
                continue
            if chance(40):
                playground[x][y]= (tk.Label(window,bg=colors[1],width=6,height=3))
                playground[x][y].grid(row=x,column=y)
                continue
            else:
                playground[x][y]= (tk.Label(window,bg=colors[2],width=6,height=3))
                playground[x][y].grid(row=x,column=y)
                continue


    window.bind('<KeyPress>', partial(pressed,playground=playground))

    window.mainloop()

if __name__ == "__main__":
    main()
