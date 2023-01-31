from art import *
from game_data import *
import random


def random_person():
    index = random.randint(0, len(data))
    return data[index]


def get_name(person):
    return person.get('name')


def get_followers(person):
    return person.get('follower_count')


first_person = random_person()
second_person = random_person()

first_name = get_name(first_person)
second_name = get_name(second_person)

first_followers = get_followers(first_person)
second_followers = get_followers(second_person)

counter = 0

while True:
    counter += 1
    choice = input(
        f"Is {first_name} higher or lower than {second_name}? (h/l) ")
    if first_followers > second_followers:
        if choice == 'h':
            print(f"Well done! Your score is {counter}.")
            second_name = first_name
            second_followers = first_followers
            first_person = random_person()
            first_name = get_name(first_person)
            first_followers = get_followers(first_person)
        elif choice == 'l':
            print(f"Unlucky! You got a final score of {counter}.")
            break
    elif first_followers < second_followers:
        if choice == 'l':
            print(f"Well done! Your score is {counter}.")
            second_name = first_name
            second_followers = first_followers
            first_person = random_person()
            first_name = get_name(first_person)
            first_followers = get_followers(first_person)
        elif choice == 'h':
            print(f"Unlucky! You got a final score of {counter}.")
            break
