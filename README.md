## Title: Media groups (consortia?) clustering **TODO**

## Abstract **TODO: reread, but should be good**
One's view of the world is based on the information we have on it, and how it is conveyed.
A big part of that information we obtain from the media, and in particular "traditional media"
namely newspapers such as *The New York Times* or *Fox News*.
As a result, the media have a huge impact on the public’s opinion.

One way to ensure you are well-informed (i.e. you are getting information on various topics) and are
not biased towards a particular stance is to gather knowledge from several sources,
e.g. several media.

But a lot of these media are owned by the same groups. This begs the question whether
the information we are getting really is diverse, or if the news and opinions shared
are roughly the same for media belonging to the same entity.

To answer that question, we will cluster journals according to different metrics
aiming at evaluating the opinion they defend.

## Research questions
* What are the best metrics to evaluate the opinions conveyed by a media.
 **(TODO really a research question, or just a method?)**
* Does the orientation of a newspaper influence his choice of speaker?
 **(TODO: same question as above)**

* Does the clustering of media enable us to detect the groups owning them?


## Proposed additional datasets
  * wikidata

## Methods:
##### Metrics considered, and an overview on how to implement them:
* Cluster according to the people cited (Naive: count them. Less naive:
  extract the topics each author is most associated with, and use their occurrences
  to find the orientation of the media).
* Cluster according to the topics treated (e.g. extract meaning from articles,
  or simply extract the "meaningful" words used).


To cluster media by people cited, we can not simply count the number of occurrences
of each speaker. We have to compare the number of citations of one person in the
journal with the number of citations of this person in the corpus in general.
To accomplish this, we extract all the citees, then group them by the
journals in which they appear. We then use [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
(*term frequency-inverse document frequency*) to separate the different media.

To extract a topic associated to, for example, articles, we use [LSI](https://en.wikipedia.org/wiki/Latent_semantic_analysis) (*Latent semantic indexation*), which is also based on TF-IDF.

##### Use of wikidata: automating the consortium extraction:
In wikidata the media considered have an `owned by`
attribute, which we can use, potentially recursively, to automate the consortium finding.
To do that we will first have to either reparse the newspapers names  --which are for now
all lower-case, all-attached-- to use them as input for the API, or to input them as-is
in the wikidata search box, which seems to usually find the expected result.

##### Notebook organization: the most important files.
  **TODO:  Confirm notebook organization.**

  | File name                                    |Its use                                   |
  |:-------------------------------------------- |:----------------------------------------:|
  |Create newspaper - speaker TF-IDF matrix.ipynb| Creates the aforementioned TF-IDF matrix |
  |Create newspaper - token TF-IDF matrix.ipynb  | Creates the aforementioned TF-IDF matrix |
  |Helper.py                                     | Extract newspapers name from URL         |
  |Newspaper_speaker_statistics.ipynb            | Some statistics and analysis on the speakers |
  |Preprocess_quotes.ipynb                       | Quote preprocessing, e.g. tokenization, formatting and lemmatization |
  |Preprocess_speakers.ipynb                     | Speakers preprocessing: see file for more details |
  |Quotes_2020_loading.ipynb                     | Quotes loading: see file for more details |



## Proposed timeline **TODO: add 1 milestone?**
* **25-11-2021:** Data processing finished (**TODO: expand on that, or we say its enough?**)
* **TODO: add intermediate milestone maybe not?**
* **10-12-2021:** Finish data analysis (i.e. **TODO ~all algorithms we were interested in have been run**)
* **12-12-2021:** Finish code cleaning and documentation.
* **15-12-2021:** Finish writing up data story (+visualisation).
* **16-12-2021:** Website is up and running, with the data story on it.
* **17-12-2021:** Panic fixes.

## Organization within the team, to be refined individually at a later date. **TODO: more precise for A&J at least**
* Antoine & Jonas
  * data processing/pipelining/filtering
  * ML algos
* Hugo & Marin
  * Data extraction / scraping (wikidata)
  * Code documentation
  * Data story?
  * Visualisation

### Questions for TAs **TODO: any questions? Might make us seem better to have some**
