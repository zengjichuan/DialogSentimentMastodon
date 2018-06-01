# DialogSentimentMastodon
Corpus and code for multi-task models of dialog acts and sentiments on Mastodon

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

This directory contains the code and the corpus required to reproduce the results of the paper
"Multi-task dialog act and sentiment recognition on Mastodon"

LICENSE
=======

The code is distributed under the open-source MIT license.
The corpus is distributed under the Creative Commons license, because the content partly comes from Mastodon (see for insance https://forum.etalab.gouv.fr/tos#3 ).
Please contact me for details about copyrights and licenses.

HOW TO USE
==========

Datasets
--------

The corpus is already pre-treated and may be used as it is with the provided software.
In particular, the training corpus has been split into ten folds to enable cross-validation.
The training files are: tmptrain.wds.{0-9} and the corresponding development files are tmpdev.wds.{0-9}
In addition, the files tmptrain.tootids.{0-9} are also given: they contain the identifier of the post
in the octodon.social Mastodon instance, so that the complete post with all metadata may be retrieved.
However, to run the experiments of the paper, there is no need of the *.tootids.* files

There is a single test file: datatestJoint.idx
For convenience, datatestJoint.txt is also given, with the posts in plain English.

In all these data files, the first column contains the index of the post within a dialog;
so every new dialog starts with "0".
The second column contains the labels of the post, separated by an underscore "_": the first label is the sentiment, and the second label is the dialog act.
The third and following columns contain the words of the post.

HOW TO REPRODUCE EXPERIMENTS
============================

Assuming that you have the necessary computational resources, you can launch the baseline multi-task experiment by running:
./launch.sh

You may also experiment with mono-task, or with various limited corpus size, by editing the file xpMT.py: please look at the comments in this file for details.

Once all experiments are finished, you should run
python analyzeda.py <dir with logs> | grep TESTACC

This script will analyze all logs, find the best epoch on the dev corpus and print out both F1s corresponding to these epochs.

