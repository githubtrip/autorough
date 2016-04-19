Why hello, you searingly smart cookie. If you are here for the world's premiere lots-of-videos-in-a-folder-to-Premiere-Pro-rough-cut repo, read on!

Auto Rough
====

*It's like a Golden Rough, but for exposing your otherwise unseen videos to the world, extremely quickly.*

![A picture of an actual Golden Rough](http://theklutzycook.com/wp-content/uploads/2012/09/Golden-Rough.jpg)

Before we begin
----

This is under heavy testing and development. I'll post something more authoritative like a version number here when it's ready to be let loose in the wild.

What you need
----

This is all you need:
*	Premiere Pro CS6 (it's great, I don't have to pay a subscription for it!),
*	[This 900mb Docker image](https://hub.docker.com/r/jacksongs/autorough/),
*	Some videos, and
*	A thumping track in mp3 format.

If you don't use the Docker image, you will need to install into a linux/Mac environment:
*	ffmpeg,
*	aubio,
*	lxml,
*	python and the PyAV package.

It's a total pain to compile all that though. Docker is your overhyped, unpredictable, unpolished but extremely useful friend.

You could probably get away with a lighter weight set of tools but this gets the job done. 

How to get it working
---

I like to run the Docker image in the current working directory, using this command:

	docker run -it -v `pwd`:`pwd` -w `pwd` jacksongs/autorough

Then, it's as simple as:

	python autorough.py -a <insert the location and name of your audio track here, or just a filename if it's in the current directory > -v <and this is the folder where your videos live>

So, for example, if I had a BuddyHolly.mp3 as my track and my videos lived in /Users/mymac/Documents/Videos, I would type:

	python autorough.py -a BuddyHolly.mp3 -v /Users/jacksongsimac/Documents/Videos 

Got any Docker tips for me? Get in touch, I need as much help as I can get. Just building this goddamn image took an afternoon.


The future of Auto Rough
----

I'm looking to integrate this into a more complete metadata environment and to have it work across Final Cut Pro as well.

Originally I didn't produce an XML, it was just an mp4, but that didn't give me much a chance to tinker with the edit. Could be a good basic option to bring back though.