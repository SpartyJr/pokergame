from tkinter import *
from PIL import ImageTk, Image
import random


class Card(object):
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit
        self.showing = True

    def __repr__(self):
        if self.showing:
            return str(self.name) + "_" + self.suit
        else:
            return "Card"


class Deck(object):
    def __init__(self):
        self.cards = []
        suits = ["h", "s", "d", "c"]
        values = {"two": 2,
                  "three": 3,
                  "four": 4,
                  "five": 5,
                  "six": 6,
                  "seven": 7,
                  "eight": 8,
                  "nine": 9,
                  "ten": 10,
                  "jack": 11,
                  "queen": 12,
                  "king": 13,
                  "ace": 14}

        for name in values:
            for suit in suits:
                self.cards.append(Card(name, values[name], suit))

    def shuffle(self):
        random.shuffle(self.cards)
        print("Deck Shuffled")

    def deal(self):
        return self.cards.pop(0)


class Player(object):
    def __init__(self):
        self.cards = []


class Hand(object):
    def __init__(self):
        self.cards = []


class Community(object):
    def __init__(self):
        self.cards = []


# Objects
player = Player()
bot_1 = Player()
bot_2 = Player()
bot_3 = Player()
bot_4 = Player()
bot_5 = Player()
community = Community()
deck = Deck()
player_hand = Hand()
bot_1_hand = Hand()
bot_2_hand = Hand()
bot_3_hand = Hand()
bot_4_hand = Hand()
bot_5_hand = Hand()
pos_list = ["Player_1", "Bot_1", "Bot_2", "Bot_3", "Bot_4", "Bot_5"]
new_last = pos_list[0]
game_state = "New Round"


def card_init():
    player.cards = ["no_card", "no_card"]
    bot_1.cards = ["no_card", "no_card"]
    bot_2.cards = ["no_card", "no_card"]
    bot_3.cards = ["no_card", "no_card"]
    bot_4.cards = ["no_card", "no_card"]
    bot_5.cards = ["no_card", "no_card"]
    community.cards = []
    deck.__init__()
    print(str(player.cards))


card_init()


def end_round():
    global new_last
    global game_state
    pos_list.pop(0)
    pos_list.insert(5, new_last)
    new_last = pos_list[0]
    game_state = "New Round"
    card_init()


def deal_preflop():
    global game_state
    game_state = "preflop"
    deck.shuffle()
    for i in range(2):
        player.cards.pop()
        player.cards.insert(0, deck.deal())
        bot_1.cards.pop()
        bot_1.cards.insert(0, deck.deal())
        bot_2.cards.pop()
        bot_2.cards.insert(0, deck.deal())
        bot_3.cards.pop()
        bot_3.cards.insert(0, deck.deal())
        bot_4.cards.pop()
        bot_4.cards.insert(0, deck.deal())
        bot_5.cards.pop()
        bot_5.cards.insert(0, deck.deal())
    print("Player's cards: " + str(player.cards))
    print("Bot 1's cards: " + str(bot_1.cards))
    print("Bot 2's cards: " + str(bot_2.cards))
    print("Bot 3's cards: " + str(bot_3.cards))
    print("Bot 4's cards: " + str(bot_4.cards))
    print("Bot 5's cards: " + str(bot_5.cards))


def deal_flop():
    global game_state
    game_state = "flop"
    for i in range(3):
        community.cards.append(deck.deal())
    print("Flop = " + str(community.cards))
    canvas.create_image(252, 256, image=eval(str(community.cards[0])), tags="c1")
    canvas.create_image(331, 256, image=eval(str(community.cards[1])), tags="c2")
    canvas.create_image(410, 256, image=eval(str(community.cards[2])), tags="c3")


def deal_turn():
    global game_state
    game_state = "turn"
    for i in range(1):
        community.cards.append(deck.deal())
    print("Turn = " + str(community.cards[3]))
    canvas.create_image(489, 256, image=eval(str(community.cards[3])), tags="c4")


def deal_river():
    global game_state
    game_state = "river"
    for i in range(1):
        community.cards.append(deck.deal())
    print("River = " + str(community.cards[4]))
    canvas.create_image(568, 256, image=eval(str(community.cards[4])), tags="c5")


root = Tk()
root.title('Poker App')
root.geometry("900x628+30+30")
# Index table background
table = PhotoImage(file="poker_table.png")
# Create canvas
canvas = Canvas(root)
canvas.pack(fill="both", expand=True)
# Place background in canvas
canvas.anchor("nw")
canvas.create_image(0, 0, image=table, anchor="nw")


def deal():
    if game_state == "New Round":
        deal_preflop()
        canvas.create_image(395, 440, image=eval(str(player.cards[0])), tags="p1")
        canvas.create_image(435, 440, image=eval(str(player.cards[1])), tags="p2")
        canvas.create_image(75, 380, image=cardback, tags="b1_1")
        canvas.create_image(115, 380, image=cardback, tags="b1_2")
        canvas.create_image(90, 100, image=cardback, tags="b2_1")
        canvas.create_image(135, 100, image=cardback, tags="b2_2")
        canvas.create_image(395, 80, image=cardback, tags="b3_1")
        canvas.create_image(435, 80, image=cardback, tags="b3_2")
        canvas.create_image(700, 380, image=cardback, tags="b4_1")
        canvas.create_image(740, 380, image=cardback, tags="b4_2")
        canvas.create_image(675, 100, image=cardback, tags="b5_1")
        canvas.create_image(715, 100, image=cardback, tags="b5_2")
        return
    if game_state == "preflop":
        deal_flop()
        return
    if game_state == "flop":
        deal_turn()
        return
    if game_state == "turn":
        deal_river()
        return
    if game_state == "river":
        end_round()
        canvas.delete("p1", "p2", "b1_1", "b1_2", "b2_1", "b2_2", "b3_1", "b3_2", "b4_1", "b4_2", "b5_1", "b5_2")
        canvas.delete("c1", "c2", "c3", "c4", "c5")


# Add action buttons
btn_fold = Button(root, text="Fold", padx=20, pady="30")
btn_check = Button(root, text="Check", padx=20, pady="30")
btn_call = Button(root, text="Call", padx=20, pady="30")
btn_raise = Button(root, text="Raise", padx=20, pady="30")
btn_deal = Button(root, text="Deal", padx=30, pady=30, command=deal)
# Place action buttons
btn_fold.place(x=500, y=500)
btn_check.place(x=600, y=500)
btn_call.place(x=700, y=500)
btn_raise.place(x=800, y=500)
btn_deal.place(x=150, y=500)

# Create card labels
two_h = ImageTk.PhotoImage(Image.open("Card PNGs/2_of_hearts.png"))
two_c = ImageTk.PhotoImage(Image.open("Card PNGs/2_of_clubs.png"))
two_d = ImageTk.PhotoImage(Image.open("Card PNGs/2_of_diamonds.png"))
two_s = ImageTk.PhotoImage(Image.open("Card PNGs/2_of_spades.png"))
three_h = ImageTk.PhotoImage(Image.open("Card PNGs/3_of_hearts.png"))
three_c = ImageTk.PhotoImage(Image.open("Card PNGs/3_of_clubs.png"))
three_d = ImageTk.PhotoImage(Image.open("Card PNGs/3_of_diamonds.png"))
three_s = ImageTk.PhotoImage(Image.open("Card PNGs/3_of_spades.png"))
four_h = ImageTk.PhotoImage(Image.open("Card PNGs/4_of_hearts.png"))
four_c = ImageTk.PhotoImage(Image.open("Card PNGs/4_of_clubs.png"))
four_d = ImageTk.PhotoImage(Image.open("Card PNGs/4_of_diamonds.png"))
four_s = ImageTk.PhotoImage(Image.open("Card PNGs/4_of_spades.png"))
five_h = ImageTk.PhotoImage(Image.open("Card PNGs/5_of_hearts.png"))
five_c = ImageTk.PhotoImage(Image.open("Card PNGs/5_of_clubs.png"))
five_d = ImageTk.PhotoImage(Image.open("Card PNGs/5_of_diamonds.png"))
five_s = ImageTk.PhotoImage(Image.open("Card PNGs/5_of_spades.png"))
six_h = ImageTk.PhotoImage(Image.open("Card PNGs/6_of_hearts.png"))
six_c = ImageTk.PhotoImage(Image.open("Card PNGs/6_of_clubs.png"))
six_d = ImageTk.PhotoImage(Image.open("Card PNGs/6_of_diamonds.png"))
six_s = ImageTk.PhotoImage(Image.open("Card PNGs/6_of_spades.png"))
seven_h = ImageTk.PhotoImage(Image.open("Card PNGs/7_of_hearts.png"))
seven_c = ImageTk.PhotoImage(Image.open("Card PNGs/7_of_clubs.png"))
seven_d = ImageTk.PhotoImage(Image.open("Card PNGs/7_of_diamonds.png"))
seven_s = ImageTk.PhotoImage(Image.open("Card PNGs/7_of_spades.png"))
eight_h = ImageTk.PhotoImage(Image.open("Card PNGs/8_of_hearts.png"))
eight_c = ImageTk.PhotoImage(Image.open("Card PNGs/8_of_clubs.png"))
eight_d = ImageTk.PhotoImage(Image.open("Card PNGs/8_of_diamonds.png"))
eight_s = ImageTk.PhotoImage(Image.open("Card PNGs/8_of_spades.png"))
nine_h = ImageTk.PhotoImage(Image.open("Card PNGs/9_of_hearts.png"))
nine_c = ImageTk.PhotoImage(Image.open("Card PNGs/9_of_clubs.png"))
nine_d = ImageTk.PhotoImage(Image.open("Card PNGs/9_of_diamonds.png"))
nine_s = ImageTk.PhotoImage(Image.open("Card PNGs/9_of_spades.png"))
ten_h = ImageTk.PhotoImage(Image.open("Card PNGs/10_of_hearts.png"))
ten_c = ImageTk.PhotoImage(Image.open("Card PNGs/10_of_clubs.png"))
ten_d = ImageTk.PhotoImage(Image.open("Card PNGs/10_of_diamonds.png"))
ten_s = ImageTk.PhotoImage(Image.open("Card PNGs/10_of_spades.png"))
jack_h = ImageTk.PhotoImage(Image.open("Card PNGs/jack_of_hearts2.png"))
jack_c = ImageTk.PhotoImage(Image.open("Card PNGs/jack_of_clubs2.png"))
jack_d = ImageTk.PhotoImage(Image.open("Card PNGs/jack_of_diamonds2.png"))
jack_s = ImageTk.PhotoImage(Image.open("Card PNGs/jack_of_spades2.png"))
queen_h = ImageTk.PhotoImage(Image.open("Card PNGs/queen_of_hearts2.png"))
queen_c = ImageTk.PhotoImage(Image.open("Card PNGs/queen_of_clubs2.png"))
queen_d = ImageTk.PhotoImage(Image.open("Card PNGs/queen_of_diamonds2.png"))
queen_s = ImageTk.PhotoImage(Image.open("Card PNGs/queen_of_spades2.png"))
king_h = ImageTk.PhotoImage(Image.open("Card PNGs/king_of_hearts2.png"))
king_c = ImageTk.PhotoImage(Image.open("Card PNGs/king_of_clubs2.png"))
king_d = ImageTk.PhotoImage(Image.open("Card PNGs/king_of_diamonds2.png"))
king_s = ImageTk.PhotoImage(Image.open("Card PNGs/king_of_spades2.png"))
ace_h = ImageTk.PhotoImage(Image.open("Card PNGs/ace_of_hearts.png"))
ace_c = ImageTk.PhotoImage(Image.open("Card PNGs/ace_of_clubs.png"))
ace_d = ImageTk.PhotoImage(Image.open("Card PNGs/ace_of_diamonds.png"))
ace_s = ImageTk.PhotoImage(Image.open("Card PNGs/ace_of_spades.png"))
cardback = ImageTk.PhotoImage(Image.open("Card PNGs/card_back.png"))

root.mainloop()
