from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("airmonitor.html", title="Shinyei Dust Monitor")

# create a new plot with a title and axis labels
p = figure(title="Shiney Dust Monitor", x_axis_label='Time', y_axis_label='PM 2.5 Concentration')

# add a line renderer with legend and line thickness
p.line(x, y, legend="PM2.5", line_width=2)

# show the results
show(p)