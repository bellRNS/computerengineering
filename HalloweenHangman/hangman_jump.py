"""
This hangman game was originally created by Katie Cunningham for Sams Teach Yourself Python in 24HRS c2014
adapted and updated by JB in 2019 for spooky halloween fun

"""

import pygame
import sys, os
from random import choice

from pygame.locals import *

"""Creating colours used in the game. 
A few extras than you are planning for are always nice
in case you "dont know what to wear"
"""
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 100, 0)
PURPLE = (100, 0, 255)


def get_words():
    """function helps to break down a string of words into individual strings"""
    f = open('words.txt')  # this text file is saved in my project environment
    temp = f.readlines()  # readlines is handy to put temp into one long string
    words = []
    for word in temp:
        words.append(word.strip())  # appends each word after stripping them by breaking at spaces between words
    return words


def draw_gallows(screen):
    """This function draws the components of the hangmans gallows."""
    pygame.draw.rect(screen, ORANGE, (450, 350, 100, 10))  # bottom 0
    pygame.draw.rect(screen, ORANGE, (495, 250, 10, 100))  # support
    pygame.draw.rect(screen, ORANGE, (450, 250, 50, 10))  # cross bar
    pygame.draw.rect(screen, ORANGE, (450, 250, 10, 25))  # noose


def draw_man(screen, body_part):
    """This function needs to run on a screen object, and passes a specific body_part to draw,
    we define these body parts later in a list"""
    if body_part == 'head':
        pygame.draw.circle(screen, ORANGE, (455, 270), 10)
    if body_part == 'body':
        pygame.draw.line(screen, ORANGE, (455, 280), (455, 320), 3)
    if body_part == "l_arm":
        pygame.draw.line(screen, ORANGE, (455, 300), (445, 285), 3)
    if body_part == 'r_arm':
        pygame.draw.line(screen, ORANGE, (455, 300), (465, 285), 3)
    if body_part == 'l_leg':
        pygame.draw.line(screen, ORANGE, (455, 320), (445, 330), 3)
    if body_part == 'r_leg':
        pygame.draw.line(screen, ORANGE, (455, 320), (465, 330), 3)


def draw_word(screen, spaces):
    """draws the spaces on the screen for the hangman word. spaces will be passed as len(word) later on."""
    x = 10  # Starts ten steps in on the left handteside
    for i in range(spaces):
        pygame.draw.line(screen, YELLOW, (x, 350), (x + 20, 350),
                         3)  # for each space given, draw a segment then jump 30
        x += 30


def draw_letter(screen, font, word, guess):
    """Functions a lot like draw_word above, but draws a letter each time, only in the correct place.
    font = necessary type font, word = given later, guess = keystroke guess.
    The 'blitting' is confusing - it draws the letters where they need to be.
    We map all of the locations using the loop below, and when we call the function we can reveal the guess
    """
    x = 10
    for letter in word:
        if letter == guess:
            letter = font.render(letter, 3, (255, 255, 255))  # this creates font in each spot necessary
            screen.blit(letter, (x, 300))  # this does the job of 'drawing' in each rendered spot
        x += 30


def main():
    pygame.init()  # necessary to INITialize pygame
    screen = pygame.display.set_mode((600, 400))  # creates screen
    font = pygame.font.SysFont("monospace", 30)  # creates a font object for the game to use
    draw_gallows(screen)  # draws the gallows
    draw_man(screen, "head")  # Starts off by drawing the head

    words = get_words()  # uses get_words to return a list of words

    word = choice(words)  # uses random module to pick a word at random from words

    draw_word(screen, len(word))  # draws the word spaces on the screen
    pygame.display.update()  # first update allows everything to be seen

    body = ['l_leg', 'r_leg', 'l_arm', 'r_arm', 'body',
            'head']  # Creates a list of body objects to choose and delete from
    counter = 0  # counter, used later and described insied while loop

    while body:
        for event in pygame.event.get():  # for every event in pygame
            if event.type == QUIT:  # if event type is pressing x on window screen
                sys.exit()  # exit
            if event.type == KEYDOWN:  # if event is a key press
                if event.unicode.isalpha():  # if its a letter
                    guess = event.unicode  # creates a variable that stores the guess
                else:
                    continue
                if guess in word:  # if guess is in the actual word
                    draw_letter(screen, font, word, guess)  # draw the write letter(guess)
                    pygame.display.update()  # update screen
                    counter += 1  # add 1 to the counter
                else:  # if the guess is not in the letter
                    body_part = body.pop()  # pick a body part, and deletes it from the list
                    draw_man(screen, body_part)  # draws a segment of the main using function
                    pygame.display.update()


                if len(word) == counter:                            #if the length of word equals number of right guess
                     background_image = pygame.image.load("spookydoggo.jpg").convert() #these load my spooky surprises
                     screen.blit(background_image, [0, 0])
                     pygame.display.update()
                     pygame.mixer.music.load('aarrgghh.wav')
                     pygame.mixer.music.play(-1)



if __name__ == '__main__':  # the magic line to get your game to run
    main()  # runs the main function with all the stuff outlined for game events
