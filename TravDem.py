import random

class TravelersDilemma:
	def __init__(self):
		# self.last = "o"
		self.default_action = 100
		self.opponent_last_action = 100 # all implemented opponents start with cooperate by default
		self.game_name = "Travelers Dilemma"
		self.action_list = [25, 40, 60, 80, 100]
		self.player_count = 5

	def get_payoff(self, p1_action, p2_action):
		if p1_action == p2_action:
			return p1_action
		elif p1_action < p2_action:
			return p1_action + self.action_list[0]
		else:
			return p2_action - self.action_list[0]

	def get_action(self, opponent_num):
		if opponent_num == 0:
			return self.low_bid()
		elif opponent_num == 1:
			return self.high_bid()
		elif opponent_num == 2:
			return self.random_bid()
		elif opponent_num == 3:
			return self.tit_for_tat(self.opponent_last_action)
		elif opponent_num == 4:
			return self.under_bid_with_jump(self.opponent_last_action)
		
	def low_bid(self):
		return self.action_list[0]

	def high_bid(self):
		return self.action_list[-1]

	def random_bid(self):
		index = random.randint(0, len(self.action_list) - 1)
		return self.action_list[index] 

	def tit_for_tat(self, opponent_last_action):
		return opponent_last_action

	def under_bid_with_jump(self, opponent_last_action):
		opponent_last_action_index = self.action_list.index(opponent_last_action)
		return self.action_list[opponent_last_action_index - 1]