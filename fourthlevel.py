from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.image import Image
from array import *
import random

global exit
exit = 0

Config.set('graphics', 'resizable', True)
Window.size = (360, 640)

''' card
    The class card is a memory card class. It has a non-unique id called 'type' and a link as an attribute. The attribute type pertains to the link, so a card with the type 1 will
    have the same link as another card with type 1, both of them will have link to a picture of a duck. By comparing the types we can, as such, discern if we have a match between
    two cards or not.  
'''

class card:
    def __init__(self, type):
        self.type = type

        switch = {
            1: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\APPLE.png",
            2: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\AVOCADO(1).png",
            3: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\CABBAGE.png",
            4: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\CORN.png",
            5: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\CUCUMBER.png",
            6: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\GARLIC.png",
            7: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\GREEN ONION.png",
            8: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\LEMON.png",
            9: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\SPINACH.png",
            10: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\WALNUT.png",
        }
        try:
            self.link = switch[type]

        except KeyError:
            print(type, "is not a valid type, there is no such memory card!")

    def __str__(self):
        types = {
            1: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\APPLE.png",
            2: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\AVOCADO(1).png",
            3: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\CABBAGE.png",
            4: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\CORN.png",
            5: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\CUCUMBER.png",
            6: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\GARLIC.png",
            7: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\GREEN ONION.png",
            8: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\LEMON.png",
            9: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\SPINACH.png",
            10: r"C:\Users\roche\Desktop\GAME\Matching Pair\Fourth Level\WALNUT.png",
        }

        return types[self.type]

    def __eq__(self, other):
        if (self.type == other.type):
            return True
        return False

class Memory_Game(App):
    def randomization(self):
        ''' randomization
            This algorithm is a shuffling algorithm to achieve pseudo randomness. We use it to shuffle the memory cards when initiating the game.
        '''

        for i in range(len(self.card_list) - 1, 0, -1):
            rand = random.randint(0, i)
            self.card_list[i], self.card_list[rand] = self.card_list[rand], self.card_list[i]

    def unflip(self, id):
        ''' unflip
            A function that takes an id and simply unflips the card meaning the backside will be turned upwards.
        '''

        index = id - 1

        # Unflipping the card:
        self.display_list[index].clear_widgets()
        self.button(str(id))

    def flip(self, id):
        ''' flip
            Takes a card with its backside up (the button label) and flips it with the image up.
        '''

        # Setting the index and checking if it is a won card already, and if so, we should do nothing:
        index = id - 1
        if (index in self.outcome):
            return 0

        # Incrementing the turn counter:
        self.turn_counter += 1

        # Count flips, set as flipped and potentially alternate turn:
        if (self.turn_counter == 3):
            self.turn_counter = 0
            first_card, second_card = self.flipped_cards

            # See if we got two of the same:
            is_pair = False
            print(first_card, second_card)
            if (self.card_list[first_card] == self.card_list[second_card]):
                sound=SoundLoader.load(r"C:\Users\roche\Desktop\GAME\successfully matched.wav")
                sound.play()
                
                print("You're Correct!!!")
                is_pair = True
                self.outcome.append(first_card)
                self.outcome.append(second_card)

                global exit
                exit += 1

                if exit == 9:
                    quit()

            if (not is_pair):
                sound=SoundLoader.load(r"C:\Users\roche\Desktop\GAME\unsuccessful matched.wav")
                sound.play()

                print("Wrong!!")
                self.unflip(first_card + 1)
                self.unflip(second_card + 1)
                self.player_turn = (self.player_turn % 2) + 1
                self.flipped_cards = [0, 0]

            return 0

        # Flipping the card:
        self.display_list[index].clear_widgets()
        memory_photo = Image(source=self.card_list[index].link)
        self.display_list[index].add_widget(memory_photo)
        self.flipped_cards[self.turn_counter - 1] = id - 1

    def button(self, id):


        b = Button(

            text=id,
            color='#525152',
            size_hint=(5, 0.3),
            pos_hint={"center_x": 5, "center_y": 5},
            border=(.1, .1, .1, .1),
            background_normal=r"C:\Users\roche\Desktop\GAME\Logo\Logo For Card.png",
        )

        self.display_list[int(id) - 1].add_widget(b)
        b.bind(on_press=lambda x: self.flip(int(b.text)))
        self.button_list.append(b)

    def card_amount(self):
        ''' card_amount
            A helper function that fills the board with buttons ranging from 1 .. to n, where n is the amount of cards the players want to have.
        '''

        for id in range(1, (self.amount_of_cards * 2) + 1):
            self.button(str(id))

    def sub_layouts(self):
        ''' sub_layouts
            Fills the sub layouts, that would be, layouts to be used like cards. To achieve the flipping affect we use inner layouts as cards and upon flipping we clear the widget
            and then paint the image on that layout (or the button if unflipping).
        '''

        for layout in self.display_list:
            self.window.add_widget(layout)

    def build(self):
        self.amount_of_cards = 10
        self.flipped_cards = [0, 0]  # Holds the index of the two flipped cards.
        self.display_list = [GridLayout(cols=4) for i in range(self.amount_of_cards * 2)]
        self.outcome = []
        self.layout = [BoxLayout(padding=2) for i in range(self.amount_of_cards * 2)]

        self.card_list = []
        self.player_turn = 1
        self.turn_counter = 0
        self.score_list = [0, 0]

        for i in range(self.amount_of_cards):
            self.card_list.append(card(i + 1))
            self.card_list.append(card(i + 1))

        # Shuffling the cards around
        self.randomization()

        # Fixing a grid:
        self.window = GridLayout()
        self.window.cols = 4
        self.window.padding = (12,80,12,80)
        self.window.spacing = (15,30)
        self.button_list = []

        # Generating subgrids in the window layout:
        self.sub_layouts()

        # Adding buttons:
        self.card_amount()

        # self.window.add_widget(self.info)
        Window.clearcolor = "#A3C1AD"
        return self.window


if __name__ == "__main__":
    Memory_Game().run()