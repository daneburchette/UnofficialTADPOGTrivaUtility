"""
TADPOG Trivia Utility: Settings Module
Python 3.9
01/20/2022
Dane Burchette
"""

class Settings:
	
	def __init__(self):
		"""Initialize Settings"""
		# Number of Normal Prizes to be drawn. Typically Steam Codes
		self.stand_prize_count = 3
		# Will there be a gand prize drawing? And how many?
		self.grand_prize = True
		self.grand_prize_count = 1
		"""
		CSV Trivia Results file information:
		Add first row with correct answers
		Add second row with scores for each answer.
		Manually edit answers to conform to format of answers when needed.
		"""
		self.csvfilename = "test.csv"