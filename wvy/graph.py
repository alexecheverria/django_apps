import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from wvy import Wvy_Wav

class Graph:
	background = ''
	gridlines = ''
	title = ''
	xlim = []
	ylim = []
	plot = None #matplot obj

	def getBackground(self):
		return self.background

	def setBackground(self, new_background):
		self.background = new_background

	def getGridlines(self):
		return self.gridlines

	def setGrindLines(self, new_gridlines):
		self.gridlines = new_gridlines

	def getTitle(self):
		return self.title

	def setTitle(self, new_title):
		self.title = new_title

	def getXLim(self, new_xlim):
		return self.xlim

	def setXLim(self, new_xlim):
		self.xlim = new_xlim

	def getYLim(self, new_ylim):
		return self.ylim

	def setYLim(self, new_ylim):
		self.ylim = new_ylim

	def getPlot(self):
		return self.plot

	def setPlot(self, new_plot):
		self.plot = new_plot

	def plotWave(self, wave_name):
		plot = plt.plot(wave_name.getAmplitudes(), wave_name.getTime(),linestyle=wave_name.getLine_Type(),
		color=wave_name.getColour(), linewidth=(getLine_Width()))
		plot.plt.title(self.getTitle())
		plot.set_axis_bgcolor(self.getBackground())
		if(xlim != 'auto'):
			plot.set_xlim(self.getXLim())
		if(ylim != 'auto'):
			plot.set_ylim(self.getYLim())
		plot.grid(self.getGridlines())
		self.setPlot(plot)

	def savePlotToPNG(self):
		print('Saving file')
		self.getPlot().plt.savefig(self.getTitle(), '.png')
		print('Done Saving')
