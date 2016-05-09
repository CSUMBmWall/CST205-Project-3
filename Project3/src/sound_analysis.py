from libraries import *

# create lines.html
output_file("Audio.html", title="Signal Wave")

def returnNewFigure():
    # create a new plot with a title and axis labels
    return figure(title="Simple Signal Wave", x_axis_label='time', y_axis_label='amplitude', toolbar_location="above",
               tools="xwheel_zoom, pan")

# TODO: fix everything but plotSignalWave
#################################################
def plotSignalWave(song_file, style):
    p = returnNewFigure()
    x = []
    print(song_file)
    print(type(song_file))
    print(len(song_file))
    print(len(song_file.strip()))
    input_data = read(song_file)
    audio = input_data[1]
    x.extend(range(0,len(audio)))

    #create html output file
    output_file("Audio.html", title="Signal Wave")

    color = style["color"]
    print("color - " + style['color'])
    print(type(color))
    print(len(color))
    # add a line renderer with legend and line thickness
    p.line(x, audio, line_width=2, color=style['color'])

    # show the results
    show(p)


#################################################

#################################################
def plotAudioHanningWindow(song_file, style):
    p = returnNewFigure()
    # read audio samples
    input_data = read("bugs_left_turn.wav")
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

    #create lines.html
    output_file("Audio.html", title="Signal Wave")


    # add a line renderer with legend and line thickness
    p.line(x, mags, line_width=2)

    # show the results
    show(p)


#################################################

#################################################
def plotAudioNormalizedFFT(song_file, style):
    p = returnNewFigure()
    input_data = read("bugs_left_turn.wav")
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

    # create lines.html
    output_file("Audio.html", title="Signal Wave")


    # add a line renderer with legend and line thickness
    p.line(x, abs(Y), line_width=2)

    # show the results
    show(p)


#################################################

#################################################
def plotAudioMagnitudeValues(song_file, style):
    p = returnNewFigure()

    # read in sound file; get first 1024 samples
    input_data = read("bugs_left_turn.wav")
    audio = input_data[1]

    # compute and normalize magnitude values
    magnitudeValues = abs(rfft(audio))  # fft
    magnitudeValues = 20 * scipy.log10(magnitudeValues)  # convert to a decibel scale
    magnitudeValues -= max(magnitudeValues)  # normalize to have a maximum value of 0 dB

    x = []
    x.extend(range(0,len(magnitudeValues)))

    # add a line renderer with legend and line thickness
    p.line(x, magnitudeValues, line_width=2)

    # show the results
    show(p)



	#################################################
