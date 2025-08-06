# This code is for categorize
import pandas as pd
import numpy as np

def categorize_submovement_duration(submovement_boundaries):
    """
    categorizes the submovements in each activity bouts.

    Parameters:
    - submovement_boundaries: The submovment boundary indices for each activity bout.
    
    Returns:
    - short_duration_PC1, long_duration_PC1, short_duration_PC2, long_duration_PC2
    - short and long duration submovement boundaries for PC1 and PC2
    """
    
    # Lists to store the categorized durations
    # each list will contain tuples of values of zero crossing index and bout no of a submovement
    # for example short_duration_PC1[10] will contain a 3 element tuple with the boundary indices 
    # of a submovement and the bout_no of that submovement like (195, 204, 2)
    short_duration_PC1 = []
    long_duration_PC1 = []
    short_duration_PC2 = []
    long_duration_PC2 = []

    sampling_freq = 30  # Sampling frequency in Hz

    # looping through each bout
    for bout_no, boundaries in enumerate(submovement_boundaries):

        # pc1_boundary and pc2_boundary contrains the boundaries of submovements for PC1 and PC2
        pc1_boundary, pc2_boundary = boundaries  # Extract PC1 and PC2 boundaries

        # Process PC1
        # looping the each zero crossing point
        for i in range(len(pc1_boundary) - 1):

            # calculating duration between a pair, dividing by sampling freq to get duration in seconds
            duration = (pc1_boundary[i + 1] - pc1_boundary[i]) / sampling_freq

            # for short duration and PC1
            if 0.05 <= duration <= 0.6:
                short_duration_PC1.append((pc1_boundary[i], pc1_boundary[i + 1], bout_no))

            # for long duration and PC1
            elif 0.6 < duration <= 5:
                long_duration_PC1.append((pc1_boundary[i], pc1_boundary[i + 1], bout_no))

        # Process PC2 similarly
        for i in range(len(pc2_boundary) - 1):
            duration = (pc2_boundary[i + 1] - pc2_boundary[i]) / sampling_freq
            if 0.05 <= duration <= 0.6:
                short_duration_PC2.append((pc2_boundary[i], pc2_boundary[i + 1], bout_no))
            elif 0.6 < duration <= 5:
                long_duration_PC2.append((pc2_boundary[i], pc2_boundary[i + 1], bout_no))
                
    return short_duration_PC1, long_duration_PC1, short_duration_PC2, long_duration_PC2

