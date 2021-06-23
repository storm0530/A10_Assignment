import math
import numpy as np
import matplotlib.pyplot as plt
import sys

K_NUM = 3
INIT_COLOR = "black"
COLOR = ["red","dodgerblue","goldenrod"]

# 2点間の距離を求める関数
def distance(x1,y1,x2,y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

def get_centroid(cls_data):
    '''
    cls_data: 座標リスト
        shape=(K_NUM,[x,y]が入ったリストの長さ)
        例: [
                # クラスタ番号0に属する座標
                [
                    [x1,y1],[x3,y3],...
                ],
                # クラスタ番号1に属する座標
                [
                    [x6,y6],[x4,y4],...
                ],
                # クラスタ番号2に属する座標
                [
                    [x2,y2],[x5,y5],...
                ]
        ]
    返り値 centroids: centroidのリスト 例:[[2,10],[5,8],[1,2]]
    '''

    centroids = []
    
    for i in range(len(cls_data)):
        sum_x = 0
        sum_y = 0
        num = len(cls_data[i])

        for j in range(num):
            sum_x += cls_data[i][j][0]
            sum_y += cls_data[i][j][1]
        
        centroids_x = sum_x/num
        centroids_y = sum_y/num
        centroids.append([centroids_x, centroids_y])

    return centroids


# centroidのどれに属するかを求める関数
def devide_cluster(centroids,data):
    '''
    centroids: centroidのリスト 例:[[2,10],[5,8],[1,2]]
    data: 対象の座標リスト 例: [[2,10],[3,2],[12,8],...]
    
    返り値 cls_centroids: クラスタリング後のcentroidのリスト 例:[[2,10],[5,8],[1,2]]
    
    返り値 cls_data: クラスタリング後の座標リスト
        shape=(K_NUM,[x,y]が入ったリストの長さ)
        例: [
                # クラスタ番号0に属する座標
                [
                    [x1,y1],[x3,y3],...
                ],
                # クラスタ番号1に属する座標
                [
                    [x6,y6],[x4,y4],...
                ],
                # クラスタ番号2に属する座標
                [
                    [x2,y2],[x5,y5],...
                ]
        ]
    '''

    # 初期化
    cls_data = []
    for i in range(len(centroids)):
        cls_data.append([])


    for i in range(len(data)):
        cls = 0
        min_d = distance(data[i][0],data[i][1],
        centroids[0][0],centroids[0][1])

        if K_NUM >= 2:
            for j in range(1,K_NUM):
                d = distance(data[i][0],data[i][1],
                centroids[j][0],centroids[j][1])
                if d < min_d:
                    cls = j
                    min_d = d  
        cls_data[cls].append(data[i])
    
    cls_centroids = get_centroid(cls_data)
    return cls_centroids, cls_data

# クラスタリングの可視化関数
def visualize(step,cls_data,centroids):
    '''
    step: k-meansの何ステップ目か
    cls_data: shape=(K_NUM,[x,y]が入ったリストの長さ)
        例: [
                # クラスタ番号0に属する座標
                [
                    [x1,y1],[x3,y3],...
                ],
                # クラスタ番号1に属する座標
                [
                    [x6,y6],[x4,y4],...
                ],
                # クラスタ番号2に属する座標
                [
                    [x2,y2],[x5,y5],...
                ]
        ]
    centroids: centroidのリスト 例:[[2,10],[5,8],[1,2]]
    '''

    fig = plt.figure()
    plt.title(f'Step{step}', fontsize=24)

    for i in range(len(cls_data)):
        cls_data_x = [cls_data[i][j][0] for j in range(len(cls_data[i]))]
        cls_data_y = [cls_data[i][j][1] for j in range(len(cls_data[i]))]
        plt.scatter(cls_data_x, cls_data_y, s=50, c=COLOR[i])

    for i in range(len(centroids)):
        plt.scatter(centroids[i][0],centroids[i][1],
        s=60,c=COLOR[i],linewidths=1,edgecolors="black")

    fig.savefig(f"./k-means_visualization/result_step{step}.png")

# 最終結果を可視化する関数
def last_visualize(cls_data):
    '''
    cls_data: shape=(K_NUM,[x,y]が入ったリストの長さ)
        例: [
                # クラスタ番号0に属する座標
                [
                    [x1,y1],[x3,y3],...
                ],
                # クラスタ番号1に属する座標
                [
                    [x6,y6],[x4,y4],...
                ],
                # クラスタ番号2に属する座標
                [
                    [x2,y2],[x5,y5],...
                ]
        ]
    '''

    fig = plt.figure()
    plt.title(f'Step Final', fontsize=24)

    for i in range(len(cls_data)):
        cls_data_x = [cls_data[i][j][0] for j in range(len(cls_data[i]))]
        cls_data_y = [cls_data[i][j][1] for j in range(len(cls_data[i]))]
        plt.scatter(cls_data_x, cls_data_y, s=50, c=COLOR[i])

    fig.savefig(f"./k-means_visualization/result_final.png")
    

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

# From this, main process

data = [
    [2,10],
    [2,5],
    [8,4],
    [5,8],
    [7,5],
    [6,4],
    [1,2],
    [4,9]
    ]
init_centroids = [[2,10],[5,8],[1,2]]

    
step = 0
print(f"k-meansによるクラスタリング Step{step}")
fig = plt.figure()
plt.title(f'Step{step}', fontsize=24)

data_x = [data[i][0] for i in range(len(data))]
data_y = [data[i][1] for i in range(len(data))]
plt.scatter(data_x, data_y, s=50, c=INIT_COLOR)

for i in range(len(init_centroids)):
    plt.scatter(init_centroids[i][0], init_centroids[i][1],
    s=60,c=COLOR[i],linewidths=1,edgecolors="black")
fig.savefig(f"./k-means_visualization/result_step{step}.png")



step = 1
print(f"k-meansによるクラスタリング Step{step}")
cls_centroids, cls_data = devide_cluster(init_centroids,data)
visualize(step, cls_data, cls_centroids)

centroids = init_centroids
if centroids == cls_centroids:
    print("k-meansによるクラスタリング終了")
    sys.exit()
else:
    while(centroids != cls_centroids):
        step += 1
        print(f"k-meansによるクラスタリング Step{step}")
        centroids = cls_centroids
        cls_centroids, cls_data = devide_cluster(centroids,data)
        visualize(step, cls_data, cls_centroids)
    
    print("k-meansによるクラスタリング終了")
    last_visualize(cls_data)
    