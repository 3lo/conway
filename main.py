#!/usr/bin/python3
import random

# Conway's game of life

board_state = []


def dead_state(w, h):
    death = []
    for i in range(w):
        death.append(0)
    for i in range(h):
        board_state.append(death[:])
    return board_state


def random_state(w, h):
    state = dead_state(w, h)
    for i in range(h):
        for j in range(w):
            random_number = random.random()
            if random_number >= 0.5:
                state[i][j] = "#"
            else:
                state[i][j] = " "
    return state


def render(state):
    print("-------")
    for i in range (len(state)):
        print(state[i])
    print("-------")


def next_board_state(state):
    pass


a_random_state = random_state(5, 6)
print(render(a_random_state))
