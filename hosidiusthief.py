import time

import utilities.color as clr
import utilities.random_util as rd
import utilities.imagesearch as imsearch
import pyautogui as pag
from model.bot import BotStatus
from model.zaros.zaros_bot import ZarosBot
from utilities.api.morg_http_client import MorgHTTPSocket
from utilities.api.status_socket import StatusSocket



import random


class ZarosHosidiusThief(ZarosBot):
    def __init__(self):
        bot_title = "Hosidius Thief"
        description = "Bots Hosidius Fruit Stall thieving."
        super().__init__(bot_title=bot_title, description=description)
        # Set option variables below (initial value is only used during UI-less testing)
        self.running_time = 1
        self.take_breaks = True

    def create_options(self):
        """
        Use the OptionsBuilder to define the options for the bot. For each function call below,
        we define the type of option we want to create, its key, a label for the option that the user will
        see, and the possible values the user can select. The key is used in the save_options function to
        unpack the dictionary of options after the user has selected them.
        """
        self.options_builder.add_slider_option("running_time", "How long to run (minutes)?", 1, 300)
        self.options_builder.add_checkbox_option("take_breaks", "Take breaks?", [" "])


    def save_options(self, options: dict):
        """
        For each option in the dictionary, if it is an expected option, save the value as a property of the bot.
        If any unexpected options are found, log a warning. If an option is missing, set the options_set flag to
        False.
        """
        for option in options:
            if option == "running_time":
                self.running_time = options[option]
            elif option == "take_breaks":
                self.take_breaks = options[option] != []
            else:
                self.log_msg(f"Unknown option: {option}")
                print("Developer: ensure that the option keys are correct, and that options are being unpacked correctly.")
                self.options_set = False
                return
        self.log_msg(f"Running time: {self.running_time} minutes.")
        self.log_msg(f"Bot will{' ' if self.take_breaks else ' not '}take breaks.")
        self.log_msg("Options set successfully.")
        self.options_set = True

    def main_loop(self):
        """
        When implementing this function, you have the following responsibilities:
        1. If you need to halt the bot from within this function, call `self.stop()`. You'll want to do this
           when the bot has made a mistake, gets stuck, or a condition is met that requires the bot to stop.
        2. Frequently call self.update_progress() and self.log_msg() to send information to the UI.
        3. At the end of the main loop, make sure to set the status to STOPPED.

        Additional notes:
        Make use of Bot/RuneLiteBot member functions. There are many functions to simplify various actions.
        Visit the Wiki for more.
        """
        # Setup APIs
        # api_m = MorgHTTPSocket()
        # api_s = StatusSocket()

        # Main loop
        self.log_msg("Selecting inventory...")
        self.mouse.move_to(self.win.cp_tabs[3].random_point())
        self.mouse.click()

        start_time = time.time()
        end_time = self.running_time * 60
        n = 0
        p = random.randint(18, 23)
        self.log_msg("Thieving...")

        while time.time() - start_time < end_time:
            # -- Perform bot actions here --
            # 5% chance to take a break between clicks
            if rd.random_chance(probability=0.05) and self.take_breaks:
                self.take_break(max_seconds=130, fancy=True)


            stalls = self.get_all_tagged_in_rect(self.win.game_view, clr.PINK)
            for stall in stalls:
                n += 1
                if stall := self.get_nearest_tag(clr.PINK):
                    self.mouse.move_to(stall.random_point())
                    if not self.mouseover_text(contains="Steal"):
                        continue
                    self.mouse.click()
                    time.sleep(1.4)
                    if n >= p:
                        self.__empty_inv()
                        n = 0
                time.sleep(1.2)
            self.update_progress((time.time() - start_time) / end_time)

        self.update_progress(1)
        self.__logout("Finished.")

    def __logout(self, msg):
        self.log_msg(msg)
        self.logout()
        self.set_status(BotStatus.STOPPED)

    def __empty_inv(self):
        self.log_msg("Dropping inventory.")
        pag.keyDown("shift")
        cookingapple_img = imsearch.BOT_IMAGES.joinpath("items", "Cookingapple.png")
        while cookingapple_inv := imsearch.search_img_in_rect(cookingapple_img, self.win.control_panel):

            self.mouse.move_to(cookingapple_inv.random_point())
            self.mouse.click()
            time.sleep(.1)

        banana_img = imsearch.BOT_IMAGES.joinpath("items", "Banana.png")
        while banana_inv := imsearch.search_img_in_rect(banana_img, self.win.control_panel):

            self.mouse.move_to(banana_inv.random_point())
            self.mouse.click()
            time.sleep(.1)

        pineapple_img = imsearch.BOT_IMAGES.joinpath("items", "Pineapple.png")
        while pineapple_inv := imsearch.search_img_in_rect(pineapple_img, self.win.control_panel):

            self.mouse.move_to(pineapple_inv.random_point())
            self.mouse.click()
            time.sleep(.1)

        lemon_img = imsearch.BOT_IMAGES.joinpath("items", "lemon.png")
        while lemon_inv := imsearch.search_img_in_rect(lemon_img, self.win.control_panel):

            self.mouse.move_to(lemon_inv.random_point())
            self.mouse.click()
            time.sleep(.1)

        lime_img = imsearch.BOT_IMAGES.joinpath("items", "Lime.png")
        while lime_inv := imsearch.search_img_in_rect(lime_img, self.win.control_panel):

            self.mouse.move_to(lime_inv.random_point())
            self.mouse.click()
            time.sleep(.1)
        redberries_img = imsearch.BOT_IMAGES.joinpath("items", "Redberries.png")
        while redberries_inv := imsearch.search_img_in_rect(redberries_img, self.win.control_panel):

            self.mouse.move_to(redberries_inv.random_point())
            self.mouse.click()
            time.sleep(.1)
        jangerberries_img = imsearch.BOT_IMAGES.joinpath("items", "jangerberries.png")
        while jangerberries_inv := imsearch.search_img_in_rect(jangerberries_img, self.win.control_panel):

            self.mouse.move_to(jangerberries_inv.random_point())
            self.mouse.click()
            time.sleep(.1)

        strawberry_img = imsearch.BOT_IMAGES.joinpath("items", "strawberry.png")
        while strawberry_inv := imsearch.search_img_in_rect(strawberry_img, self.win.control_panel):
            self.mouse.move_to(strawberry_inv.random_point())
            self.mouse.click()
            time.sleep(.1)

        strangefruit_img = imsearch.BOT_IMAGES.joinpath("items", "strangefruit.png")
        while strangefruit_inv := imsearch.search_img_in_rect(strangefruit_img, self.win.control_panel):
            self.mouse.move_to(strangefruit_inv.random_point())
            self.mouse.click()
            time.sleep(.1)

        papayafruit_img = imsearch.BOT_IMAGES.joinpath("items", "papayafruit.png")
        while papayafruit_inv := imsearch.search_img_in_rect(papayafruit_img, self.win.control_panel):
            self.mouse.move_to(papayafruit_inv.random_point())
            self.mouse.click()
            time.sleep(.1)
        pag.keyUp("shift")
