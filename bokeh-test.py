from bokeh.plotting import figure, output_file, show
import csv
# prepare some data

with open('test.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		print row[0], row[1]

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("airmonitor.html", title="Shinyei Dust Monitor")

TOOLS="resize"

# create a new plot with a title and axis labels
p = figure(tools=TOOLS, title="Shiney Dust Monitor", x_axis_type="datetime", x_axis_label='Time', y_axis_label='PM 2.5 Concentration')

# add a line renderer with legend and line thickness
p.line(x, y, legend="PM2.5", line_width=2)

# show the results
show(p)