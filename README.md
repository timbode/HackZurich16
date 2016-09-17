#README

In our project we apply machine learning to the field of biophysics,more 
precisely to bacterial run-and-tumble migration (see exampleTrajectory.png). This migration produces very
rich and enourmous data-sets. However, classification of run (nearly constant velocity, moderate angle change only 
due to diffusion) and tumble phases (high angle changes coming with an instant drop of velocity) is still a big issue
in this field due to the high underlying noise due to diffusion and experimental error fluctuations.
With our project we want provide an environment to enable the user to investigate big datasets of bacterial migration
easily. 

Our first approach was using visual recognition on IBM Watson with the help of the mentors of the IBM team. However,
this led to no succes. We had to program our own decision tree. Having a training dataset, we are able to train our 
program to classify run and tumble phases (see code classifyTrajectories.py). Results are not yet optimal due to
the bad training data set (see classified.png). 

Further work should include besides better training datasets stopping phases and helical trajectories.
