SIMULATION OF CO-60 POINT SOURCE

This template sets up the simulation of a Co-60 source (spherical, radius = 0.5 mm) at a given location and for a given number of decay events.
It creates 8 simulations, which can be run sequentially or simulataneously to save time. Finally, the results of the 8 simulations are combined and analysed.
For this text, define:
[x]: x-position of the source
[y]: y-position of the source
[z]: z-position of the source
[Nevents]: Number of events to be simulated per sub-simulation, i.e., the total number of events is [Nevents] times 8.


####AUTOMATED SIMULATION####

1. Open new_sim.sh and change the DIRECTORY key to the present working directory.

2. Use the new_sim.sh script as follows to simulate the source at the desired position:
	bash new_sim.sh [x] [y] [z] [Nevents]
   This can be run on a cluster PC as long as a legend software singularity is available. It uses /unix/legend/software/ruben/legend-software.sif at the moment.
   Alternatively, submit this as a job to the bash farm using:
	qsub -q [queue] -F "[x] [y] [z] [Nevents]" new_sim.sh

3. Collect the outputs of the simulation from the output/ folder:
	-[ARGS]_Interspec.csv: Histogram of the detected energy events to be viewed in Interspec.
	-[ARGS]_peak_counts.csv: List of the registered counts at 1173 keV, 1332 keV and 2505 keV with their associated uncertainties. Also includes the ratios of the summation peak to the photopeaks.
	-[ARGS]_countsphour.csv: Same as above, however, scaled down to counts per hour. This assumes that the source is No. 43 in the department's inventory of sources with a present activity of (5.476 \pm 0.359) kBq. 


####MANUAL SIMULATION####

There are two options with different degrees of manualisation.

A) Full manual simulation

  1. Copy the template folder in the same directory and give it a suitable name.

  2. Run set_pos.sh entering the source position and the desired number of events as follows:
	bash set_pos.sh [x] [y] [z] [Nevents]  
     Then run
	bash replicate_P1.sh

  3. In each of the P* folders, there is a run.sh script. This has to be executed individually in every folder.

  4. After the script finishes in a P* folder, move the energies_res.csv file into the summary/ folder, renaming it to [foldername].csv, where [foldername] is the folder it originates from, e.g., P2.csv

  5. Go into summary/ and use python to run main_final.py. This generates all output files in the summary/ folder ready for use.

B) Split up the job with qsub.sh, qsub1.sh and qsub2.sh

  1. Follow steps 1 and 2 in A)

  2. Run qsub.sh. This is scripted to run all simulations in the P* folder and to carry out the final analysis. Results are left in the summary/ folder.
     Alternatively: Run qsub1.sh and qsub2.sh (preferably at the same time using tmux or similar). The first script runs simulations P1 to P4, the second runs simulations P5 to P8.

  3. When splitting the job up using qsub1.sh and qsub2.sh, analysis must be carried out manually. Refer to step A5.


####COMPARE TO A REAL MEASUREMENT OF SOURCE NO. 43####

It is possible to prepare the simulation outputs in ways to allow for a direct spectrum comparison with a measured spectrum in Interspec.

  1. Complete the simulation using one of the methods laid out above.
  2. Go into the summary/ folder inside the simulation folder.
  3. Edit main_final.py.
  4. In the main()-method, change the "time" variable to the live time over which the real spectrum was recorded.
  5. The main_final.py script calls a method in hist_class.py, which calculated a scaling factor by which the Interspec simulation output will be scaled in oder to represent the same "source time" as the real spectrum. This is done assuming the source activity of source No 43 as 5.476 kBq. 


####SIMULATE OTHER SOURCES####

Other sources can be simulated by editing the sim_point_source.mac and point_source.gdml file in P1/ in the template.
In the macro edit the /gps/ion commands to the parameters of the desired source.
In the point_source.gdml file define the source material as the correct isotope composition in gdml language. (See g4simple tutorials)
The python analysis files can be adjusted to the new source, too. I tried to include some commenting and documentation in the code to make this more intuitive.
Some lines in hist_class.py main(), which are commented out, have been used before to simulate Bi-207 and Bi-214.


####
~Ruben Hoenscheid (20/07/23)
Email: ruben.honscheid.20@ucl.ac.uk

