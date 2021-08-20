import os
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

base_dir = os.getcwd()

loop_path = os.path.join(base_dir, 'sim_log_raw.npy')
vector_path = os.path.join(base_dir, 'sim_log_np.npy')

loop_log = np.load(loop_path)
loop_log = [i*1000 for i in loop_log]
vector_log = np.load(vector_path)
vector_log = [i*1000 for i in vector_log]

plt.figure(figsize=(16, 8))
plt.plot(loop_log, color='gray')
plt.plot(vector_log, color='red')
plt.legend(['loop', 'vector'])
plt.xlabel('iteration')
plt.ylabel('execution time (ms)')
plt.savefig('sim_results.svg', dpi=192, bbox_inches='tight')


print(f'Stats for looping logic (mean, std): {np.mean(loop_log), np.std(loop_log)}')
print(f'Stats for vectorised logic (mean, std): {np.mean(vector_log), np.std(vector_log)}')