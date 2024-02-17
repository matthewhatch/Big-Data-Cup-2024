import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

FILTER = ['Date', 'Clock', 'Period', 'Team','Event', 'Detail 1', 'Player', 'Player 2', 'Plt_X', 'Plt_Y', 'X Coordinate', 'Y Coordinate', 'Home Team']
EVENT_TYPE_MAP = {'Goal':'b', 'Shot': 'r'}
events = pd.read_csv('BDC_2024_Womens_Data.csv')
events['Plt_X'] = 200 - events['X Coordinate']
events['Plt_Y'] = 85 - events['Y Coordinate']
goals = events[events['Event'] == 'Goal'][FILTER]
shots = events[events['Event'] == 'Shot'][FILTER]

#merge goals and shots
shots_and_goals = pd.concat([shots, goals])
colors = shots_and_goals['Event'].map(EVENT_TYPE_MAP)

img = mpimg.imread('rink2.png')
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 200, 0, 85])
ax.set_xlim([0, 200])
ax.set_ylim([0, 85])

ax.scatter(shots_and_goals['Plt_X'], shots_and_goals['Plt_Y'], c=colors)
plt.show()