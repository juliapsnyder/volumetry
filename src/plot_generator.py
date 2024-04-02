import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class PlotGenerator:
    """Generates and saves plots based on the processed data."""

    @staticmethod
    def generate(data_frames: pd.DataFrame, folder_path: str, mouse_id: str) -> None:
        """Generates and saves a plot for the merged data using Seaborn.

        Args:
            data_frames: The merged DataFrame containing all data to be plotted.
            folder_path: The path to the folder where the plot will be saved.
            mouse_id: The ID of the mouse, used for naming the plot file.
        """

        sorted_data_frames = data_frames.sort_values(by='Timepoint')
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=sorted_data_frames, x='BinCal', y='Perc_Area', hue='Timepoint', marker='o', style='Timepoint', dashes=False)
        
        plt.xlabel('BinCal')
        plt.ylabel('Perc_Area')
        plt.title(f'Mouse ID: {mouse_id}')
        plt.legend(title='Timepoint')
        plt.savefig(f'plots/perc_area/{mouse_id}_perc_area.png')
        plt.close()

    @staticmethod
    def generate_cumulative(data_frames: pd.DataFrame, folder_path: str, mouse_id: str) -> None:
        """Generates and saves a plot for the merged data using Seaborn, with cumulative Perc_Area.

        Args:
            data_frames: The merged DataFrame containing all data to be plotted.
            folder_path: The path to the folder where the plot will be saved.
            mouse_id: The ID of the mouse, used for naming the plot file.
        """
        sorted_data_frames = data_frames.sort_values(by='Timepoint')
        
        sorted_data_frames['Cumulative_Perc_Area'] = sorted_data_frames.groupby('Timepoint')['Perc_Area'].cumsum()
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=sorted_data_frames, x='BinCal', y='Cumulative_Perc_Area', hue='Timepoint', marker='o', style='Timepoint')
        
        plt.xlabel('BinCal')
        plt.ylabel('Cumulative Perc_Area')
        plt.title(f'Mouse ID: {mouse_id} - Cumulative')
        plt.legend(title='Timepoint')
        plt.savefig(f'plots/cumulative_perc_area/{mouse_id}_cumulative_perc_area.png')
        plt.close()