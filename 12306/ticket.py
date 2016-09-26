import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up','Left','Down','Right','Restart','Exit']
letter_code = [ord(ch) for ch in 'WSADRQwsadrq']
actions_dict = dict(zip(letter_code,actions*2))
