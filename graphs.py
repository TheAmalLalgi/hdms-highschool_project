# Imports
import matplotlib.pyplot as plt
import pandas as pd

def barGraph(x_axis1, y_axis1, x_axis2, y_axis2) :
	plt.bar(x_axis1, len(y_axis1['Names']), label=x_axis1, color='tomato')
	plt.bar(x_axis2, len(y_axis2['Names']), label=x_axis2, color='teal')
	plt.xlabel('Classes')
	plt.ylabel('Strengths')
	plt.title('Class strengths graph - Bar Graph')
	plt.grid(True)
	plt.legend()
	plt.show()

def pieChart(percent, description) :
	colors = ['#FF5555', '#50FA7B', '#FFCB6B', '#82AAFF', '#C792EA', '#8BE9FD']
	explode = [0, 0, 0, 0, 0, 0.1]
	plt.pie(percent, labels = description, autopct='%1.1f%%', colors=colors, explode=explode, shadow = True)
	plt.title('Class strengths graph - Pie Chart')
	plt.show()

def histogram(x_axis, y_axis) :
	plt.hist([7, 8, 9, 10, 11, 12], bins = [7, 8, 9, 10, 11, 12], weights = x_axis, color='#50FA7B', edgecolor='#141414')
	plt.xlabel('Classes')
	plt.ylabel('Strengths')
	plt.title('Class strengths graph - Histogram')
	plt.grid(True)
	plt.show()
