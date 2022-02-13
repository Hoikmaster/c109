import statistics
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
math_list =  df["math score"].to_list()
elar_list =  df["reading score"].to_list()

#Mean for height and weight
math_mean = statistics.mean(math_list)
elar_mean = statistics.mean(elar_list)
#Median for height and weight
math_median = statistics.median(math_list)
elar_median = statistics.median(elar_list)
#Mode for height and weight
math_mode = statistics.mode(math_list)
elar_mode = statistics.mode(elar_list)

print("Mean, median and mode of height is {},{} and {}".format(math_mean,math_median,math_mode))
print("Mean, median and mode of weight is {},{} and {}".format(elar_mean,elar_median,elar_mode))

#Standard deviation for height and weight
height_std_deviation = statistics.stdev(math_list)
weight_std_deviation = statistics.stdev(elar_list)
#1, 2 and 3 Standard Deviations for height
math_first_std_deviation_start, math_first_std_deviation_end = math_mean-height_std_deviation, math_mean+height_std_deviation
elar_first_std_deviation_start, elar_first_std_deviation_end = elar_mean-height_std_deviation, elar_mean+height_std_deviation


#Percentage of data within 1, 2 and 3 Standard Deviations for Height
math_list_of_data_within_1_std_deviation = [result for result in math_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
elar_list_of_data_within_1_std_deviation = [result for result in elar_list if result > elar_first_std_deviation_start and result < elar_first_std_deviation_end]

#Printing data for height and weight (Standard Deviation)
print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for elar lies within 1 standard deviation".format(len(elar_list_of_data_within_1_std_deviation)*100.0/len(elar_list)))
print("{}% of data for math lies within 2 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for elar lies within 2 standard deviation".format(len(elar_list_of_data_within_1_std_deviation)*100.0/len(elar_list)))
print("{}% of data for math lies within 3 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for elar lies within 3 standard deviation".format(len(elar_list_of_data_within_1_std_deviation)*100.0/len(elar_list)))