# DialogSentimentMastodon
Corpus and code for multi-task models of dialog acts and sentiments on Mastodon

This directory contains the code and the corpus required to reproduce the results of the paper
"Multi-task dialog act and sentiment recognition on Mastodon" published at COLING 2018.

## Objective

This repository distributes two components:

- A novel Twitter-like dialog corpus in English with a permissive license, which has been extracted from the Mastodon social network.
- A two-layer hierarchical multi-task recurrent neural network that jointly models dialog acts and sentiments on this corpus.

The objective of this work is twofold:

- To set-up a new reproducible experimental setup and baseline for dialog act and sentiment analysis in social media
- To evaluate the correlation between both tasks (dialog act recognition and sentiment analysis) based on the proposed multi-task model

Please refer to the COLING 2018 paper "Multi-task dialog act and sentiment recognition on Mastodon" for further details.

HOW TO USE
==========

Requirements
------------

- linux OS (tested on Ubuntu 16.04.4 LTS) with bash and python 2.7.12
- pytorch (tested with version 0.3.0.post4) that must be installed within a virtualenv located at $HOME/envs/pytorch


Datasets
--------

The corpus is already pre-treated and may be used as it is with the provided software.
In particular, the training corpus has been split into ten folds to enable cross-validation.
The training files are: tmptrain.wds.{0-9} and the corresponding development files are tmpdev.wds.{0-9}
In addition, the files tmptrain.tootids.{0-9} are also given: they contain the identifier of the post
in the octodon.social Mastodon instance, so that the complete post with all metadata may be retrieved.

There is a single test file: datatestJoint.idx
For convenience, datatestJoint.txt and datatrainJoint.txt are also given, with the posts in plain English.

In all these data files, the first column contains the index of the post within a dialog;
so every new dialog starts with "0".
The second column contains the labels of the post, separated by an underscore "_": the first label is the sentiment, and the second label is the dialog act.
The third and following columns contain the words of the post.

HOW TO REPRODUCE EXPERIMENTS OF THE PAPER
============================

You may run a single experiment (training and test of the joint multi-task model on one data fold) by executing:

```
cd code/hierarchicalRNN
./launch.sh
```

You may also experiment with mono-task, or with various limited corpus size, by editing the file xpMT.py: please look at the comments in this file for details.

Note that in order to fully reproduce all experiments of the paper, we have parallelized our experiments over 140 nodes of a computer cluster for several days.
But single experiments of the paper may easily be reproduced within a few hours for a single data fold, and a few days for the full cross-validation.

LICENSE
=======

The code is distributed under the open-source MIT license.
The corpus is distributed under the Creative Commons license, because the content partly comes from Mastodon (see for insance https://forum.etalab.gouv.fr/tos#3 ).
Please contact me for details about copyrights and licenses.

# Credits

- Annotation guide
  - Somayeh Jafaritazehjani
  - Adedayo Oluokun
- Corpus annotations
  - Somayeh Jafaritazehjani
  - Adedayo Oluokun
- Pytorch code
  - Christophe Cerisara
  - Hoa T. Le

