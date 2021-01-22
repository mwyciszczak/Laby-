#nie mam pojęcia czemu to nie działa
#dlaczego nie jestem w stanie zmienić zmiennej ans buttonem

import webbrowser
from tkinter import *
import time


main = Tk()
main.geometry("800x600")
main.resizable(0, 0)
main.title("Quiz informatyczny")

A = "a"
B = "b"
C = "c"
D = "d"
"""global ans
ans = "b"""""
global score
score = 0
i = 0
global question_number
question_number = 0
global ii
ii = 0


q1 = PhotoImage(file="q_a/q1.gif")
q1_a = PhotoImage(file="q_a/q1_a.gif")
q1_b = PhotoImage(file="q_a/q1_b.gif")
q1_c = PhotoImage(file="q_a/q1_c.gif")
q1_d = PhotoImage(file="q_a/q1_d.gif")


q2 = PhotoImage(file="q_a/q2.gif")
q2_a = PhotoImage(file="q_a/q2_a.gif")
q2_b = PhotoImage(file="q_a/q2_b.gif")
q2_c = PhotoImage(file="q_a/q2_c.gif")
q2_d = PhotoImage(file="q_a/q2_d.gif")


question_1 = (q1, q1_a, q1_b, q1_c, q1_d)
question_2 = (q2, q2_a, q2_b, q2_c, q2_d)

question_list = [question_1, question_2]
answers_list = ["b", "a"]
ans_list = []


menu_quiz_button_image = PhotoImage(file="img/menu_quiz_button.gif")
menu_cat_button_image = PhotoImage(file="img/menu_cat_button.gif")
menu_exit_button_image = PhotoImage(file="img/menu_exit_button.gif")
menu_background_image = PhotoImage(file="img/menu_backgorund_image.gif")

quiz_question_image = PhotoImage(file="img/quiz_question_textbox.gif")
quiz_question_answer = PhotoImage(file="img/quiz_answer_button.gif")


def draw_background():
    background_label = Label(main, image=menu_background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


def clear_all_widgets():
    widgets = main.winfo_children()
    for x in widgets:
        if x.winfo_children():
            widgets.extend(x.winfo_children())
    for y in widgets:
        y.destroy()


def answer_a_func():
    global score
    global i
    ans_list.append("a")
    print("a")
    print(ans_list)
    if ans_list[i] == answers_list[i]:
        score += 1
        print("Score is {}".format(score))
    else:
        print("else")
def answer_b_func():
    global score
    global i
    ans_list.append("b")
    print("b")
    print(ans_list)
    if ans_list[i] == answers_list[i]:
        score += 1
        print("Score is {}".format(score))
    else:
        print("else")
def answer_c_func():
    global score
    global i
    ans_list.append("c")
    print("c")
    print(ans_list)
    if ans_list[i] == answers_list[i]:
        score += 1
        print("Score is {}".format(score))
    else:
        print("else")
def answer_d_func():
    global score
    global i
    ans_list.append("d")
    print("d")
    print(ans_list)
    while True:
        if ans_list[i] == answers_list[i]:
            score += 1
            print("Score is {}".format(score))
            break
        else:
            print("else")
            break


def exit_button_func():
    exit()


def cat_button_func():
    webbrowser.open_new_tab("https://www.pinterest.com/timzuidgeest/funny-cats/")


def draw_quiz(question, answer_a, answer_b, answer_c, answer_d):
    question_textbox = Label(main, image=question, height=100, width=600)
    question_textbox.grid(row=0, column=0, columnspan=2, padx=100, pady=50)
    answer_button_a = Button(main, image=answer_a, height=100, width=200, command=lambda: answer_a_func())
    answer_button_a.grid(row=1, column=0, pady=35)
    answer_button_b = Button(main, image=answer_b, height=100, width=200, command=lambda: answer_b_func())
    answer_button_b.grid(row=1, column=1, pady=35)
    answer_button_c = Button(main, image=answer_c, height=100, width=200, command=lambda: answer_c_func())
    answer_button_c.grid(row=2, column=0, pady=35)
    answer_button_d = Button(main, image=answer_d, height=100, width=200, command=lambda: answer_d_func())
    answer_button_d.grid(row=2, column=1, pady=35)
    global question_number
    if question_number[i] < ii + 1:
        question_number += 1

def quiz_button_func():
    for x in question_list:
        clear_all_widgets()
        draw_background()
        tuple = x
        draw_quiz(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4])


def menu():
    draw_background()
    global quiz_button
    quiz_button = Button(main, image=menu_quiz_button_image, height=100, width=350, command=quiz_button_func)
    quiz_button.grid(row=0, column=0, padx=225, pady=48)
    global cat_button
    cat_button = Button(main, image=menu_cat_button_image, height=100, width=350, command=cat_button_func)
    cat_button.grid(row=1, column=0, padx=225, pady=48)
    global exit_button
    exit_button = Button(main, image=menu_exit_button_image, height=100, width=350, command=exit_button_func)
    exit_button.grid(row=2, column=0, padx=225, pady=48)

menu()
main.mainloop()