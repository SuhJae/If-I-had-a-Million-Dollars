import matplotlib.pyplot as plt
import numpy as np
import math

principal = 255000 # initial investment
year = np.arange(0, 54)

# ==========================
# Functions
# ==========================

# Invest in Index Funds earns 3% annual interest compounded continuously
index_funds = principal * math.e ** (0.03 * year)
# they offer 5% simple interest for investments
new_bank = principal * (1 + 0.05 * year)


# create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(year, new_bank, label='New Bank', color='#410B69')
ax.plot(year, index_funds, label='Index Funds', color='#1B19CA')

# set x and y labels
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Savings Account Balance', fontsize=14)
ax.ticklabel_format(style='plain', useOffset=False, axis='y')

# set title and legend
ax.grid(True)
ax.legend(loc='upper left', fontsize=20)
# make legend background transparent
ax.legend(framealpha=0)


# make chart look nicer
#set style to ggplot
plt.style.use('ggplot')
# set background color to #FAFCFF
ax.set_facecolor('#FAFCFF')
# also set figure background color to #FAFCFF
fig.set_facecolor('#FAFCFF')

# set grid and text color to #01050A
# ax.grid(color='#01050A')
ax.spines['bottom'].set_color('#01050A')
ax.spines['top'].set_color('#01050A')
ax.spines['right'].set_color('#01050A')
ax.spines['left'].set_color('#01050A')
ax.tick_params(axis='x', colors='#01050A')
ax.tick_params(axis='y', colors='#01050A')

# set font from the font file (path to font file: 'fonts/Inter-Regular.ttf')

# add text and dots for values at specific years (10, 20, 50)
text_years = [10, 20, 50]

for year_val in text_years:
    index_funds_val = principal * math.e ** (0.03 * year_val)
    new_bank_val = principal * (1 + 0.05 * year_val)

    index_funds_text = ax.text(year_val, index_funds_val, f'{int(index_funds_val):,}' + ' ', ha='right', fontsize=12)
    new_bank_text = ax.text(year_val, new_bank_val, f'{int(new_bank_val):,}' + ' ', ha='right', fontsize=12)

    new_bank_color = ax.get_lines()[0].get_color()
    index_funds_color = ax.get_lines()[1].get_color()

    ax.plot(year_val, index_funds_val, 'o', color=index_funds_color, markersize=4)
    ax.plot(year_val, new_bank_val, 'o', color=new_bank_color, markersize=4)

    index_funds_text.set_color(index_funds_color)
    new_bank_text.set_color(new_bank_color)

# find the intersection point and add a dot and text

# find the intersection point

intersection_point = np.argwhere(np.diff(np.sign(index_funds - new_bank))).flatten()
# remove the first element
intersection_point = np.delete(intersection_point, 0)

# plot the intersection point and
ax.plot(year[intersection_point], index_funds[intersection_point], 'o', color='#01050A', markersize=8)
ax.text(year[intersection_point], index_funds[intersection_point], f'{int(year[intersection_point]):,}' + ' ', ha='right', fontsize=16, color='#01050A')

plt.show()

# save figure
fig.savefig('savings_account.png', dpi=300, bbox_inches='tight')