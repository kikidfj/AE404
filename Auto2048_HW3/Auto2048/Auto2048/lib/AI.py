from lib.Grid import * 
import asyncio
import random
import multiprocessing
from multiprocessing import Process
from multiprocessing.managers import SharedMemoryManager
from multiprocessing import shared_memory
from os import cpu_count
import time
class AI:
	def __init__(self, multi_core=False):
		self.multi_core = multi_core
		self.init_dict()


	def multi_process_sim_game(self, game_state, proc_n_games, n_games, pilId = -1, pil_fmName = "", pil_scName = ""):
		cpuNum = cpu_count()
		divide_n_games = int(n_games/cpuNum)
		pilFm = shared_memory.ShareableList(name = pil_fmName)
		pilSc = shared_memory.ShareableList(name = pil_scName)
		for i in range(proc_n_games):
			result = self.sim_game(copy.deepcopy(game_state))
			pilFm[divide_n_games*pilId + i] = int(result[0])
			pilSc[divide_n_games*pilId + i] = result[1]
		pilFm.shm.close()
		pilFm.shm.unlink()
		pilSc.shm.close()
		pilSc.shm.unlink()


	def sim_game(self, game_state):
		temp_game = Grid(template = game_state)
		first_move = random.choice(list(Moves))
		temp_game.move(first_move)
		while True:
			if not temp_game.move(random.choice(list(Moves))): break
		return (first_move, temp_game.score())


	def next_move(self, game_state, n_games):
		

		if True:
			procList = []
			cpuNum = cpu_count()
			divide_n_games = int(n_games/cpuNum)
			smm = SharedMemoryManager()
			smm.start()
			pil_fm = smm.ShareableList([0]*n_games)
			pil_sc = smm.ShareableList([0]*n_games)
			for i in range(cpuNum-1):
				procList.append(Process(target = self.multi_process_sim_game,args = (game_state, divide_n_games, n_games, i, pil_fm.shm.name, pil_sc.shm.name)))
			for i in range(cpuNum-1):
				procList[i].start()
			self.multi_process_sim_game(game_state, n_games-(cpuNum-1)*divide_n_games, n_games, cpuNum-1, pil_fm.shm.name, pil_sc.shm.name)
			for i in range(cpuNum-1):
				procList[i].join()
			for i in range(len(pil_fm)):
				self.move_results[pil_fm[i]].append(pil_sc[i])
		else:
			results = []
			for i in range(n_games):
				results.append(self.sim_game(copy.deepcopy(game_state)))
			for result in results:
				self.move_results[result[0]].append(result[1])
		choices = []
		for i in Moves:
			if len(self.move_results[i]) == 0: continue
			choices.append((i, sum(self.move_results[i]) / len(self.move_results[i])))
		choices.sort(key=lambda x: x[1], reverse=True)
		self.init_dict()
		print(choices[0][0].name)
		return choices[0][0]


	def init_dict(self):
		self.move_results = {}
		for i in Moves:
			self.move_results[i] = []