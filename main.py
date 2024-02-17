import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.lines import Line2D

FILTER = ['Date', 'Clock', 'Period', 'Team','Event', 'Detail 1', 'Player', 'Player 2', 'Plt_X', 'Plt_Y', 'X Coordinate', 'Y Coordinate', 'Home Team']
TEAM_COLOR_MAP = {'Women - United States':'b', 'Women - Canada':'r'}
EVENT_TYPE_MAP = {'Goal':'*', 'Zone Entry': 's'}
events = pd.read_csv('BDC_2024_Womens_Data.csv')

# plot x and y based on home team and period
# if Home Team matches Team  and period is odd, flip the x and y coordinates
# if Home Team does not match Team and period is even, flip the x and y coordinates
events['Plt_X'] = events.apply(lambda row: 200 - row['X Coordinate'] if (row['Team'] == row['Home Team'] and row['Period'] % 2 == 1) or (row['Team'] != row['Home Team'] and row['Period'] % 2 == 0) else row['X Coordinate'], axis=1)
events['Plt_Y'] = events.apply(lambda row: 85 - row['Y Coordinate'] if (row['Team'] == row['Home Team'] and row['Period'] % 2 == 1) or (row['Team'] != row['Home Team'] and row['Period'] % 2 == 0) else row['Y Coordinate'], axis=1) 

zone_entry = events[events['Event'] == 'Zone Entry']
carried = zone_entry[zone_entry['Detail 1'] == 'Carried'][FILTER]
dumped = zone_entry[zone_entry['Detail 1'] == 'Dumped'][FILTER]
played = zone_entry[zone_entry['Detail 1'] == 'Played'][FILTER]

# lets get all the Zone Entry events that are carried and see the 5 events before and after
for index, row in played.iterrows():
    # save events plus the seven events after
    sorrounding_events = events.loc[index:index + 10][FILTER]
    # print if one of the Events is a goal
    if 'Goal' in sorrounding_events['Event'].values:
        # lets plot all the x and y coordinates from sourrounding events on rink_coords.png
        print(sorrounding_events)
        print('-'*150)

        img = mpimg.imread('rink.png')
        fig, ax = plt.subplots()
        ax.imshow(img, extent=[0, 200, 0, 85])
        ax.set_xlim([0, 200])
        ax.set_ylim([0, 85])
        
        colors = sorrounding_events['Team'].map(TEAM_COLOR_MAP)  # Map the team names to colors
        for event, marker in EVENT_TYPE_MAP.items():
            event_data = sorrounding_events[sorrounding_events['Event'] == event]
            ax.scatter(event_data['Plt_X'], event_data['Plt_Y'], c=event_data['Team'].map(TEAM_COLOR_MAP), marker=marker, s=100)
        
        default_data = sorrounding_events[~sorrounding_events['Event'].isin(EVENT_TYPE_MAP.keys())]
        ax.scatter(default_data['Plt_X'], default_data['Plt_Y'], c=default_data['Team'].map(TEAM_COLOR_MAP), marker='o')
        
        # Create a legend
        legend_elements = [Line2D([0], [0], marker='o', color='w', label=team, markerfacecolor=color, markersize=10) 
                  for team, color in TEAM_COLOR_MAP.items()]
        ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0.65, 1.5))
        
        plt.savefig(f'output/scoring-play-{index}.png')
        # plt.show()
