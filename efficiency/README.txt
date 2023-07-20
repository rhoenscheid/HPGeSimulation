EFFICIENCY CURVE GENERATION

This template sets up the simulation environment for an efficiency curve at a given location.
Source: Sphere of 1mm radius, containing a Geant4 gamma source, which emits radiation at specified energies.
Energies: 20 keV, 30 keV, 50 keV, 80 keV, 100 keV, 200 keV, 300 keV, 500 keV, 800 keV, 1000 keV, 1200 keV, 1400 keV, 1600 keV, 1800 keV, 2000 keV, 2200 keV, 2400 keV

####AUTOMATIC SIMULATION####

The new_sim.sh script completes a simulation with given x,y,z and Nevents variables: The DIRECTORY key in the script has to be changed to the PWD. 
Create also an output/ folder so the script can move the completed simulation outputs there.
	bash new_sim.sh [x] [y] [z] [Nevents]
	x: x-coordinate, y: y-coordinate, z: z-coordinate, Nevents: number of events simulated at each energy.
This can be executed locally, assuming that a LEGEND software container is availabel at /unix/legend/software/ruben/legend-software.sif.
Alternatively, submit this as a job to the bash farm via:
	qsub -q [queue] -F "[x] [y] [z] [Nevents] new_sim.sh
where the variables have the same meaning as outlined above. The queue can be short / medium / long.
After one simulation, expect to find the following files in output/:
	-[ARGS]_fit_deg4.png : Efficiency curve with a curve_fit of degree 4.
	-[ARGS]_df.csv : List of energies and associated detection efficiencies.
	-[ARGS]_parametersN.csv : List of fitting parameters for a fit of degree N, where N can take values 2, 3, 4.
	-[ARGS]_parametersN_unc.csv : List of uncertainties in the fit parameters for the fit of degree N.


####MANUAL SIMULATION####

1. Copy the template folder via "cp -r template/ [FOLDERNAME].
2. Enter the new folder. Set the position and number of events to be simulated at each energy. This is done automatically by set_pos.sh. Syntax:
	bash set_pos.sh [x] [y] [z] [Nevents]
	x: x-coordinate, y: y-coordinate, z: z-coordinate, Nevents: number of events simulated at each energy.
3. Run qsub.sh. This will complete the simulation at every energy in one large job. The outputs can be collected from the final_analysis/ folder.
	Outputs:
	-Fitted_Curve_degN.png where N is the degree of the fit : Efficiency curves
	-energies.csv : List of all detected energies in all simulations
	-Interspec_spectrum.csv : Histogram file for use in Interspec. Shows a histogram of all detected energies in energies.csv
	-parameters_degN.csv : Fitting parameters determined for the fit of order N.
	-unc_degN.csv : Uncertainties associated with the fitting parameters of order N.

4. Alternative without qsub.sh:

  a. Having executed step 2, go into the folders, which have as names the energies they are simulating. 
  b. Enter a legend-software.sif container via "singularity run -B /unix [path to singularity]
  c. In the singularity, run "g4simple sim_point_source.mac"
  d. After this has finished, run "python main.py"
  e. The file "sim_out.root" takes a lot of diskspace and can be removed once the main.py script has finished.
  f. Repeat this procedure in every energy simulation folder.
  g. Once all done, run "bash to_merge.sh". This will merge everything into one energies.csv file for the final analysis.
  h. Go into final_analysis/ and run hist_efficiency.py. This will finally generate the outputs listed under step 2. above.

5. Recommended if using tmux:
  
  a. Execute steps 1 and 2. Then set up window panes in tmux on different cluster PCs.
  b. Have each pane execute one of the runN.sh files in run-files/. These split the simulation job up into smaller parts, according to:
	run1.sh - 20keV, 30keV, 2400keV
	run2.sh - 50keV, 80keV, 2200keV
	run3.sh - 100keV, 200keV, 2000keV
	run4.sh - 300keV, 500keV
	run5.sh - 800keV, 1000keV
	run6.sh - 1200keV, 1400keV
	run7.sh - 1600keV, 1800keV
  c. Once all jobs are finished, follow steps 4g and 4h.
  d. Note that this does not automatically remove the sim_out.root files from each energy folder. These have to be removed manually by the user. 

####
~Ruben Hoenscheid (20/07/23)
Email: ruben.honscheid.20@ucl.ac.uk

 
  
