import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import make_interp_spline, BSpline

plt.style.use('seaborn')

columns = {
    'Q': 'Q (чел. / день)',
    'FC': 'FC (т.р. / год)',
    'VC': 'VC (т.р. / год)',
    'TC': 'TC (т.р. / год)',
    'MC': 'MC (т.р. / чел.)',
    'AFC': 'AFC (т.р. / чел.)',
    'AVC': 'AVC (т.р. / чел.)',
    'ATC': 'ATC (т.р. / чел.)',
}

data = {
    'Q': [1, 100, 200, 300, 400, 500],
    'FC': [1000, 1000, 1000, 1000, 1000, 1000],
    'VC': [0, 700, 1000, 1300, 1700, 2500],
}
data = pd.DataFrame(data)

data['TC'] = data['FC'] + data['VC']

d_TC = data['TC'][1:] - list(data['TC'][:-1])
d_Q = data['Q'][1:] - list(data['Q'][:-1])
MC = d_TC / d_Q
data['MC'] = ['-'] + [round(x, 3) for x in MC]

AFC = data['FC'][1:] / list(data['Q'][1:])
data['AFC'] = ['-'] + [round(x, 3) for x in AFC]

AVC = data['VC'][1:] / list(data['Q'][1:])
data['AVC'] = ['-'] + [round(x, 3) for x in AVC]

ATC = data['AFC'][1:] + list(data['AVC'][1:])
data['ATC'] = ['-'] + [round(x, 3) for x in ATC]

def interpolate(x, y):
    interpolator = make_interp_spline(x, y, k=2)
    x = np.linspace(min(x), max(x), 300)
    y = interpolator(x)
    return x, y

for costs in ['FC', 'VC', 'TC']:
    x = data['Q']
    y = data[costs]
    
    x, y = interpolate(x, y)
    
    plt.plot(x, y, label=columns[costs])
plt.legend()
plt.title('График общих затрат')
plt.xlabel(columns['Q'])
#plt.show()
plt.savefig('./common.png')
plt.clf()

for costs in ['MC', 'AFC', 'AVC', 'ATC']:
    
    x = data['Q'][1:]
    y = data[costs][1:]
    
    x, y = interpolate(x, y)
    
    plt.plot(x, y, label=columns[costs])
plt.legend()
plt.title('График средних и маржинальных')
plt.xlabel(columns['Q'])
#plt.show()
plt.savefig('./averages.png')

data.columns = [columns[column] for column in data.columns]
data.to_markdown('./data.md', index=False)
