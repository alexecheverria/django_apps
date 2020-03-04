from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	project_name = models.CharField(max_length=100)
	graphs = {}
	notes = {}
	files = {}
	waves = {}

	def __str__(self):
		return f'{self.user.username} User'

	#Project Name Methods
	def getProject_Name(self):
		return self.project_name

	def setProject_Name(self, new_project_name):
		self.project_name = new_project_name

	#Project Graph Methods
	def getGraphs(self):
		return self.graphs

	def setGraphs(self, new_graphs):
		self.graphs = new_graphs

	def addGraph(self, new_graph, new_graph_name):
		self.getGraphs()[new_graph_name] = new_graph

	def deleteGraph(self, graph_name):
		try:
			del self.getGraphs()[graph_name]	
		except:
			print(graph_name, " doesn't exist in this project")

	#Project Note Methods
	def getNotes(self):
		return self.notes

	def setNotes(self, new_notes):
		self.notes = new_notes

	def addNote(self, new_note, new_note_name):
		self.getGraphs()[new_note_name] = new_note

	def deleteNote(self, note_name):
		try:
			del self.getNotes()[note_name]	
		except:
			print(note_name, " doesn't exist in this project")

	#Project File Methods	
	def getFiles(self):
		return self.files	

	def setFiles(self, new_files):
		self.files = new_files

	def addFile(self, new_file, new_filename):
		self.getFiles()[new_filename] = new_file

	def deleteFile(self, filename):
		try:
			del self.getFiles()[filename]	
		except:
			print(filename, " doesn't exist in this project")

	#Wave Methods
	def getWaves(self):
		return self.waves

	def setWaves(self, new_waves):
		self.waves = new_waves

	def addWave(self, new_wave, new_wave_name):
		self.getWaves()[new_wave_name] = new_wave

	def deleteWave(self, wave_name):
		try:
			del self.getWaves()[wave_name]	
		except:
			print(wave_name, " doesn't exist in this project")

	def processWave(self, transform_coes, wave_name):
		try:
			self.getWaves()[wave_name]
		except:
			print("Issue with wave")
		ampl_x = self.getWaves()[wave_name].getAmplitudes()[:]
		ampl_y = self.getWaves()[wave_name].getAmplitudes()[:]
		length = self.getWaves()[wave_name].getLength()
		for i in range(length):
			#print('iteration: ', i)
			temp = 0
			for power in transform_coes[0]:		
				xval = ampl_x[i+power]	
				if(abs(power) <= i):				
					temp += transform_coes[0][power]*xval
				
			for power in transform_coes[1]:
				if(abs(power) <= i and power != 0):
					if(power>=0):
						temp += transform_coes[1][power]*ampl_y[i + power]
					else:
						temp += -1*transform_coes[1][power]*ampl_y[i + power]
			try:
				#print(temp/transform_coes[1][0])
				ampl_y[i] = Decimal(temp/transform_coes[1][0])

			except:
				ampl_y[i] = Decimal(temp)
			if(i%100000 == 0):
				print('chugging along')
			#print(ampl_y[i])
		for i in range(length):
			
			print('copying now, value is', ampl_y[i] )
			ampl_y[i] = int(ampl_y[i])
		print('broke loop')
		
		self.getWaves()[wave_name].setAmplitudes(ampl_y, length)
