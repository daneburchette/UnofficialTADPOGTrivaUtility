Unofficial TADPOG Trivia Utility

Require CSV Layout:
Row 1 acts as Field Names.
	Layout "question_0,question_1...question_n,name,contact,drawing"
	question_0...n - Each represents question from Trivia
	name - Name of participant
	contact - Preferred method of contact of participant (i.e. phone number, e-mail, facebook, discord, etc.)
	drawing - Boolean, True if participating in prize drawing, False if participating only for fun
Row 2 acts as Answer Key.
	Answers are case sensitive and any manually added participant answers must be reformatted to conform.
Row 3 acts as Point Value.
	Integer values attributed to each question, reflecting subjective difficulty of each qeustion.
	Each point represents an extra entry of Participants Name into the drawing pool for a prize.
	Standard Point Value is 2 per question, 5 for difficult "Bonus Questions"
Rows 4+ act as individual Entries from Participants, collecting Answers, Name, Contact Info, and Participation Status

Modifying settings.py for use:

Set variable self.stand_prize_count to integer for number of standard prizes (i.e. Global Steam Codes)
Set variable self.grand_prize to boolean for presense of physical grand prize
Set variable self.grand_prize_count to integer for number of grand prizes (i.e. cool shit from Kris Vaughn)
	Note: this variable is unused if self.grand_prize is set to False, and is thus ignored.
Set variable self.csvfilename to string for name of the CSV file

Running Utility:

Once CSV is formatted and Settings are... set... Run trivia.py.
	The Script will return Option to print list of entries for verification
	Next user is given option to Draw Winners or cancel if error is found
	Finally winners are printed (if confirmed) and script terminates