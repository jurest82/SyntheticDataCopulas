import matplotlib.pyplot as plt


def scatter(df_real, df_synthetic):

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 2, 1)
    plt.scatter('X', 'Y', data=df_real, label='real')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend(fontsize=15)

    plt.subplot(1, 2, 2)
    plt.scatter('X', 'Y', data=df_synthetic, label='synthetic', color='r')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend(fontsize=15)
