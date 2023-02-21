from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.config import Config
from array import *
from subprocess import call
from kivy.core.audio import SoundLoader

Config.set('graphics', 'resizable', True)
Window.size = (360, 640)

# Global declaration of Variables
class Variables():

    '''We declared global variables to access their values easily'''
    global garlic, scallion, spinach, cucumber, avocado, corn, apple, walnuts, lemon, cabbage
    global eggs, milk, butter, rice, flour, cornstarch, heavy_cream, parmesan_cheese, cream_cheese
    global salt, pepper, dried_oregano, parsley, soy_sauce, sugar, cinnamon_powder, vanilla
    global pork, beef, shrimp, poultry, crab_meat, salmon, squid
    global cheesecake, applepie, bakedsalmon, porkbbq, steak, alfredopasta, butteredshrimp, calamari, chickenfillet,\
    crabcornsoup, maki, spinachsalad
    global make_cheesecake, make_applepie, make_bakedsalmon, make_porkbbq, make_steak, make_alfredopasta, \
    make_butteredshrimp, make_calamari, make_chickenfillet, make_crabcornsoup, make_maki, make_spinachsalad
    global dayOne, dayTwo, dayThree, dayFour

    # Variables used in Fruits and Vegetables
    garlic = 0
    scallion = 0
    spinach = 0
    cucumber = 0
    avocado = 0
    corn = 0
    walnuts = 0
    lemon = 0
    apple = 0
    cabbage = 0

    # Variables used in Animal Products and Grains
    eggs = 0
    milk = 0
    butter = 0
    rice = 0
    flour = 0
    cornstarch = 0
    heavy_cream = 0
    parmesan_cheese = 0
    cream_cheese = 0

    # Variables used in Herbs, Spices and Seasonings
    salt = 0
    pepper = 0
    dried_oregano = 0
    parsley = 0
    soy_sauce = 0
    sugar = 0
    cinnamon_powder = 0
    vanilla= 0

    # Variables used in Meat
    pork = 0
    beef = 0
    shrimp = 0
    poultry = 0
    crab_meat = 0
    salmon = 0
    squid = 0

    # Variables used for dishes
    cheesecake = 0
    applepie = 0
    bakedsalmon = 0
    porkbbq = 0
    steak = 0
    butteredshrimp = 0
    chickenfillet = 0
    calamari = 0
    crabcornsoup = 0
    alfredopasta = 0
    spinachsalad = 0
    maki = 0

    # Variables that will indicate the dishes to be incremented
    make_cheesecake = 0
    make_applepie = 0
    make_bakedsalmon = 0
    make_porkbbq = 0
    make_steak = 0
    make_alfredopasta = 0
    make_butteredshrimp = 0
    make_calamari = 0
    make_chickenfillet = 0
    make_crabcornsoup = 0
    make_maki = 0
    make_spinachsalad = 0

    global andrei_1, trixie_1, avegail_2, shoji_2, mae_2

    andrei_1 = 0
    trixie_1 = 0
    avegail_2 = 0
    shoji_2 = 0
    mae_2 = 0

    dayOne = 0
    dayTwo = 0
    dayThree = 0
    dayFour = 0

# Looping sound
sound=SoundLoader.load(r"C:\Users\roche\Desktop\GAME\in_game.mp3")
sound.volume = 0.3
sound.loop = True
sound.play()

# SCREENS INCLUDED INSIDE THE GAME
class MainMenu(Screen):
    pass

class Kitchen(Screen):
    pass
           
class OrderArea(Screen):
    pass

class StorageRoom(Screen):
    pass

class MatchingPair(Screen):
    
    '''This function calls the firstlevel.py file. After exiting the called program it increments
    all the stock of meat, goes the same with the other remaining method'''

    def open_firstlevel(self):
        call(["python", "firstlevel.py"])
        global pork, beef, shrimp, poultry, crab_meat, salmon, squid

        pork += 1
        beef += 1
        shrimp += 1
        poultry += 1
        crab_meat += 1
        salmon += 1
        squid += 1
        
    def open_secondlevel(self):
        call(["python", "secondlevel.py"]) 
        global salt, pepper, dried_oregano, parsley, soy_sauce, sugar, cinnamon_powder, vanilla

        salt += 1
        pepper += 1
        dried_oregano += 1
        parsley += 1
        soy_sauce += 1
        sugar += 1
        cinnamon_powder += 1
        vanilla += 1

    def open_thirdlevel(self):
        call(["python", "thirdlevel.py"])
        global eggs, milk, butter, rice, flour, cornstarch, heavy_cream, parmesan_cheese, cream_cheese

        eggs += 1
        milk += 1
        butter += 1
        rice += 1
        flour += 1
        cornstarch += 1
        heavy_cream += 1
        parmesan_cheese += 1
        cream_cheese += 1

    def open_fourthlevel(self):
        call(["python", "fourthlevel.py"])
        global garlic, scallion, spinach, cucumber, avocado, corn, apple, walnuts, lemon, cabbage

        garlic += 1
        scallion += 1
        spinach += 1
        cucumber += 1
        avocado += 1
        corn += 1
        apple += 1
        walnuts += 1
        lemon += 1
        cabbage += 1

# Main screen manager that connects all the screens
class WindowManager(ScreenManager):
    pass

screen = Builder.load_string()

class MatchNMunch(App):
    def build(self):
        return screen

class FruitsAndVeggies(Popup):
    
    global garlic, scallion, spinach, cucumber, avocado, corn, apple, walnuts, lemon, cabbage

    # Gets the value of the global variables indicated and pass it within the function
    def refresh(self):
        self.ids.garlic.text = str(garlic)
        self.ids.scallion.text = str(scallion)
        self.ids.spinach.text = str(spinach)
        self.ids.cucumber.text = str(cucumber)
        self.ids.avocado.text = str(avocado)
        self.ids.corn.text = str(corn)
        self.ids.walnuts.text = str(walnuts)
        self.ids.lemon.text = str(lemon)
        self.ids.apple.text = str(apple)
        self.ids.cabbage.text = str(cabbage)

class AnimalProductsGrains(Popup):

    global eggs, milk, butter, rice, flour, cornstarch, heavy_cream, parmesan_cheese, cream_cheese

    # Gets the value of the global variables indicated and pass it within the function
    def refresh(self):
        self.ids.eggs.text = str(eggs)
        self.ids.milk.text = str(milk)
        self.ids.rice.text = str(rice)
        self.ids.flour.text = str(flour)
        self.ids.cornstarch.text = str(cornstarch)
        self.ids.heavy_cream.text = str(heavy_cream)
        self.ids.creamcheese.text = str(cream_cheese)
        self.ids.parmesan_cheese.text = str(parmesan_cheese)
        self.ids.butter.text = str(butter)

class HerbsSpicesSeasonings(Popup):
    
    global salt, pepper, dried_oregano, parsley, soy_sauce, sugar, cinnamon_powder, vanilla

    # Gets the value of the global variables indicated and pass it within the function
    def refresh(self):
        self.ids.salt.text = str(salt)
        self.ids.pepper.text = str(pepper)
        self.ids.dried_oregano.text = str(dried_oregano)
        self.ids.parsley.text = str(parsley)
        self.ids.soy_sauce.text = str(soy_sauce)
        self.ids.sugar.text = str(sugar)
        self.ids.cinnamon_powder.text = str(cinnamon_powder)
        self.ids.vanilla.text = str(vanilla)

class Meat(Popup):
    
    global pork, beef, shrimp, poultry, crab_meat, salmon, squid
 
    # Gets the value of the global variables indicated and pass it within the function
    def refresh(self):
        self.ids.pork.text = str(pork)
        self.ids.beef.text = str(beef)
        self.ids.shrimp.text = str(shrimp)
        self.ids.poultry.text = str(poultry)
        self.ids.crab_meat.text = str(crab_meat)
        self.ids.salmon.text = str(salmon)
        self.ids.squid.text = str(squid)

class Oven(Popup):

    # Increments the dish indicated while decrementing the ingredients
    def Cheesecake(self):
        global cream_cheese, eggs, sugar, heavy_cream, vanilla, cheesecake, make_cheesecake

        if cream_cheese > 0 and eggs > 0 and sugar > 0 and heavy_cream > 0 and vanilla > 0:
            make_cheesecake += 1
            cream_cheese -= 1
            eggs -= 1
            sugar -= 1
            heavy_cream -= 1
            vanilla -= 1

    def ApplePie(self):
        global apple, eggs, sugar, butter, flour, make_applepie, applepie

        if apple > 0 and eggs > 0 and sugar > 0 and butter > 0 and flour > 0:
            make_applepie += 1
            apple -= 1
            eggs -= 1
            sugar -= 1
            butter -= 1
            flour -= 1

    def BakedSalmon(self):
        global salmon, lemon, butter, garlic, salt, pepper, make_bakedsalmon, bakedsalmon

        if salmon > 0 and lemon > 0 and butter > 0 and garlic > 0 and salt > 0 and pepper > 0:
            make_bakedsalmon += 1
            salmon -= 1
            lemon -= 1
            butter -= 1
            garlic -= 1
            salt -= 1
            pepper -= 1

    def PorkBBQ(self):
        global pork, soy_sauce, garlic, sugar, lemon, make_porkbbq, pork_bbq

        if pork > 0 and soy_sauce > 0 and garlic > 0 and sugar > 0 and lemon > 0:
            make_porkbbq += 1
            pork -= 1
            soy_sauce -= 1
            garlic -= 1
            sugar -= 1
            lemon -= 1

class FryingPan(Popup):
    
    # Increments the dish indicated while decrementing the ingredients
    def Steak(self):
        global beef, salt, pepper, garlic, make_steak, steak

        if beef > 0 and salt > 0 and pepper > 0 and garlic > 0:

            make_steak += 1
            beef -= 1
            salt -= 1
            pepper -= 1
            garlic -= 1

    def GarlicButteredShrimp(self):
        global shrimp, butter, garlic, salt, pepper, lemon, make_butteredshrimp, butteredshrimp

        if shrimp > 0 and butter > 0 and garlic > 0 and salt > 0 and pepper > 0 and lemon > 0:
            
            make_butteredshrimp += 1
            shrimp -= 1
            butter -= 1
            garlic -= 1
            salt -= 1
            pepper -= 1
            lemon -= 1

    def ChickenFillet(self):
        global poultry, flour, eggs, make_chickenfillet, chickenfillet

        if poultry > 0 and flour > 0 and eggs > 0:

            make_chickenfillet += 1
            poultry -= 1
            flour -= 1
            eggs -= 1

    def Calamari(self):
        global squid, flour, salt, dried_oregano, pepper, make_calamari, calamari

        if squid > 0 and flour > 0 and salt > 0 and dried_oregano > 0 and pepper > 0:

            make_calamari += 1
            squid -= 1
            flour -= 1
            salt -= 1
            dried_oregano -= 1
            pepper -= 1
            
class Pot(Popup):
    
    # Increments the dish indicated while decrementing the ingredients
    def CrabCornSoup(self):
        global corn, crab_meat, eggs, scallion, salt, pepper, cornstarch, make_crabcornsoup, crabcornsoup
        if corn > 0 and crab_meat > 0 and eggs > 0 and scallion > 0 and salt > 0 and pepper > 0 and cornstarch > 0:
            
            make_crabcornsoup += 1
            corn -= 1
            crab_meat -= 1
            eggs -= 1
            scallion -= 1
            salt -= 1
            pepper -= 1
            cornstarch -= 1

    def ChickenAlfredoPasta(self):
        global flour, poultry, heavy_cream, parmesan_cheese, butter, parsley, make_alfredopasta, alfredopasta

        if flour > 0 and poultry > 0 and heavy_cream > 0 and parmesan_cheese > 0 and butter > 0 and parsley > 0:

            make_alfredopasta += 1
            flour -= 1
            poultry -= 1
            heavy_cream -= 1
            parmesan_cheese -= 1
            butter -= 1
            parsley -= 1


class ChoppingBoard(Popup):
    
    # Increments the dish indicated while decrementing the ingredients
    def SpinachSalad(self):
        global spinach, apple, walnuts, make_spinachsalad, spinachsalad

        if spinach > 0 and apple > 0 and walnuts > 0:

            make_spinachsalad += 1
            spinach -= 1
            apple -= 1
            walnuts -= 1

    def CaliforniaMaki(self):
        global rice, crab_meat, avocado, cucumber, make_maki, maki

        if rice > 0 and crab_meat > 0 and avocado > 0 and cucumber > 0:

            make_maki += 1
            rice -= 1
            crab_meat -= 1
            avocado -= 1
            cucumber -= 1

# A popup window for created dishes
class Refrigerator(Popup, Widget):

    # A function that will be called to show the number of created dishes
    def refresh(self):

        global cheesecake, make_cheesecake

        self.ids.cheesecake.text = str(cheesecake)
        if make_cheesecake >= 1:
            cheesecake += 1
            make_cheesecake -= 1

        global applepie, make_applepie

        self.ids.applepie.text = str(applepie)
        if make_applepie >= 1:
            applepie += 1
            make_applepie -= 1

        global bakedsalmon, make_bakedsalmon
        bakedsalmon, make_bakedsalmon

        self.ids.bakedsalmon.text = str(bakedsalmon)
        if make_bakedsalmon >= 1:
            bakedsalmon += 1
            make_bakedsalmon -= 1

        global porkbbq, make_porkbbq
        porkbbq, make_porkbbq

        self.ids.porkbbq.text = str(porkbbq)
        if make_porkbbq >= 1:
            porkbbq += 1
            make_porkbbq -= 1

        global steak, make_steak
        steak, make_steak

        self.ids.steak.text = str(steak)
        if make_steak >= 1:
            steak += 1
            make_steak -= 1

        global butteredshrimp, make_butteredshrimp
        butteredshrimp, make_butteredshrimp

        self.ids.butteredshrimp.text = str(butteredshrimp)
        if make_butteredshrimp >= 1:
            butteredshrimp += 1
            make_butteredshrimp -= 1

        global chickenfillet, make_chickenfillet
        chickenfillet, make_chickenfillet

        self.ids.chickenfillet.text = str(chickenfillet)
        if make_chickenfillet >= 1:
            chickenfillet += 1
            make_chickenfillet -= 1
            
        
        global calamari, make_calamari
        calamari, make_calamari

        self.ids.calamari.text = str(calamari)
        if make_calamari >= 1:
            calamari += 1
            make_calamari -= 1
            
        global crabcornsoup, make_crabcornsoup
        crabcornsoup, make_crabcornsoup

        self.ids.crabcornsoup.text = str(crabcornsoup)
        if make_crabcornsoup >= 1:
            crabcornsoup += 1
            make_crabcornsoup -= 1

        global alfredopasta, make_alfredopasta
        alfredopasta, make_alfredopasta

        self.ids.alfredopasta.text = str(alfredopasta)
        if make_alfredopasta >= 1:
            alfredopasta += 1
            make_alfredopasta -= 1
            
        global spinachsalad, make_spinachsalad
        spinachsalad, make_spinachsalad

        self.ids.spinachsalad.text = str(spinachsalad)
        if make_spinachsalad >= 1:
            spinachsalad += 1
            make_spinachsalad -= 1

        global maki, make_maki
        maki, make_maki
        
        self.ids.maki.text = str(maki)
        if make_maki >= 1:
            maki += 1
            make_maki -= 1

# Day one customers popup window
class DayOne(Popup):

    # A function that will indicate that the customer has been served
    def Shoji(self):
        global maki, dayOne

        if maki >= 1:
            maki -= 1
            self.ids.shoji_1.background_normal = r"C:\\Users\\roche\\Desktop\\GAME\\Button\\Customer\\Shoji_down.png"
            dayOne += 1

    def Mae(self):
        global spinachsalad, dayOne

        if spinachsalad >= 1:
            spinachsalad -= 1
            self.ids.mae_1.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Mae_down.png"
            dayOne += 1

    def Avegail(self):
        global chickenfillet, dayOne

        if chickenfillet >= 1:
            chickenfillet -= 1
            self.ids.avegail_1.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Avegail_down.png"
            dayOne += 1

# Day two customers popup window
class DayTwo(Popup, Widget):

    def Andrei(self):
        global steak, andrei_1

        if steak >= 1:
            andrei_1 = 1
            steak -= 1
            self.ids.andrei_1.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Andrei_down.png"
        
    def Trixie(self):
        global applepie, trixie_1

        if applepie >= 1:
            trixie_1 = 1
            applepie -= 1
            self.ids.trixie_1.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Trixie_down.png"

    def Avegail(self):
        global chickenfillet, avegail_2

        if chickenfillet >= 1:
            avegail_2 = 2
            chickenfillet -= 1
            
    def Shoji(self):
        global maki, shoji_2

        if maki >= 1:
            shoji_2 = 1
            maki -= 1
            self.ids.shoji_2.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Shoji_down.png"

    def Mae(self):
        global spinachsalad, mae_2

        if spinachsalad >= 1:
            mae_2 = 1
            spinachsalad -= 1
            self.ids.mae_2.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Mae_down.png"

# Day three customers popup window
class DayThree(Popup, Widget):
    
    def Trixie(self):
        global applepie

        if applepie >= 1:
            applepie -= 1
            self.ids.avegail_1.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Trixie_down.png"

    def Princess(self):
        global cheesecake

        if cheesecake >= 1:
            cheesecake -= 1
            self.ids.bind.trixie_1
            self.ids.trixie_1.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Princess_down.png"

    def Jaime(self):
        global chickenfillet

        if chickenfillet >= 1:
            chickenfillet -= 1
            self.ids.avegail_2.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Jaime_down.png"

    def Anya(self):
        global maki

        if maki >= 1:
            maki -= 1
            self.ids.shoji_2.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Anya_down.png"

    def Andrei(self):
        global spinachsalad

        if spinachsalad >= 1:
            spinachsalad -= 1
            self.ids.mae_2.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Andrei_down.png"

    def Jericho(self):
        global spinachsalad

        if spinachsalad >= 1:
            spinachsalad -= 1
            self.ids.mae_2.background_normal = r"C:\Users\roche\Desktop\GAME\Button\Customer\Jericho_down.png"

# Day four customers popup window
class DayFour(Popup, Widget):
    pass

class Tutorial(Popup, Widget):  
    pass

if __name__ == "__main__":
    MatchNMunch().run()
