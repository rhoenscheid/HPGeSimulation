# HPGeSimulation


## Efficiency Simulations
  Download the efficiency folder and unpack the .zip file to obtain the "template" folder in your working directory. Create an empty "output" folder in the same directory. There is a new_sim.sh file, which will run everything automatically. However, also in the .zip file are instruction on how to manually run the simulation.
  run new_sim.sh [x] [y] [z] [Nevents]
    x: x-coordinate of the test point
    y: y-coordinate of the test point
    z: z-coordinate of the test point
    Nevents: number of events simulated at each energy
    This will copy the template and configure it according to the x,y,z coordinates passed to the simulation. It then runs the scenario at different energies (20keV, 30keV, 50keV, 80keV, 100keV, 200keV, 300keV, 500keV, 800keV, 1000keV, 1200keV, 1400keV, 1600keV, 1800keV, 2000keV, 2200keV, 2400keV).
    Detection efficiency at each energy will be computed and output into an efficiency csv file. Additionally, three curves are fit to the data, the fit paramters of which are output into separate files in the output/ folder.

## Co-60 Source Simulations
