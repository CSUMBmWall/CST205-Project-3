import Tkinter as tk
from Tkinter import *
from Tkinter import Canvas
import tkFont

from sound_analysis import *

#----------------------------------------#
#----------FONT CUSTOM INFO--------------#
#----------------------------------------#
TITLE_FONT = ("AppleGothic", 85, "bold")
BUTTON_FONT = ("AppleGothic", 35)
SMALL_FONT = ("AppleGothic", 20)

BUTTON_COLOR = "#FF5722" # accent color: orange
BG_COLOR = "#607D8B" # primary color: light blue gray
TEXT_COLOR = "#212121" # primary text: matte black


song_file = "" 
style_string = {}

#################################################
class AudioViz(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# container to stack frames on top of each other
		# the desired visible frame will be raised above the others
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		# initialize empty list to hold all frames
		self.frames = {}

		for F in (WelcomeScreen, SongSelect, ColorSelect, StyleSelect, VisualSelect):
			page_name = F.__name__
			frame = F(container, self)

			# declare elements of frames list
			self.frames[page_name] = frame 

			# all pages in the same location
			frame.grid(row=0, column=0, sticky="nsew") 
			frame.configure(bg=BG_COLOR) 

		# first visible frame
		self.show_welcome()

	# display WelcomeScreen
	def show_welcome(self):
		global song_file 
		song_file = ""

		global style_string
		style_string = {}
		frame = self.frames["WelcomeScreen"]
		frame.tkraise()

	# display SongSelect frame
	def show_song_menu(self):
		frame = self.frames["SongSelect"]
		frame.tkraise()

	# display ColorSelect frame
	def show_color_menu(self, song):
		global song_file 
		song_file = song

		frame = self.frames["ColorSelect"]
		frame.tkraise()

	# display StyleSelect frame
	def show_style_menu(self, colorVal):
		global style_string
		style_string["color"] = colorVal
		frame = self.frames["StyleSelect"]
		frame.tkraise()

	# display VisualSelection frame
	def show_visual_menu(self, shape):
		global style_string
		style_string["shape"] = shape
		frame = self.frames["VisualSelect"]
		frame.tkraise()

	

	
#################################################


#################################################
# welcome screen
class WelcomeScreen(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		# title aesthetics
		title = tk.Label(self, text="audio\nvisualizer", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# enter button
		enter = tk.Button(self, text="enter", padx="20", pady="5", highlightthickness="0", highlightbackground=BUTTON_COLOR,
                          highlightcolor=BUTTON_COLOR, command=lambda: controller.show_song_menu())
		enter.config(font=BUTTON_FONT)
		enter.place(relx=0.5, rely=0.625, anchor=CENTER)
		
#################################################


#################################################
# menu to select song file
class SongSelect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# title aesthetics
		title = tk.Label(self, text="song?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# bugs button
		bugs = tk.Button(self, text="Bugs Bunny", width="15", highlightthickness="0",
                         command=lambda: controller.show_color_menu("..\\audio\\bugs_left_turn.wav"))
		bugs.config(font=BUTTON_FONT)

		# song3 button
		handsDown = tk.Button(self, text="PacMan", width="15", highlightthickness="0",
						  command=lambda: controller.show_color_menu("..\\audio\\dead_poets_captain.wav"))
		handsDown.config(font=BUTTON_FONT)

		# display buttons
		bugs.pack()
		handsDown.pack()

#################################################


#################################################
# ask user to select color of plot
class ColorSelect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		# title aesthetics
		title = tk.Label(self, text="color?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# cyan
		cyan = tk.Button(self, text="cyan", width="15", fg="#00ffff", highlightthickness="0",
                         command=lambda: controller.show_style_menu('c'))
		cyan.config(font=BUTTON_FONT)

		# magenta
		magenta = tk.Button(self, text="magenta", width="15", fg="#ff00ff", highlightthickness="0",
                            command=lambda: controller.show_style_menu('m'))
		magenta.config(font=BUTTON_FONT)

		# green
		green = tk.Button(self, text="green", width="15", fg="#00FF00", highlightthickness="0",
                          command=lambda: controller.show_style_menu('g'))
		green.config(font=BUTTON_FONT)

		# black
		black = tk.Button(self, text="black", width="15", highlightthickness="0",
                          command=lambda: controller.show_style_menu('b'))
		black.config(font=BUTTON_FONT)

		# button to allow user to start over
		start_over = tk.Button(self, text="start over", width="15", highlightthickness="0",
                               command=lambda: controller.show_song_menu())
		start_over.config(font=SMALL_FONT)

		cyan.pack()
		magenta.pack()
		green.pack()
		black.pack()
		start_over.pack()
#################################################


#################################################
# ask user to select style of plot
class StyleSelect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		# title aesthetics
		title = tk.Label(self, text="style?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# solid line
		square = tk.Button(self, text="[][][][][][][][]", width="15", highlightthickness="0",
                           command=lambda: controller.show_visual_menu('s'))
		square.config(font=BUTTON_FONT)

		# circle
		circle = tk.Button(self, text="ooooooooooooooo", width="15", highlightthickness="0",
                           command=lambda: controller.show_visual_menu('o'))
		circle.config(font=BUTTON_FONT)

		# star
		line = tk.Button(self, text="-------------------", width="15", highlightthickness="0",
                         command=lambda: controller.show_visual_menu('--'))
		line.config(font=BUTTON_FONT)

		# pixel
		triangle = tk.Button(self, text="vvvvvvvvvvvvvvvvvvv", width="15", highlightthickness="0",
                             command=lambda: controller.show_visual_menu('v'))
		triangle.config(font=BUTTON_FONT)

		# button to allow user to start over
		start_over = tk.Button(self, text="start over", width="15", highlightthickness="0",
                               command=lambda: controller.show_song_menu())
		start_over.config(font=SMALL_FONT)

		square.pack()
		circle.pack()
		line.pack()
		triangle.pack()
		start_over.pack()
#################################################


#################################################
# menu to select audio visualizer method
class VisualSelect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		global song_file

		# title aesthetics
		title = tk.Label(self, text="visualizer?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# original audio
		orig_audio = tk.Button(self, text="signal wave", width="15", highlightthickness="0",
                               command=lambda: plotSignalWave(song_file, style_string))
		orig_audio.config(font=BUTTON_FONT)

		# audio with hanning window
		audio_hann = tk.Button(self, text="hann window", width="15", highlightthickness="0",
                               command=lambda: plotAudioHanningWindow(song_file, style_string))
		audio_hann.config(font=BUTTON_FONT)

		# audio normalized with fft
		audio_fft = tk.Button(self, text="fft", width="15", highlightthickness="0",
                              command=lambda: plotAudioNormalizedFFT(song_file, style_string))
		audio_fft.config(font=BUTTON_FONT)

		# audio magnitude values
		audio_mag = tk.Button(self, text="mag", width="15", highlightthickness="0",
                              command=lambda: plotAudioMagnitudeValues(song_file, style_string))
		audio_mag.config(font=BUTTON_FONT)

		# button to allow user to start over
		start_over = tk.Button(self, text="start over", width="15", highlightthickness="0",
                               command=lambda: controller.show_song_menu())
		start_over.config(font=SMALL_FONT)

		orig_audio.pack()
		audio_hann.pack()
		audio_mag.pack()
		audio_fft.pack()
		start_over.pack()
#################################################


#################################################
# run application
if __name__ == "__main__":
	app = AudioViz()
	app.geometry("600x700")
	app.title("Audio Visualizer")
	app.mainloop()
#################################################




