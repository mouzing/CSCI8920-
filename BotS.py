import random

class BattleOfTheSexes:
	def __init__(self):
		self.last = "o"
		self.default_action = "o"
		self.opponent_last_action = "o" # all implemented opponents start with cooperate by default
		self.game_name = "Battle of the Sexes"
		self.action_list = ["o", "f"]
		self.payoff = {"oo": (3, 2), # copied from wikipedia entry
					"ff": (2, 3),
					"of": (1, 1),
					"fo": (0, 0)}
		self.player_count = 5 

	def get_payoff(self, p1_action, p2_action):
		return self.payoff[p1_action + p2_action][0]

	def get_action(self, opponent_num):
		if opponent_num == 0:
			return self.always_opera()
		elif opponent_num == 1:
			return self.always_football()
		elif opponent_num == 2:
			return self.random_action()
		elif opponent_num == 3:
			return self.tit_for_tat(self.opponent_last_action)
		elif opponent_num == 4:
			return self.flip_flop()

	def always_opera(self):
		return "o"

	def always_football(self):
		return "f"

	def random_action(self):
		if random.uniform(0,1) > .5:
			return "o"
		else:
			return "f"

	def tit_for_tat(self, opponent_last_action):
		return opponent_last_action

	def flip_flop(self):
		if self.last == "o":
			self.last = "f"
			return "f" 
		else:
			self.last = "o"
			return "o"
