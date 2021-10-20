from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import statistics


def bostonFunc():
    boston = load_boston()
    X = boston.data
    Y = boston.target

    x = range(0, boston.data.shape[0],1)

    CRIME =  0; ZN = 1; INDUSTRIAL = 2; ROOMS=5; DISTANCE =7 ;

    plt.figure(figsize=(30,8))

    plt.plot(x, X[:,INDUSTRIAL],"y-", label='Industrial')
    plt.plot(x, X[:,DISTANCE],"b-", label='Distance')
    plt.plot(x, X[:,ROOMS],"c-", label='Rooms')
    plt.rcParams.update({'font.size':18})
    plt.legend(prop={'size':22}); plt.grid();
    print(X.shape)
    print(Y.shape)
    print(X[0:3,:])
    print(Y[0:5])
    print(X[0:ZN])
    print(X[1:3,CRIME])
    print(boston.data.shape[0])
    print(boston.data.shape[1])

    mean=[]; variance=[]
    for i in range(boston.data.shape[1]):
        mean.append(statistics.mean(X[:,i]))
        variance.append(statistics.variance(X[:,i]))

    for i in range(boston.data.shape[1]):
        print(format(i) + "mean : {:.2f}".format(mean[i]) + ", variance: {:.2f}".format(variance[i]))

    #fig,axs = plt.subplots(1,2, figsize={7, 4})

    #3D Scatter of two figures
    #axs[1] = Axes3D(fig, elev=40, azim=30)
    #axs[1].scatter(X[:,DISTANCE], X[:,ROOMS], "y", c='b',marker='o')
    #axs[1].set_xlabel("Distance", fontsize=22)
    #axs[1].set_ylabel("Rooms", fontsize=22)
    #axs[1].set_zlabel("Boston", fontsize=22)

    plt.show()

if __name__ == '__main__':
    bostonFunc()
    print("It Finished Succesfully")


