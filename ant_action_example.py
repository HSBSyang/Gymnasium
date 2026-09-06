import gymnasium as gym
import numpy as np


env = gym.make("Ant-v5", render_mode="human")
obs, info = env.reset(seed=0)


count = 0


try:
    while True:
        phase = np.sin(np.pi * count / 8)
        action = np.zeros(8, dtype=np.float32)


        action[1] =  0.25 * phase
        action[3] =  0.25 * phase
        obs, reward, terminated, truncated, info = env.step(action)
        count += 1


       
        if terminated or truncated:
            obs, info = env.reset()
            count = 0
finally:
    env.close()
