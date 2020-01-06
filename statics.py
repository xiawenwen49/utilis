import numpy as np 
import pandas as pd 
import os
import glob
# import sys
# sys.path.append('../')
import plot


def save_csv_data(filename, data_dict):
    df = pd.DataFrame(data_dict)
    df.to_csv(filename)

def load_csv_data(filename, key):
    df = pd.read_csv(filename)
    value = df[key]
    return value

 
def find_files():
    # files1 = glob.glob("/home/xiawenwen/workspace/IMFB-KDD2019-master/SimulationResults/linear_1440/reward/*12_31*IMGUCB_IMFB.csv")
    # files2 = glob.glob("/home/xiawenwen/workspace/IMFB-KDD2019-master/SimulationResults/linear_1440/reward/*12_30*LinUCB_egreedy_0.1_UCB1.csv")
    # files1.extend(files2)
    files1 = glob.glob("/home/xiawenwen/workspace/IMFB-KDD2019-master/SimulationResults/linear_1613/loss/*.csv")
    files = files1
    # figure_name = 'reward_linear_Flickr.pdf'
    figure_name = 'loss_linear_0_20_NetHEPT.pdf'
    
    imgucb_mat = []
    imfb_mat = []
    imlinucb_mat = []
    egreedy_mat = []
    ucb1_mat = []


    for f in files:
        df = pd.read_csv(f)
        if df.get('IMGUCB', None) is not None:
            imgucb_mat.append(df['IMGUCB'])
        if df.get('IMFB', None) is not None:
            imfb_mat.append(df['IMFB'])
        if df.get('LinUCB', None) is not None:
            imlinucb_mat.append(df['LinUCB'])
        if df.get('egreedy_0.1', None) is not None:
            egreedy_mat.append(df['egreedy_0.1'])
        if df.get('UCB1', None) is not None:
            ucb1_mat.append(df['UCB1'])
    
    data_list = []
    if len(imgucb_mat) != 0:
        data_list.append(imgucb_mat)
    if len(imfb_mat) != 0:
        data_list.append(imfb_mat)
    if len(imlinucb_mat) != 0:
        data_list.append(imlinucb_mat)
    if len(egreedy_mat) != 0:
        data_list.append(egreedy_mat)
    if len(ucb1_mat) != 0:
        data_list.append(ucb1_mat)
    
    data_list = list(map(lambda x:np.array(x), data_list))

    y_list = list(map(lambda x:np.mean(x, axis=0), data_list))
    std_list = list(map(lambda x:np.sqrt(np.var(x, axis=0)), data_list))

    num = len(y_list[0])
    x_list = [range(1, num+1) for i in y_list]
#  {'color':'green'}, {'color':'cyan'}, {'color':'magenta'},
    plotArg_list=[{'color': 'red', 'facecolor': 'red'},
                    {'color': 'blue', 'facecolor': 'blue'},
                    {'color': 'green', 'facecolor': 'green'},
                    {'color': 'cyan', 'facecolor': 'cyan'},
                    {'color': 'magenta', 'facecolor': 'magenta'},
                    ]

    
    p = plot.Plot()
    p.plot_fill_var(y_list, std_list, x_list,
                    legend_list=['IMGUCB', 'IMFB', 'IMLinUCB', '$\epsilon$-greedy', 'CUCB'], 
                    title='Reward', 
                    xlabel='Round', 
                    ylabel='Reward', 
                    plotArg_list=plotArg_list,
                    figure_name=figure_name)


if __name__ == "__main__":
    find_files()



