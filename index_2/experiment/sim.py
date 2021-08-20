def orig(size: int = 600, sim_log: str = 'sim_log_raw.npy'):
	import os
	import time
	import numpy as np

	T0 = time.time()
	log = np.array([])
	sim_log_path = os.path.join(os.getcwd(), sim_log)

	inputs = np.random.rand(size,)
	weights = np.random.rand(size, size)
	biases = np.random.rand(size,)
	outputs = []

	# calc
	for n_w, n_b in zip(weights, biases):
		n_op = 0
		for ip, w in zip(inputs, n_w):
			n_op += ip * w
		n_op += n_b
		outputs.append(n_op)
	if len(outputs) != size:
		raise Exception(f"Whoopsie! Shape mismatch. Correct logic.")
	# log
	if os.path.exists(sim_log_path):
		log = np.load(sim_log_path)
	log = np.append(log, round(time.time() - T0, 3))
	np.save(sim_log_path, log)


def np_opt(size: int = 600, sim_log: str = 'sim_log_np.npy'):
	import os
	import time
	import numpy as np

	T0 = time.time()
	log = np.array([])
	sim_log_path = os.path.join(os.getcwd(), sim_log)

	inputs = np.random.rand(size,)
	weights = np.random.rand(size, size)
	biases = np.random.rand(size,)

	# calc
	outputs = np.dot(weights, inputs) + biases
	if len(outputs) != size:
		raise Exception(f"Whoopsie! Shape mismatch. Correct logic.")
	# log
	if os.path.exists(sim_log_path):
		log = np.load(sim_log_path)
	log = np.append(log, round(time.time() - T0, 3))
	np.save(sim_log_path, log)

if __name__=='__main__':
	import sys
	size = 600
	try:
		if sys.argv[1] == 'loop':
			if len(sys.argv) > 2:
				size = int(sys.argv[2])
			orig(size)
		elif sys.argv[1] == 'vector':
			if len(sys.argv) > 2:
				size = int(sys.argv[2])
			np_opt(size)
		else:
			sys.stderr.write(f'Usage: python sim.py [loop, vector] [(optional) size]\n')
			raise KeyError(f'Unknown argument {sys.argv[1] if len(sys.argv) > 1 else None}')
	except IndexError as exc:
		sys.stderr.write(f'error: Usage: python sim.py [loop, vector] [(optional) size]\n')