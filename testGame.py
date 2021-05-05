import random

class testGame:
	def __init__(self):
		self.default_action = "c"
		self.opponent_last_action = "c" # all implemented opponents start with cooperate by default
		self.game_name = "Test Game"
		self.action_list = ["c", "d"]
		self.payoff = {"cc": (3, 3),
					"dd": (1, 1),
					"cd": (1, 5),
					"dc": (5, 1)}
		self.player_count = 5 

	def get_payoff(self, p1_action, p2_action):
		return self.payoff[p1_action + p2_action][0]

	def get_action(self, opponent_num):
		if opponent_num == 0:
			return self.always_cooperate()
		elif opponent_num == 1:
			return self.always_defect()
		elif opponent_num == 2:
			return self.random_action()
		elif opponent_num == 3:
			return self.tit_for_tat(self.opponent_last_action)
		elif opponent_num == 4:
			return self.ms_copycat(self.opponent_last_action)

	def always_cooperate(self):
		return "c"

	def always_defect(self):
		return "d"

	def random_action(self):
		if random.uniform(0,1) > .5:
			return "c"
		else:
			return "d"

	def tit_for_tat(self, opponent_last_action):
		return opponent_last_action

	def ms_copycat(self, opponent_last_action):
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
