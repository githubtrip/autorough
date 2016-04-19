# Good day and welcome! Thanks for visiting this intriguing script.
# What does it do? I'm glad you asked. It listens to a music track, peers into a folder of videos, and creates a rough cut of the videos matching the beat of the music. Neato!

# First, this part allows you to set where your video files are located, as well as the name and location of your audio track. Note! Your audio file MUST be an mp3.
import argparse

parser = argparse.ArgumentParser(description='Identify the video and audio folder locations.')
parser.add_argument('-v','--videofolder',default='/')
parser.add_argument('-a','--track')
args = vars(parser.parse_args())
print args

# Let's save these as nicer variables.
vidfolder = args['videofolder']

if args['track'] != None:
	audiofile = args['track'] # Note! Your audio file MUST be an mp3.
else:
	audiofile = None

print vidfolder, audiofile

if audiofile != None:
	# Now here is the magic to get the BPM of the file. This is amended from the aubio repo here: https://github.com/aubio/aubio/blob/master/python/demos/demo_bpm_extract.py

	from aubio import source, tempo
	from numpy import median, diff

	def get_file_bpm(path, params = {}):
	    """ Calculate the beats per minute (bpm) of a given file.
	        path: path to the file
	        param: dictionary of parameters
	    """
	    try:
	        win_s = params['win_s']
	        samplerate = params['samplerate']
	        hop_s = params['hop_s']
	    except:
	        """
	        # super fast
	        samplerate, win_s, hop_s = 4000, 128, 64 
	        # fast
	        samplerate, win_s, hop_s = 8000, 512, 128
	        """
	        # default:
	        samplerate, win_s, hop_s = 44100, 1024, 512

	    print path,samplerate,hop_s
	    s = source(path, samplerate, hop_s)
	    samplerate = s.samplerate
	    o = tempo("specdiff", win_s, hop_s, samplerate)
	    # List of beats, in samples
	    beats = []
	    # Total number of frames read
	    total_frames = 0

	    while True:
	        samples, read = s()
	        is_beat = o(samples)
	        if is_beat:
	            this_beat = o.get_last_s()
	            beats.append(this_beat)
	            #if o.get_confidence() > .2 and len(beats) > 2.:
	            #    break
	        total_frames += read
	        if read < hop_s:
	            break

	    # Convert to periods and to bpm 
	    bpms = 60./diff(beats)
	    b = median(bpms)
	    return b

	bpm = get_file_bpm(audiofile)
	beat = bpm/60
	print 'Beats per second for the audio is',beat
	print 'Frames per beat (assuming 24fps) is',23.976/beat
else:
	beat=2 # This sets a default of 2 beats per second if no audio track is provided.

# This simply gets the duration of the track, using PyAV.
import av
fordur = av.open(audiofile)
print 'Duration is',fordur.duration/1000000.0,'seconds'







