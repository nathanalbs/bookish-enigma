"""
**************************************************************
Name        : final_project.py
Author      : Nathan Albertson
Created     : 04/30/2023
Course      : CIS 152 Data Structures
Copyright   : This is my own original work based on
              specifications issued by our instructor
Description : Application allowing players to join different video game tournaments
    and outputting the final rosters
***************************************************************
"""

#define player class with name, rank, and age attributes
class Player:
    def __init__(self, name, rank, age):
        self.name = name
        self.rank = rank
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.rank}, {self.age})"

#here is my queue data structure that will hold the player ojbects as they join the tournaments
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        self.bubble_sort()

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def remove_player(self, name):
        for i, player in enumerate(self.items):
            if player.name == name:
                return self.items.pop(i)
    #bubble sort algorithm for sorting the players by ranks
    def bubble_sort(self):
        for i in range(len(self.items)):
            for j in range(len(self.items) - i - 1):
                if self.items[j].rank > self.items[j+1].rank:
                    self.items[j], self.items[j+1] = self.items[j+1], self.items[j]

#this is a stack data structure which hold the tournaments
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

#this is just a simple class that holds the tournaments name and begins the queues
class Tournament:
    def __init__(self, name):
        self.name = name
        self.players = Queue()

    def add_player(self, name, rank, age):
        rank_values = {
            "Iron": 9,
            "Bronze": 8,
            "Silver": 7,
            "Gold": 6,
            "Platinum": 5,
            "Diamond": 4,
            "Master": 3,
            "Grandmaster": 2,
            "Challenger": 1
        }
        #here I've added some input validation for the ranks
        rank = rank.capitalize()
        if rank not in rank_values:
            print(f"Invalid rank: {rank}. Please enter one of the following ranks: {', '.join(rank_values.keys())}.")
            return
        player = Player(name, rank, age)
        #here I wanted some validation so that only Challenger ranked players would be allowed to join the all star game
        if self.name == "All-Star Game" and rank != "Challenger":
            print(f"Sorry, only Challenger players can join the {self.name} tournament.")
        else:
            self.players.enqueue(player)
    #this funtion outputs the final rosters
    def play(self):
        print(f"Playing {self.name}...")
        while not self.players.is_empty():
            player = self.players.dequeue()
            print(f" {player}")

    def __str__(self):
        return self.name

#creats stack and adds tournaments
tournaments = Stack()
tournaments.push(Tournament("League Championship Series"))
tournaments.push(Tournament("League of Legends EMEA Championship"))
tournaments.push(Tournament("All-Star Game"))

#my main that prompts and gets user input for player info
for tournament in tournaments.items:
    print(f"Joining {tournament}...")
    while True:
        name = input("Enter your name (or 'q' to finish): ")
        if name == 'q':
            break
        rank = input("Enter your rank: ")
        age = input("Enter your age: ")
        tournament.add_player(name, rank, age)

        #option to leave the tournament
        while True:
            leave = input("Do you want to leave the tournament? (y/n): ")
            if leave.lower() == 'y':
                tournament.players.remove_player(name)
                print(f"{name} has left the tournament.")
                break
            elif leave.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

while not tournaments.is_empty():
    tournament = tournaments.pop()
    tournament.play()
