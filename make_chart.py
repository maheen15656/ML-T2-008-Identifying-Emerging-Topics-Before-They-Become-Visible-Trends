import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

res = pd.read_csv('expanding_window_results.csv')
df = pd.read_csv('prompt_engineering_corpus.csv')

fig, ax = plt.subplots(figsize=(8, 4.2))
time = res['year'] + res['month'] / 12
ax.plot(time, res['n_semantically_related_so_far'], marker='o', color='#2E5EAA',
        label='Semantic detector (TF-IDF cluster proximity)', linewidth=2)

df['time_f'] = df['year'] + df['month'] / 12
df_sorted = df.sort_values('time_f')
lit_cum, count = [], 0
for _, row in df_sorted.iterrows():
    if row['literal_hit']:
        count += 1
    lit_cum.append(count)
df_sorted['lit_cum'] = lit_cum
ax.plot(df_sorted['time_f'], df_sorted['lit_cum'], marker='s', color='#B0413E',
        label='Volume baseline (literal-term paper count)', linewidth=2)

ax.axvline(x=2019 + 9/12, color='#2E5EAA', linestyle='--', alpha=0.5, linewidth=1)
ax.axvline(x=2021 + 2/12, color='#B0413E', linestyle='--', alpha=0.5, linewidth=1)
ax.annotate('Semantic detector\nflags candidate cluster\n(Sep 2019)', xy=(2019 + 9/12, 2),
            xytext=(2019.3, 8), fontsize=8, color='#2E5EAA',
            arrowprops=dict(arrowstyle='->', color='#2E5EAA', alpha=0.6))
ax.annotate('Literal term\nfirst appears\n(Feb 2021)', xy=(2021 + 2/12, 1),
            xytext=(2021.5, 3), fontsize=8, color='#B0413E',
            arrowprops=dict(arrowstyle='->', color='#B0413E', alpha=0.6))

ax.set_xlabel('Year')
ax.set_ylabel('Cumulative count')
ax.set_title('Semantic detector vs. volume baseline: "prompt engineering" emergence (N=20 papers)')
ax.legend(loc='upper left', fontsize=9)
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('lead_time_chart.png', dpi=160)
print('Saved lead_time_chart.png')
