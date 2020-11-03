import pandas
import math

def displayInfo(arr, colNumber):
	maxVal = max(arr)
	minVal = min(arr)
	average = sum(arr)/len(arr)
	print("For " + colNumber)
	print("Max: " + str(maxVal))
	print("Min: " + str(minVal))
	print("Average: " + str(average))
	print()

def main():
	file = pandas.read_excel("daily_python_excelsheet.xlsx", header=None).to_numpy()
	col0 = [item for item in file[:,0] if math.isnan(item) is False]
	col1 = [item for item in file[:,1] if math.isnan(item) is False]
	col2 = [item for item in file[:,2] if math.isnan(item) is False]
	allData = col0 + col1 + col2

	displayInfo(col0, "column 0")
	displayInfo(col1, "column 1")
	displayInfo(col2, "column 2")
	displayInfo(allData, "all columns")

main()