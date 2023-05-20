import matplotlib.pyplot as plt
import numpy as np
import math

principal = 255000 # initial investment
year = np.arange(0, 54)

# ==========================
# Functions
# ==========================

# Savings Account earns 1.5% annual interest compounded annually
savings_account = principal * (1 + 0.015) ** year
# Invest in Bonds earns 2% annual interest compounded quarterly
bonds = principal * (1 + (0.02 / 4)) ** (year * 4)
# Invest in Index Funds earns 3% annual interest compounded continuously
index_funds = principal * math.e ** (0.03 * year)


# create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(year, savings_account, label='Savings Account', color='#01050A')
ax.plot(year, bonds, label='Bonds', color='#410B69')
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
    savings_val = principal * (1 + 0.015) ** year_val
    bonds_val = principal * (1 + (0.02 / 4)) ** (year_val * 4)
    index_funds_val = principal * math.e ** (0.03 * year_val)

    savings_text = ax.text(year_val, savings_val, f'{int(savings_val):,}' + ' ', ha='right', fontsize=12)
    bonds_text = ax.text(year_val, bonds_val, f'{int(bonds_val):,}' + ' ', ha='right', fontsize=12)
    index_funds_text = ax.text(year_val, index_funds_val, f'{int(index_funds_val):,}' + ' ', ha='right',
                               fontsize=12)

    savings_color = ax.get_lines()[0].get_color()
    bonds_color = ax.get_lines()[1].get_color()
    index_funds_color = ax.get_lines()[2].get_color()

    ax.plot(year_val, savings_val, 'o', color=savings_color, markersize=4)
    ax.plot(year_val, bonds_val, 'o', color=bonds_color, markersize=4)
    ax.plot(year_val, index_funds_val, 'o', color=index_funds_color, markersize=4)

    savings_text.set_color(savings_color)
    bonds_text.set_color(bonds_color)
    index_funds_text.set_color(index_funds_color)

plt.show()

# save figure
fig.savefig('savings_account.png', dpi=300, bbox_inches='tight')