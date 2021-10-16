import pandas as pd
import statistics
import csv

reader = pd.read_csv('height-weight.csv')
heightList = reader['Height(Inches)'].to_list()

height_mean = statistics.mean(heightList)
height_meadian = statistics.median(heightList)
height_mode = statistics.mode(heightList)

print("Mean,Median and Mode For The Data is {},{},{}",format(height_mean,height_meadian,height_mode))

height_std_devi = statistics.stdev(heightList)

height_first_std_devi_start,height_first_std_devi_end = height_mean-height_std_devi,height_mean+height_std_devi
height_second_std_devi_start,height_second_std_devi_end = height_mean-(2*height_std_devi),height_mean+(2*height_std_devi)
height_third_std_devi_start,height_third_std_devi_end = height_mean-(3*height_std_devi),height_mean+(3*height_std_devi)

height_list_of_1st_data = [result for result in heightList if result > height_first_std_devi_start and result > height_first_std_devi_end]
height_list_of_2nd_data = [result for result in heightList if result > height_second_std_devi_start and result > height_second_std_devi_end]
height_list_of_3rd_data = [result for result in heightList if result > height_third_std_devi_start and result > height_first_std_devi_end]

print("{}% Standard Deviation of the Data 1 ",format(len(height_list_of_1st_data))*100.0/len(heightList))
print("{}% Standard Deviation of the Data 2 ",format(len(height_list_of_2nd_data))*100.0/len(heightList))
print("{}% Standard Deviation of the Data 3 ",format(len(height_list_of_3rd_data))*100.0/len(heightList))

