import tkinter as tk
from tkinter import ttk
from tkinter import * 

class Cell:
	def __init__(self):
		self.alive = False

	def change_status(self):
		if self.alive:
			self.alive = False
		else:
			self.alive = True

	def status(self):
		if self.alive:
			return "Alive"
		else:
			return "Dead"

class Cluster:
	def __init__(self, x, y):
		self.cluster = []
		self.x = x
		self.y = y
		for i in range(y):
			self.cluster.append([])
			for j in range(x):
				self.cluster[i].append(Cell)
		self.alive = []

	def __str__(self):
		return str(self.cluster)

	def change_status(self, x, y):
		if (x, y) in self.alive:
			self.alive.remove((x, y))
		self.cluster[y][x].change_status()
		if self.cluster[y][x].alive:
			self.alive.append((x, y))

	def action(self):
		if len(self.alive) != 0:
			cl = []
			for row in range(len(self.cluster)):
				for cell in range(len(self.cluster[row])):
					a = 0
					if row-1>=0 and cell-1>=0:
						a += 1 if self.cluster[row-1][cell-1].alive
					if row-1>=0:
						a += 1 if self.cluster[row-1][cell].alive
					if row-1>=0 and cell+1<=len(self.cluster[row]):
						a += 1 if self.cluster[row-1][cell+1].alive
					if cell+1<=len(self.cluster[row]):
						a += 1 if self.cluster[row][cell+1].alive
					if row+1<=len(self.cluster) and cell+1<=len(self.cluster[row]):
						a += 1 if self.cluster[row+1][cell+1].alive
					if row+1<=len(self.cluster):
						a += 1 if self.cluster[row+1][cell].alive
					if row+1<=len(self.cluster) and cell-1>=0:
						a += 1 if self.cluster[row+1][cell-1].alive
					if cell-1>=0
						a += 1 if self.cluster[row][cell-1].alive
					if a == 3 and not self.cluster[row][cell].alive:
						cl.append((row, cell))
					if a > 3 and self.cluster[row][cell].alive:
						cl.append((row, cell))
					if a == 1 and self.cluster[row][cell].alive:
						cl.append((row, cell))

cluster = Cluster(10, 10)
root = Tk()
root.geometry(str(32*cluster.x) + 'x' + str(32*cluster.y+50))
ded = Canvas(root, height=32, width=32)
picture_file = PhotoImage(file = './dead.png')
ded.create_image(32, 0, anchor=NE, image=picture_file)
life = Canvas(root, height=32, width=32)
picture_file2 = PhotoImage(file = './alive.png') 
life.create_image(32, 0, anchor=NE, image=picture_file2)
Button(root, text='start', bg='#F0F8FF', font=('arial', 12, 'normal'), command=klik).place(x=100, y=299)


#print(cluster)
