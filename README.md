# HPGeSimulation
This is a summary of my work as a MAPS summer intern with the HEP group at UCL. Over six weeks, I created a simulation of our HPGe detector, which can be used to generate efficiency curves for a given location in space. Additionally, it can be employed to simulate the spectra of radioactive point sources in the detector.
My own efficiency curve outputs are in the output/ folder.

## Efficiency Simulations
  Download the efficiency folder and unpack the .zip file to obtain the "template" folder in your working directory. Create an empty "output" folder in the same directory. There is a new_sim.sh file, which will run everything automatically. However, also in the .zip file are instruction on how to manually run the simulation. 
  The file contains a README.txt, which details how to obtain an efficiency curve for at a given location in the detector.

## Co-60 Source Simulations
  Download the Co-60 folder and unpack the .zip file. Retrieve the "template" folder, the "output" folder and the new_sim.sh script into your working directory.
  Follow the instructions in the accompanying README.txt to simulate a Co-60 source in the detector.

## Geometry
  The simulation uses the .gdml language to set up the detector geometry as required by g4simple. The geometry files are:
    - detector_crystal.gdml: This is the Germanium crystal
    - cryostat.gdml: This is the Aluminium cryostat surrounding the crystal. It includes a solid 22mm thick base.
    - point_source.gdml: This is the source file, which creates a sphere of 0.5 mm radius to contain the source.
    - shielding_new.gdml: This is the lead and copper shielding around the detector.
    - nitrogen_supply.gdml: This is the thermal connection into the liquid nitrogen tank under the detector.
    - main_sim.gdml: This is the main geometry file which puts the pieces together. Coordinates of each part are specified at the beginning of this document.
  The macro file for simulations of sources is sim_point_source.mac. The macro for visualisations is vis_2.mac. It generates a HepRApp output to visualise the geometry.
