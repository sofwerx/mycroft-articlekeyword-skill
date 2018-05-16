
from pathlib import Path
from summa import keywords
import sys

text = """
As humankind continues to stare into the dark abyss of deep space in an eternal quest to understand our origins, new computational tools and technologies are needed at unprecedented scales. Gigantic datasets from advanced high resolution telescopes and huge scientific instrumentation installations are overwhelming classical computational and storage techniques.

This is the key issue with exploring the Universe – it is very, very large. Combining advances in machine learning and high speed data storage are starting to provide hitherto unheard of levels of insight that were previously in the realm of pure science fiction. Using computer systems to infer knowledge from observation isn’t new, but the scale at which we need to examine large data today certainly is.

Because the data are so unwieldy and complicated, new methods need to be devised to quickly annotate features that are important, sifting out valuable signals from all of the noise. Nothing is probably more difficult than finding the signal of an “echo” observed from the “sound” a pair of black holes colliding billions of light years away from Earth. This was the premise of the algorithms needed to make sense of the data from the Laser Interferometer Gravitational-Wave Observatory (LIGO) project. They need to filter out a vast array of noise from the real “proton sized” signal, it is an intrinsically computationally intensive process, the main reason being just the sheer size and noiseiness of the captured data.

The Next Platform listened in to Daniel George, a researcher from the National Center for Supercomputing Applications (NCSA) at The University of Illinois, speaking about their latest work they presented at the Meeting of the American Physical Society. We have covered their work in a previous episode of The Interview. It is a fascinating use case for AI in astrophysics.

The team has now published two papers on their methods to use AI to find gravitational waves. First up was the initial paper, “Deep neural networks to enable real-time multimessenger astrophysics” in Physics Review D, in February 2018, with the follow-on Deep Learning for real-time gravitational wave detection and parameter estimation: Results with Advanced LIGO data in Physics Letters B, in March 2018.

The most recent work “Classification and clustering of LIGO data with deep transfer learning they discussed at the APS meeting, which is due to be published in Physics Review D, goes still one a step further to show how they have also used transfer learning to take previously trained networks and then apply them to new data. The team are clearly building an iterative portfolio of methods to apply to gravitational waves.


All LIGO source data are publicly available, and as defined in the LIGO data management plan, the data comes in at about 25 megabytes per second per interferometer, leading to an aggregate collection of about 1.5 petabytes a year. Each individual data slice corresponds to 4,096 seconds of GPS time, each of these specific slices may contain up to 130 MB of potential event data. It’s all encoded as either JSON, HDF5 or plain ASCII data frames. Out of the gate, it sounds like an impossible and inordinately daunting task to even think about how much compute you would need to look at all of this data. It is complex difficult data for sure, fortunately the new AI methods to do this need only focus on a few of these rather specific 4K second slices of data to learn something about how to best find the signal.

George et. al. demonstrated that their “Deep Transfer Method” enabled very deep convolutional neural networks to carry out what they call “glitch classification”, even given small and unbalanced training datasets. They significantly reduced the training time, and achieved an accuracy above 98.8%, lowering their previous error rate by over 60%.

More importantly, once they trained via transfer learning on these known classes, they show that the neural networks can also be truncated and used as feature extractors for unsupervised clustering to automatically group together new and unknown classes of glitches and anomalous signals. This novel capability is very important to identify and remove new types of glitches which will occur as the LIGO/Virgo detectors continue to gradually attain their design sensitivity.

As a real-world and practical use case of their artificial intelligence methods, the team has stated “We are trying to do this so fast that LIGO can instantly tell you where to point your telescope.”


To understand more, The Next Platform downloaded two of the carefully annotated 4,096 second strain datasets for one of these events, GW151226 collected at 16384Hz. One from the detector in Hanford, Washington and the other one from Livingston, Louisiana. Fortunately, these datasets represent only a pair of old school CD-ROMs worth of compressed information. Approximately 600 MB of compressed data from each detection station that corresponds to the actual critical event signal. Three specific “gravitational wave events”, GW150914, LVT151012, and GW151226 were taken by George et. al. as example data to craft their method.

Here’s the real challenge though, and why this is hard. This is data that has been annotated already. Annotated by bespoke hand-made algorithms, hard enough to craft, design, and build that when combined with phenomenal infrastructure and science teams resulted in a Nobel Prize. However, finding net new equivalent “CDROM sized slice” worth of critical data located somewhere buried inside over a petabyte and a half of interferometer data generated each year isn’t trivial. That’s the hard part, and that’s the part the team are turning to AI for help with.

This challenge is also not unique to advanced astrophysics. Many of us in a number of fields from Chemistry to Social Science are also searching through our vast complex datasets looking for valid and new and interesting signals. Mining for gold is easier, and it makes for a great analogy for what is happening here.

So, that’s the real challenge to solve. These CDROM sized “golden data nuggets” are the now carefully annotated slices that the extended LIGO team use train their new neural network methods. Once they “teach” these networks to essentially know what “golden data nuggets” look like, they can then use “transfer learning” to effectively reuse these computationally intensively trained “metal detectors” to then sift through brand new, and as yet unclassified data soil, continuing in their search for brand new, potentially ever more valuable “golden nuggets.”

When the LIGO scientists go looking for signal (their equivalent of a “golden data nugget”), they need to see a “false alarm” rate estimated to be less than 1 event per 203,000 years, also that signal has to be detected simultaneously in both Washington and Louisiana. This is clearly the scientific version of “find the needle in a haystack” territory for sure. To showcase their new neural network method, the team used a dataset of twenty-two classes of glitches, carefully curated and labeled by the “Gravity Spy” project using raw data collected during LIGO’s first discovery campaign.


Critical to all of this research were GPU accelerators – specifically the Tesla P100s used in the DGX-1 server from Nvidia – which enabled accelerated training of neural networks. They used the Wolfram Language neural network functionality, built a top of the open-source MXNet framework, that in turn uses the cuDNN library for accelerating the training on Nvidia GPUs. ADAM was deployed as the underlying learning algorithm. The significant horsepower of the Blue Waters system, which is also GPU accelerated, was brought to bear for their modeling data and for solving Einstein’s equations via simulation. The group are also looking into generative models GANs (generative adversarial networks) to further reduce the multi-week time taken (even for Blue Waters) for these specific steps.

They aren’t the only astrophysics group in town looking at using AI to reduce the complexity of their data. Brian Nord for example, works in the deep skies lab on gravitational lensing at Fermilab. A gravitational lens is formed between a distant light source and an observer that bends the light from the source as it travels towards the observer. The amount of bending is one of the predictions of Albert Einstein’s general theory of relativity. Researchers can also use “lensing” as a measurement of how much dark matter there is in the universe. Between 1979 and now, only 1,000 such “lenses” have been discovered, but they predict significantly more of these observations will be found. The Dark Energy Survey (DES) uses the dark energy camera, and is predicted to have over 2,000 galaxy scale lenses in this survey. LSST was hinted to find potentially 120,000 of these types of events. This team also didn’t want to reinvent the wheel, and they also turned to AI techniques to help them. Using deep learning they found 8 new confirmed lenses, by looking at 100’s of square degrees of images. They use “ensembles of networks” and then use a simple majority vote to decide on which are lenses and which are not lenses. This specific technique of “jury vote” or consensus prediction is becoming very popular in a variety of fields to improve the quality of AI systems.

Finally, one last challenge with the rise of AI in astrophysics, as in most other fields is the ever-present issue of reproducibility. A recent article in Physics Today draws specific attention to exactly this issue of data and algorithm provenance. The headline – A combination of data-churning telescopes and proprietary algorithms has led to a slate of opaque research that has some astronomers concerned – is clearly quite troublesome.

However, all is not lost. For example, Alice Allen discusses the volunteer-run Astrophysics Source Code Library in this Nature Toolbox Q&A. Allen and her team are actively contacting researchers to make sure that software and algorithms are uploaded to their archive. It will take an entire community to make sure that the new systems we design, especially as they continue to be more and more automatic can continue to provide reproducible science.

In summary, the adoption of artificial intelligence in astrophysics is a wonderful new tool to have in our bag of discovery. For lower precision detective work when mining noisy data for data nuggets, the application of the Tensor Core  versus the CPU core paradigm is absolutely appropriate and will continue to drive large scale computational architectures such as “Summit” at Oak Ridge National Laboratory and other massive machines for a good few years to come.




"""
#file_path = text
#'/home/david/Documents/textrank/aih.txt'
#text = Path(file_path).read_text()


from summa import summarizer
print(summarizer.summarize(text, words=100))

#print(keywords.keywords(text, words=10 , scores=True))

#
# from summa import summarizer
# print(summarizer.summarize(text))
#print(text)