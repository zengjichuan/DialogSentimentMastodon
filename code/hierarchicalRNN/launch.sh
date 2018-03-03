# This script launches one experiment over 10 folds, with two runs per folds.
# The best number of epochs is averaged over the 10 development folds.
# This script further repeats this whole process 7 times, each time with an increasing size of the training corpus

# The latest pytorch environment should be installed with virtualenv in $HOME/envs/pytorch

# Note that this code precisely estimates F1 evaluation metrics, which can only be done by averaging across many experiments !
# So it is not possible to run these experiments on a single computer, as it would take forever.
# If you only have a single computer, you may however run the ./runda.sh script instead, which executes a single run.

# This script assumes that:
# - there exists a cluster called "cluster" with more than 140 nodes
# - all necessary data and code is available in all nodes at: $HOME/git/dasent/mastodon/pytorch

# prepare the main script and copies it into the cluster
echo "#!/bin/bash" > runda.sh
echo 'source $HOME/envs/pytorch/bin/activate' >> runda.sh
echo 'cd $HOME/git/dasent/mastodon/pytorch' >> runda.sh
echo 'i=$(echo $1 | cut -d_ -f1)' >> runda.sh
echo 'j=$(echo $1 | cut -d_ -f2)' >> runda.sh
echo 'echo "fold $i trainsize $j"' >> runda.sh
echo 'python xpMT.py $i 100 100 0.001 500 $j | tee logdase.$i.$j' >> runda.sh
chmod 755 runda.sh
scp runda.sh cluster:
scp *.py cluster:git/dasent/mastodon/pytorch/

# clean the previous logs
ssh cluster "rm -f git/dasent/mastodon/pytorch/logdase.*"

# launch ./runda.sh 140 times on the cluster with various parameters
# the results will be saved in logdase.fold.tsize
for i in 0 1 2 3 4 5 6 7 8 9; do
   for tsize in 1 10 50 100 150 200 100000; do
       parms=$i"_"$tsize
       ssh cluster "./runda.sh $parms\""
       parms=$i"_0"$tsize
       ssh cluster "./runda.sh $parms\""
   done
done


