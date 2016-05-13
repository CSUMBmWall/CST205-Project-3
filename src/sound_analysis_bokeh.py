from libraries import *


# TODO: fix everything but plotSignalWave
#################################################
def plotSignalWave(song_file, style):
    '''
    input_data = read(song_file)
    audio = input_data[1]
    # plot the first 1024 samples
    plt.plot(audio[0:1024])
    '''


    sound_wave = wave.open(song_file, 'r')

    #extract raw audio from .wav file
    signal = sound_wave.readframes(-1)
    signal = np.fromstring(signal, 'Int16')

    # frame rate of .wav file
    frame_rate = sound_wave.getframerate()

    # time vector spaced linearly with
    # the size of the audio file
    time = np.linspace(0, len(signal)/frame_rate, num = len(signal))


    input_data = read(song_file)
    audio = input_data[1]
    x = []
    x.extend(range(0, len(audio)))
    showBokeh("Signal Wave", style, x, audio)


#################################################

#################################################
def plotAudioHanningWindow(song_file, style):
    # read audio samples
    input_data = read(song_file)
    audio = input_data[1]
    # apply a Hanning window
    window = hann(1024)
    audio = audio[0:1024] * window
    # fft
    mags = abs(rfft(audio))
    # convert to dB
    mags = 20 * scipy.log10(mags)
    # normalise to 0 dB max
    mags -= max(mags)

    x = []
    x.extend(range(0, len(mags)))

    showBokeh("Hanning Window", style, x, mags)


#################################################

#################################################
def plotAudioNormalizedFFT(song_file, style):
    input_data = read(song_file)
    style_string = style["color"] + style["shape"]
    audio = input_data[1]
    # read in sound file; get first 1024 samples
    duration = len(audio)
    audioFFT = fft(audio) / duration  # fft computing and normalizing
    audioFFT = audioFFT[range(duration / 2)]
    audioFFT = audioFFT[1:]
    x = []
    x.extend(range(0,len(audioFFT)))
    showBokeh("Normalized FFT", style, x, abs(audioFFT))

#################################################

#################################################
def plotAudioMagnitudeValues(song_file, style):
    # read in sound file; get first 1024 samples
    input_data = read(song_file)
    audio = input_data[1]
    audio = audio[0:1024]

    # compute and normalize magnitude values
    magnitudeValues = abs(rfft(audio))  # fft
    magnitudeValues = 20 * scipy.log10(magnitudeValues)  # convert to a decibel scale
    magnitudeValues -= max(magnitudeValues)  # normalize to have a maximum value of 0 dB
    x = []
    x.extend(range(0, len(magnitudeValues)))
    showBokeh("Magnitude Values", style, x, magnitudeValues)


def returnNewFigure(title):
    # create a new plot with a title and axis labels
    return figure(title=title, x_axis_label='time', y_axis_label='amplitude', toolbar_location="above",
               tools="xwheel_zoom, pan, box_select, box_zoom, lasso_select, reset")


def showBokeh(title, style, x, y):
    output_file("Audio.html", title=title)

    print style

    colorDict = {"c": "cyan", "m": "magenta", "g": "green", "b": "black"}
    color = colorDict[style["color"]]
    p = returnNewFigure(title)


    if style["shape"] == "s":
        p.square(x, y, line_width=2, color=color, fill_color="black", size=6)

    if style["shape"] == "--":
        p.line(x,y, line_width=2, line_color=color,)

    if style["shape"] == "o":
        p.circle(x, y, line_width=2, color=color, fill_color="black", size=6)

    if style["shape"] == "v":
        p.triangle(x, y, line_width=2, color=color, fill_color="black", size=6)

    show(p)

def showMatPlotLib(title, style, x):
    plt.title(title)
    style_string = style["color"] + style["shape"]
    plt.plot(x, style_string)
    plt.show()

	#################################################
