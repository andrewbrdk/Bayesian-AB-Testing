import numpy as np
import pandas as pd
import scipy.stats as stats
import plotly.graph_objects as go

np.random.seed(7)

d = np.arange(0, 30)

p = 0.05
N = 5000
ns = stats.binom.rvs(n=N, p=p, size=len(d))
cr = ns / N
p_drop = p*2/3
ns_drop = stats.binom.rvs(n=N, p=p_drop, size=len(d)//2)
cr_drop = ns_drop / N
p_inc = p*1.03
ns_inc = stats.binom.rvs(n=N, p=p_inc, size=len(d)//2)
cr_inc = ns_inc / N

fig = go.Figure()
fig.add_trace(go.Scatter(x=d, y=cr*100, 
                        name='Базовое значение', line_color='black'))
fig.add_trace(go.Scatter(x=d[len(d)//2-1:], 
                         y=np.concatenate([cr[[len(d)//2-1]]*100, cr_drop*100]),
                         name='-30%', line_color='black', line_dash='dash'))
fig.add_trace(go.Scatter(x=d[len(d)//2-1:], 
                         y=np.concatenate([cr[[len(d)//2-1]]*100, cr_inc*100]),
                         name='+3%', line_color='black', opacity=0.4, line_dash='dash'))
fig.update_layout(title='Эффект',
                  xaxis_title='Дни',
                  yaxis_title='Метрика',
                  xaxis_range=[0, len(d)-1],
                  xaxis_showticklabels=False,
                  yaxis_range=[1, 7],
                  yaxis_showticklabels=False,
                  hovermode="x",
                  barmode="group",
                  width=900)
fig.show()

#fig.write_image("./effect_size.png", scale=2)
