# Title: The dictatorship of consortia on the media they own.

**TODO: a link to the notebook**  
**see [this](https://github.com/epfl-ada/ada-2020-project-milestone-p3-p3_chic) if
you want to see how some updated their README**

## Notebook important files:

| File name                                    |Its purpose                                   |
|:-------------------------------------------- |:----------------------------------------:|
|Wikidata_scraping.ipynb| Code used to do the data augmentation, in other words to construct the features we were missing |
|Process_data.ipynb | The pipeline used to clean, format and transform our data before the analysis |
|Analysis.ipynb  | The final notebook, containing all the visualization and analysis |


## Abstract
One's view of the world is based on the information we have on it, and how it is conveyed.
A big part of that information we obtain from the media, and in particular "traditional media"
namely newspapers such as *The Guardian* or *Fox News*.
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

## \[old\] Research questions
- Is the influence of media ownership groups visible in quotes shared by newspapers?
- Does the clustering of media based on quotebank enable us to detect the groups owning them?
- What are the best metrics to identify the group they belong to?  
  * Based on the speakers: Does the membership of a media to a consortium influence the choice / importance of their speakers?  
  * Based on the quotes: Does the membership of a media to a consortium influence
   the choice / importance of the topics treated or the use of a specific term?

## Additional datasets
  * wikidata

  Use of wikidata: automating the consortium extraction:
  In wikidata the media considered have an `owned by`
  attribute, which we can use, potentially recursively, to automate the consortium finding.
  To do that we will first have to either reparse the newspapers names  --which are for now
  all lower-case, all-attached-- to use them as input for the API, or to input them as-is
  in the wikidata search box, which seems to usually find the expected result.

  We have the "Pywikibot" notebook that proves we can link the name of the website we found in
  the quote dataset to its corresponding wikidata qid. For instance linking "nytimes.com" to its qid
  "Q9684" which references "The New York Times" in wikidata.

## \[old\] Methods:

##### Features and algorithms to be used:
There are numerous features and similarity metrics to be chosen from.  

The features we study are based on our a priori analysis of
which factors will be most useful in clustering the media, namely the speakers
quoted by this media, and the words in the quote.

We can then use different algorithms and similarity metrics to measure the distance
between media. We will try several and choose the one giving the best
results, i.e. the clearest clustering. The methods we have selected are:
* Use [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
(*term frequency-inverse document frequency*) on the sets of words, or on speakers
having spoken for a specific media, in order to give a bigger
weight to more "significant" words or people.   
Then either use PCA[^5] to project these vectors in a smaller subspace along the axis with the larger variance.  
Or [LSI](https://en.wikipedia.org/wiki/Latent_semantic_analysis) (*Latent semantic indexing*)
which, applied on term-newspaper TF-IDF matrix, extracts the main topics. We thus obtain smaller dimension features representing the importance of a topic for a newspaper. This can be similary applied on the TF-IDF matrix of the speakers.  
Finally run k-means (with euclidean distance) on the resulting vectors. For the choice of k
we can start from the number of consortia, then decrease k from there. The reasoning
is that there cannot be more than k clusters given our criteria, but there can still
be some overlap between different consortia.

* For each media, remember the set of citees, the distance measure is be
the Jaccard similarity on these sets. We then run some clustering algorithms
using jaccard algorithm, e.g. DBSCAN on the media. Note that Jaccard similarity may be problematic in
our case, because small sets (e.g. small media) cannot be similar to big sets.

[^5]: PCA reduces the computational complexity of further algorithms (e.g. k-means),
and for dimensions <= 3 can be used to visualize clusters.

## Organization within the team.
* Antoine & Jonas
  * Quotes and speakers preprocessing
  * Creation of TF-IDF matrices
  * Implementation of different pipeline to cluster newspaper
  * Visualization
* Hugo & Marin
  * Data extraction / scraping (wikidata)
  * Code documentation
  * Data story
  * Website
  * Visualization
