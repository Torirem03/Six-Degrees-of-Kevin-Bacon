from bs4 import BeautifulSoup
import requests
from googlesearch import search
import csv
import random
from tkinter import *
from PIL import ImageTk, Image


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Exit", command=self.exit_program)
        menu.add_cascade(label="File", menu=file_menu)

    def winner_screen(self):
        canvas = Canvas(root, width=800, height=500)
        root.title("You Won Six Degrees of Kevin Bacon!!!")
        window_width = 600
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        root.iconbitmap("final_project/kevin_bacon_icon.ico")
        img = ImageTk.PhotoImage(Image.open("final_project/happy_kb.jpg"))
        canvas.create_text(300, 50, text="CONGRATULATIONS!!!", fill="black", font=('Helvetica 15 bold'))
        canvas.create_image(300, 75, anchor=N, image=img)
        canvas.pack()
        root.mainloop()

    def lose_screen(self):
        canvas = Canvas(root, width=800, height=500)
        root.title("You lost...")
        window_width = 600
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        root.iconbitmap("final_project/kevin_bacon_icon.ico")
        img = ImageTk.PhotoImage(Image.open("final_project/sad_kb.jpg"))
        canvas.create_text(300, 50, text="Better luck next time :(", fill="black", font=('Helvetica 15 bold'))
        canvas.create_image(300, 75, anchor=N, image=img)
        canvas.pack()
        root.mainloop()

    def exit_program(self):
        exit()


def difficulty_setup():
    diff_setting = input("Select your difficulty: Easy, Medium, Hard, or Film Buff: \n")
    match diff_setting:
        case "Easy" | "easy":
            return 6
        case "Medium" | "medium":
            return 5
        case "Hard" | "hard":
            return 4
        case "Film Buff" | "film buff":
            return 3
        case other:
            return print("Did not recognize input. Please check spelling and try again."), exit()


def starting_actor():
    with open('final_project/Top 1000 Actors and Actresses.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        random_actor = random.choice(list(csv_reader))
        beginning_actor = "".join(random_actor)
    return beginning_actor


def movie_search(m_name):
    for url in search(m_name + ' movie IMDB', stop=1):
        return url


def tv_search(tv_name):
    for url in search(tv_name + ' tv show IMDB', stop=1):
        return url


def cast_list_parser(url):
    response = requests.get(url + "fullcredits?ref_=tt_cl_sm")
    soup = BeautifulSoup(response.text, "html.parser")
    actors = soup.select("td.primary_photo")
    actor_list = []
    for index in range(0, len(actors)):
        movie_string = str(actors[index])
        new_actors = movie_string.split('"')
        actor_list.append(new_actors[5])
    return actor_list


def player_name_validation(pname):
    try:
        if pname.isalpha():
            return f"Alright {pname}! Let's see if you got what it takes!"
        else:
            raise TypeError
    except TypeError:
        print("Please only use letters from A-Z. Restart the program to try again.")
        exit()


def game_logic(difficulty, actor, player_name):
    attempts = 0
    game_won = False

    print("Your starting actor is: " + actor)
    while attempts < difficulty:
        show_guess = input("Give us a movie or tv show name that contains this actor. "
                           "If Kevin Bacon is also in this show/movie, you win!: ")
        genre_answer = input("Is this a tv show or movie? ")
        if genre_answer.lower() == "movie":
            cast_list = cast_list_parser((movie_search(show_guess)))
        else:
            cast_list = cast_list_parser((tv_search(show_guess)))
        while actor not in cast_list:
            print("Movie must contain starting actor to continue!")
            show_guess = input("Give us a movie or tv show name that contains this actor. "
                               "If Kevin Bacon is also in this show/movie, you win!: ")
            genre_answer = input("Is this a tv show or movie? ")
            if genre_answer.lower() == "movie":
                cast_list = cast_list_parser((movie_search(show_guess)))
            else:
                cast_list = cast_list_parser((tv_search(show_guess)))
        else:
            if "Kevin Bacon" in cast_list:
                attempts += 1
                print(
                    f"You won! Congratulations {player_name}! You guessed the degrees of Bacon within "
                    f"{attempts} attempt(s)!")
                game_won = True
                return game_won
            else:
                print(f"Yes! {actor} is in {show_guess}")
                actor = input(f"Please enter a new actor from {show_guess}: ")
                while actor not in cast_list:
                    print("This actor is not in that movie/tv show. Please try again.")
                    actor = input(f"Please enter a new actor from {show_guess}: ")
                else:
                    attempts += 1
    print(f"You lost, {player_name}... Try again!")
    return game_won


if __name__ == '__main__':
    print("Let's Play 6 degrees of Kevin Bacon!")
    p_name = input("Please enter your name: ")
    print(player_name_validation(p_name))

    diff_level = difficulty_setup()
    s_actor = starting_actor()
    win_lose = game_logic(diff_level, s_actor, p_name)
    if win_lose:
        root = Tk()
        winner = Window(root)
        winner.winner_screen()
    else:
        root = Tk()
        loser = Window(root)
        loser.lose_screen()
