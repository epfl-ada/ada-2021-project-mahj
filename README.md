## Title: The dictatorship of consortia on their owned media.

**TODO: add that:**

## Abstract
One's view of the world is based on the information we have on it, and how it is conveyed.
A big part of that information we obtain from the media, and in particular "traditional media"
namely newspapers such as *The New York Times* or *Fox News*.
As a result, the media have a huge impact on the public’s opinion.

One way to ensure you are well-informed (i.e. you are getting information on various topics) and are
not biased towards a particular stance[^1] is to gather knowledge from several sources,
e.g. several media.

[^1]: https://www.allsides.com/media-bias/media-bias-ratings

But a lot of these media are owned by the same groups. This begs the question whether
the information we are getting really is diverse, or if the news and opinions shared
are roughly the same for media belonging to the same entity.[^2]

[^2]: https://www.youtube.com/watch?v=_fHfgU8oMSo

To answer that question, we will try to cluster journals according to different metrics
aiming at evaluating the opinion they defend. Other scientists have already obtained
similar results[^3] [^4] based on twitter which makes us also expect to get interesting results.

[^3]: https://www.mediaobservatory.com/
[^4]: https://newsteller.io/source

## Research questions
- Is the influence of media ownership groups visible in quotes shared by newspapers?
- Does the clustering of media based on quotebank enable us to detect the groups owning them?
- What are the best metrics to identify the group they belong to?  
  * Based on the speakers: Does the membership of a media to a consortium influence the choice / importance of their speakers?  
  * Based on the quotes: Does the membership of a media to a consortium influence the choice / importance of topics or use of a specific term?



## Proposed additional datasets
  * wikidata

  Use of wikidata: automating the consortium extraction:
  In wikidata the media considered have an `owned by`
  attribute, which we can use, potentially recursively, to automate the consortium finding.
  To do that we will first have to either reparse the newspapers names  --which are for now
  all lower-case, all-attached-- to use them as input for the API, or to input them as-is
  in the wikidata search box, which seems to usually find the expected result.

## Methods:

> ignore quoted text. Only here to be saved for now.
> ##### Metrics considered, and an overview on how to implement them:
* Cluster according to the people cited (Naive: count them. Less naive:
  extract the topics each author is most associated with, and use their occurrences to find the orientation of the media).
* Cluster according to the topics treated (e.g. extract meaning from articles, or simply extract the "meaningful" words used).

  >To cluster media by people cited, we can not simply count the number of occurrences
  of each speaker. We have to compare the number of citations of one person in the
  journal with the number of citations of this person in the corpus in general.
  To accomplish this, we extract all the citees, then group them by the
  journals in which they appear. We then use [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
  (*term frequency-inverse document frequency*) to separate the different media.

> To extract a topic associated to, for example, articles, we use [LSI](https://en.wikipedia.org/wiki/Latent_semantic_analysis) (*Latent semantic indexation*), which is also based on TF-IDF.

##### Features and algorithms to be used:
There are numerous features and similarity metrics to be chosen from.  

The features we study are based on our a priori analysis of
which factors will be most useful in clustering the media, namely the speakers
quoted by this media, and the words **TODO: "in the quotes", or "in the articles
from which the quotes come"?**

We can then use different algorithms and similarity metrics to measure the distance
between media. We will try several and choose the one giving the best
results, i.e. the clearest clustering. The methods we have selected are:
* Use [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
(*term frequency-inverse document frequency*) on the sets of words, or on the
number of speakers having spoken for a specific media, in order to give a bigger
weight to more "significant" words or people. Then use PCA[^5] with cosine similarity
as a distance metric to project these vectors in a smaller subspace, and finally run
k-means (with cosine similarity) on the resulting vectors.
* For each media, remember the set of citees, the distance measure is be
the Jaccard similarity on these sets. We then run PCA[^5], then k-means on these media.
**TODO: explain LSI.**
* [LSI](https://en.wikipedia.org/wiki/Latent_semantic_analysis) (*Latent semantic indexation*)
which we will apply on the words to extract the most interesting "topics"

[^5]: PCA is optional, but can be visually clearer (for dimensions <= 3 at least),
 and will reduce variance for the k-means algorithm.

We will in our analysis only focus on a few carefully selected ones,
based either on their complexity or an a ()

##### Notebook organization: the most important files.

  | File name                                    |Its use                                   |
  |:-------------------------------------------- |:----------------------------------------:|
  |Create newspaper - speaker TF-IDF matrix.ipynb| Creates the aforementioned TF-IDF matrix |
  |Create newspaper - token TF-IDF matrix.ipynb  | Creates the aforementioned TF-IDF matrix |
  |Helper.py                                     | Extract newspapers name from URL         |
  |Newspaper_speaker_statistics.ipynb            | Some statistics and analysis on the speakers |
  |Preprocess_quotes.ipynb                       | Quote preprocessing, e.g. tokenization, formatting and lemmatization |
  |Preprocess_speakers.ipynb                     | Speakers preprocessing: see file for more details |
  |Quotes_2020_loading.ipynb                     | Quotes loading: see file for more details |

## Proposed timeline
* **17-nov-2021:** Media grouped by consortia.
* **25-nov-2021:** Newspaper selection finished (i.e. decide on which to drop, and implement remote processing if it is still too big for local algorithms (e.g. AWS))
* **30-nov-2021:** Pipelines for different metrics implemented
* **10-dec-2021:** Finish data analysis.
* **12-dec-2021:** Finish code cleaning and documentation.
* **15-dec-2021:** Finish writing up data story (+visualization).
* **16-dec-2021:** Website is up and running, with the data story on it.
* **17-dec-2021:** Panic fixes.

## Organization within the team, to be refined individually at a later date. **TODO: more precise for A&J at least**
* Antoine & Jonas
  * Quotes and speakers preprocessing
  * Creation of TF-IDF matrices
  * Implementation of different pipeline to cluster newspaper
* Hugo & Marin
  * Data extraction / scraping (wikidata)
  * Code documentation
  * Data story?
  * Visualization

## Questions for TAs **TODO: any questions left?*
