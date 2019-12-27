# import matplotlib
# from matplotlib import pyplot as plt 
import numpy as np
import datetime
# from scipy.interpolate import spline
# import scipy.signal as signal
# import scipy.io as scio
# matplotlib.use('PDF')

class Plot(object):
    def __init__(self):

        pass
    
    def plot_data_lists(self, y_list, x_list, legend_list, 
                        title, 
                        figure_name, 
                        xlabel, 
                        ylabel, 
                        length, 
                        height, 
                        label_fsize, 
                        plotArg_list):
        '''
        data_list: 数据列表
        label_list: label列表
        把这些data画在一张图上
        '''
        assert len(x_list) == len(y_list) == len(legend_list) == len(plotArg_list), "list length not equal."
        for x, y in zip(x_list, y_list):
            assert len(x) == len(y), 'data length not equal.'
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots(figsize=(length, height))
        ax.grid(True)

        # color_list = plotArgs['colorList']
        # lineStyle_list = plotArgs['lineStyleList']
        # marker_list = plotArgs['markerList']
        for x, y, legend, plotArg in zip(x_list, y_list, legend_list, plotArg_list):
            ax.plot(x,y, label=legend, **plotArg) 
        # 图线主要是这三个属性：linestyle, color, marker。更多信息：https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html
        # markers = ['o', 'p', 'v', 's', 'D']

        # ax.plot()
        ax.set_xlabel(xlabel, fontsize=label_fsize)
        ax.set_ylabel(ylabel, fontsize=label_fsize)
        ax.set_title(title)
        ax.legend()
        ax.grid(True)
        plt.savefig(figure_name)
        plt.close('all') # 关闭figure

    def plot_fill_var(self, y_list, std_list, x_list, legend_list, title, xlabel, ylabel, plotArg_list, figure_name):
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.grid(True)
        for x, y, std, legend, plotArg in zip(x_list, y_list, std_list, legend_list, plotArg_list):
            ax.plot(x,y, label=legend, color=plotArg['color']) 
            ax.fill_between(x, y+std, y-std, facecolor=plotArg['facecolor'], alpha=0.4)
        
        ax.legend(loc='upper left')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        # plt.show()
        plt.savefig(figure_name)
        plt.close('all')
        pass


# if __name__ == "__main__":
    
    # plot_Q_S_rewards()
    # plot_accuracy()
    # data_padding()
    # plot_regrets()
    
