from libraries import *

#-----------------------------------------------#
#----------BOKEH PLOTTING STRATEGIES------------#
#-----------------------------------------------#
#################################################
def returnNewFigure(title):
    # create a new plot with a title and axis labels
    return figure(title=title, x_axis_label='time', y_axis_label='amplitude', toolbar_location="above",
               tools="xwheel_zoom, pan")
#################################################


#################################################
def showPlot(title, color, x, y):
    p = returnNewFigure(title)
    output_file("Audio.html", title=title)
    # add a line renderer with legend and line thickness
    p.line(x, y, line_width=2, color=color)
    # show the results
    show(p)
#################################################


#################################################
def plotSignalWave(song_file, style):

    x = []
    input_data = read(song_file)
    audio = input_data[1]
    x.extend(range(0,len(audio)))

    showPlot("Signal Wave", style["color"], x, audio)
#################################################


#################################################
def plotAudioHanningWindow(song_file, style):
    # read audio samples
    input_data = read(song_file)
    audio = input_data[1]
    # apply a Hanning window
    window = hann(1024)
    audio = audio[0:1024]*	window
    # fft
    mags = abs(rfft(audio))
    # convert to dB
    mags = 20 * scipy.log10(mags)
    # normalise to 0 dB max
    mags -= max(mags)

    x = []
    x.extend(range(0, len(mags)))

    showPlot("Hanning Window", style["color"], x, mags)
#################################################


#################################################
def plotAudioNormalizedFFT(song_file, style):
    input_data = read(song_file)
    audio = input_data[1]
    # read in sound file; get first 1024 samples
    duration = len(audio)
    k = np.arange(duration)  # returns values up to duration
    T = duration / 44100.0
    freq = k / T  # two sides frequency
    freq = freq[range(duration/2)]	# one side frequency
    Y = fft(audio) / duration  # fft computing and normalizing
    Y = Y[range(duration // 2)]
    Y = Y[1:]
    x = []
    x.extend(range(1, len(Y)))

    showPlot("Normalized FFT", style["color"], x, abs(Y))
#################################################


#################################################
def plotAudioMagnitudeValues(song_file, style):
    # read in sound file; get first 1024 samples
    input_data = read(song_file)
    audio = input_data[1]

    # compute and normalize magnitude values
    magnitudeValues = abs(rfft(audio))  # fft
    magnitudeValues = 20 * scipy.log10(magnitudeValues)  # convert to a decibel scale
    magnitudeValues -= max(magnitudeValues)  # normalize to have a maximum value of 0 dB
    magnitudeValues = magnitudeValues[1:]

    x = []
    x.extend(range(0,len(magnitudeValues)))

    showPlot("Magnitude Values", style["color"], x, magnitudeValues)
#################################################