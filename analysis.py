#Python Analysis Script"
import numpy as np
import uproot
import pandas as pd
import matplotlib.pyplot as plt


def get_df(filename):
    """
    Extract the pandas dataframe from the Root TTree.
    Input:
    -filename: Name of .root file
    Returns:
    -dataframe: Pandas dataframe with "event" and "Edep" column from .root file
    """
    print("Creating dataframe from file...")


    file = uproot.open(filename)
    tree = file["g4sntuple"]

    event_arr_0 = tree["event"].arrays(library='np')
    Edep_arr_0 = tree["Edep"].arrays(library='np')

    event_arr = np.array(event_arr_0['event'][:])
    Edep_arr = np.array(Edep_arr_0['Edep'][:][:])
    Edep_arr = [np.sum(Edep_arr[i]) for i in range(len(Edep_arr))]
    
    dataframe = pd.DataFrame(pd.DataFrame({'event' : event_arr, 'Edep' : Edep_arr}))

    dataframe.astype({'event': 'int64'})
    dataframe.astype({'Edep': 'float'})


    print("DataFrame created.")

    return dataframe

def hist_analysis(filename):
    """
    Obtain an array of the measured deposited energies.
    """

    dataframe = get_df(filename)

    energies = np.array(dataframe["Edep"])
    
    print("Computed deposited energies.")

    return energies

def plot_histogram(filename):
    """
    Use matplotlib to plot the histogram of deposited energies, given a .root file.
    """

    energies = hist_analysis(filename)
    bin_number = int(np.sqrt(len(energies))/3)

    print("Creating histogram with",bin_number,"bins.")

    plt.figure()
    
    plt.hist(energies, bins=bin_number, range=[0.01,2.5], histtype = 'step')
    plt.xlabel("Energy [MeV]")
    plt.ylabel("Number of Events")

    plt.title("Test Run with Co-60 Point Source")

    plt.savefig("TestRun_hist.png", dpi=300)

    print("Saved histogram.")


if __name__ == "__main__":

    plot_histogram("sim_out.root")

    print("Success.")
