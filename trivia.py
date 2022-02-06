"""
Unofficial TADPOG Trivia Utility
Python 3.10.2
01/20/2022
Dane Burchette
"""

from random import choice, shuffle
from settings import Settings
import misc_func as mf

class Entry:

    def __init__(self, _dict):
        """Initialize Player's entry and answers for grading from dictionary"""
        self.responses = _dict
        self._create_variables()

    def __str__(self):
        """Printable string for Class Data"""
        return f"Name:\t\t{self.name}\nContact:\t{self.contact}\nDrawing:\t{self.drawing}\nScore:\t\t{self.points}\n"

    def __bool__(self):
        """Boolean value for class entry"""
        if self.drawing:
            return True
        elif not self.drawing:
            return False

    def _create_variables(self):
        """Generate Entry Variables"""
        self.name = self.responses["name"]
        self.contact = self.responses["contact"]
        self.drawing = self._drawing_correct()
        self.answers = self._load_answers()

    def _drawing_correct(self):
        """Correct String to Boolean"""
        match self.responses["drawing"]:
            case "True":
                return True
            case "False":
                return False
            case _:
                input(f"You fucked up {self.responses["name"]}'s entry!\nFix it.")

    def _load_answers(self):
        """Create dictionary of answers for Entry Class"""
        _dict, x = {},0
        while True:
            if self.responses.get(f"question_{x}", False):
                _dict[f"question{x}"] = self.responses[f"question_{x}"]
                x += 1
            else:
                break
        return _dict

    def score(self, answers, points):
        """Score answers"""
        self.points = 1
        for key in self.answers.keys():
            match self.answers[key]:
                case answers[key]:
                    self.points += int(points[key])
                case _:
                    pass
            
class Trivia:

    def __init__(self):
        """Initialize Trivia Drawing Class"""
        self.settings = Settings()
        self.trivia_dicts = mf.load_csv(self.settings.csvfilename)
        # Make Answer Key
        self.answers = self._gen_answers(0)
        self.points = self._gen_answers(1)
        # Make list of Entry Classes
        self.entries = self._gen_entries()
        # Now we're finally going to score!
        self.score_entries()
        self.drawing_list = self._gen_drawing()
        # Launch Menu for data confirmation and drawing
        self.menu()

    def menu(self):
        """User Menu"""
        menu_list = ["Unofficial TADPOG Trivia Utility:\n",
                    "1 - Draw Winners",
                    "2 - Print All Entries",
                    "3 - Print All Drawing Participants",
                    "4 - Print All For Fun Participants",
                    "Q - Quit without Drawing"]
        while True:
            mf._clear_screen()
            for option in menu_list:
                print(option)
            user_choice = input("\nEnter Choice: ")
            match user_choice:
                case "1":
                    # And the winners are...
                    mf._clear_screen()
                    self.winners = self._draw_all_winners()
                    self.print_winners()
                    break
                case "2":
                    mf._clear_screen()
                    self.print_entries()
                    input("Enter to Return to Menu")
                case "3":
                    mf._clear_screen()
                    self.print_entries(drawing=True)
                    input("Enter to Return to Menu")
                case "4":
                    mf._clear_screen()
                    self.print_entries(drawing=False)
                    input("Enter to Return to Menu")
                case ("Q"|"q"):
                    print("Closing Utility")
                    break
                case _:
                    pass


    def _gen_answers(self, value):
        """Return Dictionary with Answers if value = 0, Points if value = 1"""
        _dict, x = {},0
        while True:
            if self.trivia_dicts[value].get(f"question_{x}", False):
                _dict[f"question{x}"] = self.trivia_dicts[value][f"question_{x}"]
                x += 1
            else:
                break
        return _dict

    def _gen_entries(self):
        """Make list of entry classes"""
        number_of_entries = (len(self.trivia_dicts) - 1)
        _list = []
        while number_of_entries > 1:
            _list.append(Entry(self.trivia_dicts[number_of_entries]))
            number_of_entries -= 1
        return _list

    def score_entries(self):
        """Activate scoring function for each entry"""
        for entry in self.entries:
            entry.score(self.answers, self.points)

    def _gen_drawing(self):
        """Create list to draw winners from"""
        _list = []
        for entry in self.entries:
            if entry: #Entered in drawing
                _list += [entry] * entry.points
        return _list

    def _draw_all_winners(self):
        """Draw winners from pool"""
        _list, x = [], 0
        if self.settings.grand_prize:
            _list = self._draw_winners(self.settings.grand_prize_count, _list)
        _list = self._draw_winners(self.settings.stand_prize_count, _list)
        return _list
            
    def _draw_winners(self, count, _list):
        """Pick this many winners"""
        while count:
            shuffle(self.drawing_list)
            new_draw = choice(self.drawing_list)
            if new_draw not in _list:
                _list.append(new_draw)
                count -= 1
        return _list

    def print_winners(self):
        """Print out winners from drawing"""
        if self.settings.grand_prize:
            x = (self.settings.grand_prize_count - 1)
            while x >= 0:
                print(f"Grand Prize Winner\n{self.winners[x]}")
                x -= 1
        x = (self.settings.stand_prize_count * -1)
        while x < 0:
            print(f"Prize Winner\n{self.winners[x]}")
            x += 1

    def print_entries(self, drawing=None):
        """Print full list of entries"""
        match drawing:
            case None:
                # Print all
                for entry in self.entries:
                    print(entry)
            case True:
                # Print only those in drawing.
                for entry in self.entries:
                    if entry:
                        print(entry)
            case False:
                # Print only those not in drawing.
                for entry in self.entries:
                    if not entry:
                        print(entry)


if __name__ == "__main__":
    start = Trivia()