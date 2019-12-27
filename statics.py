import numpy as np 
import pandas as pd 
import os
import glob
# import sys
# sys.path.append('../')
import plot


def mean_var():
    pass

def save_csv_data(filename, data_dict):
    df = pd.DataFrame(data_dict)
    df.to_csv(filename)

def load_csv_data(filename, key):
    df = pd.read_csv(filename)
    value = df[key]
    return value

 
def find_files():
    files = glob.glob("/home/xiawenwen/workspace/IMFB-KDD2019-master/SimulationResults/nonlinear_1557/reward/*.csv")
    imgucb_mat = []
    imfb_mat = []
    for f in files:
        # print(f)
        df = pd.read_csv(f)
        imgucb_mat.append(df['IMGUCB'])
        imfb_mat.append(df['IMFB'])
    imgucb_mat = np.array(imgucb_mat)
    imfb_mat = np.array(imfb_mat)

    imgucb_mean = np.mean(imgucb_mat, axis=0)
    imgucb_std = np.sqrt( np.var(imgucb_mat, axis=0) )

    imfb_mean = np.mean(imfb_mat, axis=0)
    imfb_std = np.sqrt( np.var(imfb_mat, axis=0) )

    figure_name = 'reward_1557.pdf'
    p = plot.Plot()
    p.plot_fill_var([imgucb_mean, imfb_mean], [imgucb_std, imfb_std], [range(1, len(imgucb_mean)+1), range(1, len(imgucb_mean)+1)],
                    legend_list=['IMGUCB', 'IMFB'], 
                    title='Reward', 
                    xlabel='Round', 
                    ylabel='Reward', 
                    plotArg_list=[{'color': 'red', 'facecolor': 'red'},
                    {'color': 'blue', 'facecolor': 'blue'}],
                    figure_name=figure_name)


    print(imgucb_mat.shape, imfb_mat.shape)


if __name__ == "__main__":
    find_files()



