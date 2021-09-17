import plotly.figure_factory as ff
import pandas as pd
import random
import statistics
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")

data = df["reading_time"].tolist()

mean = statistics.mean(data)
deviation = statistics.stdev(data)

print("population mean: ", mean)
print("population deviation: ", deviation)

def random_set_of_mean(counter): 
    dataset = [] 
    for i in range(0, counter): 
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index] 
        dataset.append(value) 
    mean = statistics.mean(dataset) 
    return mean 

mean_list = [] 
for i in range(0,1000): 
    set_of_means= random_set_of_mean(300) 
    mean_list.append(set_of_means) 

sample_mean = statistics.mean(mean_list) 
print("Mean of sampling distribution : ",sample_mean )

sampleStandardDeviation = statistics.stdev(mean_list)
print("Deviation of sampling distribution : ",sampleStandardDeviation )

first_stdev_start,first_stdev_end = sample_mean - sampleStandardDeviation, sample_mean + sampleStandardDeviation
second_stdev_start,second_stdev_end = sample_mean - (sampleStandardDeviation * 2), sample_mean + (sampleStandardDeviation * 2)
third_stdev_start,third_stdev_end = sample_mean - (sampleStandardDeviation * 3), sample_mean + (sampleStandardDeviation * 3)

print("first deviation: ", first_stdev_start, first_stdev_end)
print("second deviation: ", second_stdev_start, second_stdev_end)
print("third deviation: ", third_stdev_start, third_stdev_end)

fig = ff.create_distplot([mean_list],["Reading Time"],show_hist=False) 
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines", name ="MEAN")) 

fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START")) 
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START")) 
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START")) 
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 

fig.show()