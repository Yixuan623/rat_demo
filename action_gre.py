import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
num_frames=500
duration=1.0
t = np.linspace(0, duration, num_frames)  # 时间序列 (0 → 1秒)
freq = 1  
amplitude = 0.1  
a1 = amplitude * np.sin(2 * np.pi * freq * t) 

# 可视化控制点列
plt.plot(a1)
plt.title("Control Points")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid()
plt.show()

# 输出控制点列
print(a1)