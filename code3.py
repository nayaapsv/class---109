import pandas as pd
import statistics
import csv
import plotly.figure_factory as pf
import plotly.graph_objects as go

df = pd.read_csv('StudentsPerformance.csv')
score = df['reading score'].to_list()

mean = statistics.mean(score)
std = statistics.stdev(score)

fstd_start , fstd_end = mean - std,mean + std
sstd_start , sstd_end = mean - (2*std),mean + (2*std)
tstd_start , tstd_end = mean - (3*std),mean + (3*std)

score_inside_fstd = [result for result in score if result>fstd_start and result<fstd_end]
score_inside_sstd = [result for result in score if result>sstd_start and result<sstd_end]
score_inside_tstd = [result for result in score if result>tstd_start and result<tstd_end]

print(format(len(score_inside_fstd)*100/len(score)))
print(format(len(score_inside_sstd)*100/len(score)))
print(format(len(score_inside_tstd)*100/len(score)))

fig = pf.create_distplot([score],['Score'] , show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.03], mode="lines", name="MEAN"))

fig.add_trace(go.Scatter(x=[fstd_start, fstd_start], y=[0, 0.03], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[fstd_end, fstd_end], y=[0, 0.03], mode="lines", name="Standard Deviation 1"))

fig.add_trace(go.Scatter(x=[sstd_start,sstd_start], y=[0, 0.03], mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[sstd_end, sstd_end], y=[0, 0.03], mode="lines", name="Standard Deviation 2"))

fig.add_trace(go.Scatter(x=[tstd_start,tstd_start], y=[0, 0.03], mode="lines", name="Standard Deviation 3"))
fig.add_trace(go.Scatter(x=[tstd_end, tstd_end], y=[0, 0.03], mode="lines", name="Standard Deviation 3"))
fig.show()