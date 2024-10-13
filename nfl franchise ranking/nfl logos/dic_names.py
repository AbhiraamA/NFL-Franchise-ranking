image_paths = {
    
    'Arizona Cardinals':"analytics/nfl logos/CARDS.png",
    'Atlanta Falcons' : "analytics/nfl logos/atl.png",
    'Baltimore Ravens':"analytics/nfl logos/bmore.png",
    'Buffalo Bills':"analytics/nfl logos/buffalobills.png",
    'Carolina Panthers' : "analytics/nfl logos/car.png",
    'Chicago Bears' : "analytics/nfl logos/dabears.png",
    'Cincinnati Bengals' : "analytics/nfl logos/bengals.png",
    'Cleveland Browns' : "analytics/nfl logos/browns.png",
    'Dallas Cowboys' : "analytics/nfl logos/dal.png",
    'Denver Broncos' : "analytics/nfl logos/denver.png",
    'Detroit Lions' : "analytics/nfl logos/det.png",
    'Green Bay Packers' : "analytics/nfl logos/gbp.png",
    'Houston Texans' : "analytics/nfl logos/htx.png",
    'Indianapolis Colts' : "analytics/nfl logos/colts.png",
    'Jacksonville Jaguars': "analytics/nfl logos/jags.png",
    'Kansas City Chiefs': "analytics/nfl logos/kc.png",
    'Las Vegas Raiders' : "analytics/nfl logos/lv.png",
    'Los Angeles Chargers': "analytics/nfl logos/lachargers.png",
    'Los Angeles Rams' : "analytics/nfl logos/larams.png",
    'Miami Dolphins': "analytics/nfl logos/miamidolphins.png",
    'Minnesota Vikings' : "analytics/nfl logos/min.png",
    'New England Patriots' : "analytics/nfl logos/min.png",
    "New Orleans Saints" : "analytics/nfl logos/NO.png",
    "New York Giants" : "analytics/nfl logos/nyg.png",
    "New York Jets" : "analytics/nfl logos/nyjets.png",
    "Philadelphia Eagles" : "analytics/nfl logos/phil.png",
    'Pittsburgh Steelers' : "analytics/nfl logos/pittsburgh.png",
    'San Francisco 49ers' : "analytics/nfl logos/sf49.png",
    'Seattle Seahawks' : "analytics/nfl logos/seahW.png",
    'Tampa Bay Buccaneers' : "analytics/nfl logos/tamp.png",
    'Tennessee Titans' : "analytics/nfl logos/tennesee.png",
    'Washington Commanders':"analytics/nfl logos/wash.png"

}


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the data
df = pd.read_excel("analytics/NFL franchise rankings.xlsx")

# Define weights for the metrics
weights = {
    'W-L%': .75,
    'W plyf': 3,      
    'L plyf': -1,    
    'Non sb chmp': 15,       
    'SBwl': 23,
    'SBwl app' : 12,
    'Conf': 10,
    'Div': 3,
    'Yr plyf': 2
}

# Calculate the total score for each franchise
df['Score'] = 0
for metric, weight in weights.items():
    df['Score'] += df[metric] * weight

# Sort by Score and calculate Score per time
df_sorted = df.sort_values(by='Score', ascending=False)
df_sorted['Score per time'] = df_sorted['Score'] / df_sorted['Tot yrs']
df_sorted_time = df_sorted.sort_values(by='Score per time', ascending=False)

# Get top 5 and bottom 5 for regular ranking
top_5 = df_sorted.head(5)
bottom_5 = df_sorted.tail(5)

# Get top 5 and bottom 5 for time-based ranking
top_5_time = df_sorted_time.head(5)
bottom_5_time = df_sorted_time.tail(5)

# Helper function to get color gradients
def get_gradient_color(base_color, rank, total):
    # Get RGB components
    r, g, b = base_color
    factor = (rank - 1) / (total - 1)
    return (int(r + (255 - r) * factor), int(g + (255 - g) * factor), int(b + (255 - b) * factor))

# Function to add image
def add_image(ax, path, xy):
    img = Image.open(path)
    ax.imshow(img)
    ax.axis('off')
    ax.set_position([xy[0], xy[1], 0.1, 0.1])

# Create a figure
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

image_paths = {
    
    'Arizona Cardinals':"analytics/nfl logos/CARDS.png",
    'Atlanta Falcons' : "analytics/nfl logos/atl.png",
    'Baltimore Ravens':"analytics/nfl logos/bmore.png",
    'Buffalo Bills':"analytics/nfl logos/buffalobills.png",
    'Carolina Panthers' : "analytics/nfl logos/car.png",
    'Chicago Bears' : "analytics/nfl logos/dabears.png",
    'Cincinnati Bengals' : "analytics/nfl logos/bengals.png",
    'Cleveland Browns' : "analytics/nfl logos/browns.png",
    'Dallas Cowboys' : "analytics/nfl logos/dal.png",
    'Denver Broncos' : "analytics/nfl logos/denver.png",
    'Detroit Lions' : "analytics/nfl logos/det.png",
    'Green Bay Packers' : "analytics/nfl logos/gbp.png",
    'Houston Texans' : "analytics/nfl logos/htx.png",
    'Indianapolis Colts' : "analytics/nfl logos/colts.png",
    'Jacksonville Jaguars': "analytics/nfl logos/jags.png",
    'Kansas City Chiefs': "analytics/nfl logos/kc.png",
    'Las Vegas Raiders' : "analytics/nfl logos/lv.png",
    'Los Angeles Chargers': "analytics/nfl logos/lachargers.png",
    'Los Angeles Rams' : "analytics/nfl logos/larams.png",
    'Miami Dolphins': "analytics/nfl logos/miamidolphins.png",
    'Minnesota Vikings' : "analytics/nfl logos/min.png",
    'New England Patriots' : "analytics/nfl logos/min.png",
    "New Orleans Saints" : "analytics/nfl logos/NO.png",
    "New York Giants" : "analytics/nfl logos/nyg.png",
    "New York Jets" : "analytics/nfl logos/nyjets.png",
    "Philadelphia Eagles" : "analytics/nfl logos/phil.png",
    'Pittsburgh Steelers' : "analytics/nfl logos/pittsburgh.png",
    'San Francisco 49ers' : "analytics/nfl logos/sf49.png",
    'Seattle Seahawks' : "analytics/nfl logos/seahW.png",
    'Tampa Bay Buccaneers' : "analytics/nfl logos/tamp.png",
    'Tennessee Titans' : "analytics/nfl logos/tennesee.png",
    'Washington Commanders':"analytics/nfl logos/wash.png"

}

for i, (index, row) in enumerate(top_5.iterrows()):
    color = get_gradient_color((0, 255, 0), i+1, 5)  # Green gradient
    axes[0].barh(i, row['Score'], color=np.array(color)/255)
    axes[0].text(0.02, i, f"{i+1}.", va='center', ha='right', fontsize=12, fontweight='bold')
    axes[0].text(0.15, i, row['Tm'], va='center', ha='left', fontsize=12)
    if row['Tm'] in image_paths:
        add_image(axes[0], image_paths[row['Tm']], xy=(0.1, i-0.4))
    axes[0].text(0.9, i, f"{row['Score']:.2f}", va='center', ha='left', fontsize=12)

axes[0].set_title('Top 5 by Score')
axes[0].invert_yaxis()
axes[0].axis('off')

# Plot Bottom 5 by Score
for i, (index, row) in enumerate(bottom_5.iterrows()):
    color = get_gradient_color((255, 0, 0), i+1, 5)  # Red gradient
    axes[1].barh(i, row['Score'], color=np.array(color)/255)
    axes[1].text(0.02, i, f"{len(df) - 5 + i + 1}.", va='center', ha='right', fontsize=12, fontweight='bold')
    axes[1].text(0.15, i, row['Tm'], va='center', ha='left', fontsize=12)
    if row['Tm'] in image_paths:
        add_image(axes[1], image_paths[row['Tm']], xy=(0.1, i-0.4))
    axes[1].text(0.9, i, f"{row['Score']:.2f}", va='center', ha='left', fontsize=12)

axes[1].set_title('Bottom 5 by Score')
axes[1].invert_yaxis()
axes[1].axis('off')

plt.tight_layout()
plt.show()
