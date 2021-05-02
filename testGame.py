import random

class testGame:
	default_action = "c"
	opponent_last_action = "c" # all implemented opponents start with cooperate by default
	game_name = "Test Game"
	action_list = ["c", "d"]
	payoff = {"cc": (3, 3),
			"dd": (1, 1),
			"cd": (1, 5),
			"dc": (5, 1)}
	player_count = 5 

	def get_action(opponent_num):
		if opponent_num == 0:
			return testGame.always_cooperate()
		elif opponent_num == 1:
			return testGame.always_defect()
		elif opponent_num == 2:
			return testGame.random_action()
		elif opponent_num == 3:
			return testGame.tit_for_tat(testGame.opponent_last_action)
		elif opponent_num == 4:
			return testGame.ms_copycat(testGame.opponent_last_action)

	def always_cooperate():
		return "c"

	def always_defect():
		return "d"

	def random_action():
		if random.uniform(0,1) > .5:
			return "c"
		else:
			return "d"

	def tit_for_tat(opponent_last_action):
		if opponent_last_action == "c":
			return "c"
		else:
			return "d"

	def ms_copycat(opponent_last_action):
		# mixed strategy favoring copy-cat with 80/20 or 20/80
		chance = random.uniform(0, 1)
		if opponent_last_action == "c":
			if chance <	.8:
				return "c"
			else:
				return "d"
		else:
			if chance < 0.8:
				return "d"
			else:
				return "c"
