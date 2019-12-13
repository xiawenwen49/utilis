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
    
    def plot_data_lists(self, y_list, x_list, label_list, length=10, height=6, x_label='x', y_label='y', label_fsize=14, save=True, figure_name='temp'):
        '''
        data_list: 数据列表
        label_list: label列表
        把这些data画在一张图上
        '''
        import matplotlib.pyplot as plt
        # if save:
        #     matplotlib.use('PDF')
        startTime = datetime.datetime.now()
        fig, ax = plt.subplots(figsize=(length, height))
        ax.grid(True)

        for y, x,  label in zip(y_list, x_list, label_list):
            ax.plot(x,y, label=label) 
        # 图线主要是这三个属性：linestyle, color, marker。更多信息：https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html
        # markers = ['o', 'p', 'v', 's', 'D']

        # ax.plot()
        ax.set_xlabel(x_label, fontsize=label_fsize)
        ax.set_ylabel(y_label, fontsize=label_fsize)
        ax.legend()
        ax.grid(True)
        
        plt.savefig(figure_name + str(startTime.strftime('_%m_%d_%H_%M'))+'.pdf')
        plt.show()

        # if save:
        #     plt.savefig(figure_name)
        # else:
        #     plt.show()




# def plot_regrets():
#     save = True
#     graph = 1
#     if save:
#         matplotlib.use('PDF')
    
#     result_dir = r'./results/regret_reserved/'

#     if graph == 1:
#         Q_regret_f = result_dir + r'regret_rlssp_Q_graph1_2019_05_25_14_46_53.csv'
#         SARSA_regret_f = result_dir + r'regret_rlssp_SARSA_graph1_2019_05_25_15_54_10.csv'
#         klhhr_regret_f = result_dir + r'regret_klhhr_graph1_2019_05_25_15_27_32.csv'
#         cucb_regret_f = result_dir + r'regret_cucb_graph1_2019_05_25_15_27_35.csv'
#         ts_regret_f = result_dir + r'regret_ts_graph1_2019_05_25_15_04_17.csv'
#     elif graph == 2:
#         Q_regret_f = result_dir + r'regret_rlssp_Q_graph2_2019_05_22_14_47_03.csv'
#         SARSA_regret_f = result_dir + r'regret_rlssp_SARSA_graph2_2019_05_25_15_57_54.csv'
#         klhhr_regret_f = result_dir + r'regret_klhhr_graph2_2019_05_22_15_59_58.csv'
#         cucb_regret_f = result_dir + r'regret_cucb_graph2_2019_05_22_16_02_55.csv'
#         ts_regret_f = result_dir + r'regret_ts_graph2_2019_05_25_14_16_37.csv'

    

#     files = [Q_regret_f, SARSA_regret_f, klhhr_regret_f, cucb_regret_f, ts_regret_f]
#     labels = ['$Q_{SSP}$, $\\alpha_0=0.25$', '$SARSA_{SSP}$, $\\alpha_0=0.25$', 'KL-HHR', 'CUCB', 'Thompson Sampling']
#     # load数据
#     datas = []
#     x = np.array([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) # x：需要画到图上的数据点的位置
#     for f in files:
#         data = utils.load_csv_data(f, 'regret').values
#         filtered = np.zeros(len(x)) # 需要画到图上的数据点
#         for i, index in enumerate(x):
#             filtered[i] = data[index//10] # //10 因为每隔10次记录一次
#         datas.append(filtered)
    
#     # 初始化图表
#     fig, ax = plt.subplots(figsize=(10, 6)) # 
#     fontsize = 14
#     # ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))

#     # 画图
#     markers = ['o', 'p', 'v', 's', 'D']
#     for i, filtered in enumerate(datas):
#         ax.plot(x, filtered, marker=markers[i], mec='none', ms=6, label=labels[i])

#     # 显示
#     ax.set_xscale('log')
#     # ax.set_yscale('log')
#     ax.ticklabel_format(axis='y', style='sci', scilimits=(-3, 4))
#     ax.grid(True)
#     ax.legend()
#     ax.set_xlabel('number of received packets', fontsize=fontsize)
#     ax.set_ylabel('regret', fontsize=fontsize)
#     plt.show()

#     if save:
#         plt.savefig(r'figures\regret-graph{}.pdf'.format(graph))

    

# if __name__ == "__main__":
    
    # plot_Q_S_rewards()
    # plot_accuracy()
    # data_padding()
    # plot_regrets()
    
