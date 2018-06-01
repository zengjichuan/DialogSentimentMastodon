# This is the main script to run experiments with the hierarchical RNN on dialog act recognition and sentiment classification of Mastodon Twitter-like social network dialogs.
# By default, it will run a unique experiment over a single fold of a joint dialog-act & sentiment model.

XPtype="fast"

# If you want to reproduce the experiments of the paper
# XPtype="crossvalidation"

# requirements:
# - linux OS (tested on Ubuntu 16.04.4 LTS) with bash and python 2.7.12
# - pytorch (tested with version 0.3.0.post4) must be installed within a virtualenv located at $HOME/envs/pytorch

if [ ! -f $HOME/envs/pytorch/bin/activate ]; then
    echo "ERROR: you must have pytorch installed in a virtualenv in $HOME/envs/pytorch"
    exit
fi

curdir=""$(pwd)
echo "#!/bin/bash" > runda.sh
echo 'source $HOME/envs/pytorch/bin/activate' >> runda.sh
echo 'cd "'$curdir'"' >> runda.sh
echo 'i=$(echo $1 | cut -d_ -f1)' >> runda.sh
echo 'j=$(echo $1 | cut -d_ -f2)' >> runda.sh
echo 'echo "fold $i trainsize $j"' >> runda.sh
echo 'python xpMT.py $i 100 100 0.001 500 $j | tee logdase.$i.$j' >> runda.sh
chmod 755 runda.sh

if [ $XPtype -e "fast" ]; then
    # run a single experiment on Fold 0 with training corpus of size 1 (see Figure 2, part of the first point on the left)
    bash ./runda.sh "0_1"
else
    # run 10 fold-crossvalidation with varying training corpus size (see Figure 2 of the paper)
    # launch ./runda.sh 140 times with various parameters
    # the results will be saved in logdase.fold.tsize
    for i in 0 1 2 3 4 5 6 7 8 9; do
       for tsize in 1 10 50 100 150 200 100000; do
           parms=$i"_"$tsize
           bash "./runda.sh $parms\""
           # The same experiment is run a second time to avoid badly initialized parameters
           parms=$i"_0"$tsize
           bash "./runda.sh $parms\""
       done
    done
fi


