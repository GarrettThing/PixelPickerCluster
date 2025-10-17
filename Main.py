from imghdr import tests

import cv2
import numpy as np
import sys

radius = 1
def main():
    image=cv2.imread("/Users/garrettclark/PycharmProjects/PixelPickerCluster/Pixel Picker Cluster/Yes.png")
    window = np.zeros(image.shape,dtype=image.dtype)
    cv2.imshow("hi",image)
    cv2.waitKey(1000)
    k_att = 5

    # for y in image:
    #     print("next row of pixels: ")
    #     for x in y:
    #         print(str(x))
    db_scan(image,k_att)

def db_scan(img,k):

    test_attractor = []
    test_cluster = []


    for y in range(int(len(img)/10)):
        for x in range(int(len(img[y])/10)):

            cur_cluster = cluster(img,[],[x*10,y*10])

            if cur_cluster[0] not in test_cluster:
                test_attractor.append([x,y])
                test_cluster.append(cur_cluster)

    print('doh')
    while len(test_cluster) > k:
        remove_ind = -1
        smallest = 10000000
        for cur in range(len(test_cluster)):
            cur_len = len(test_cluster[cur])
            if cur_len < smallest:
                smallest = cur_len
                remove_ind = cur
        test_attractor.pop(remove_ind)
        test_cluster.pop(remove_ind)

    print(test_cluster)

    for pixel in range(len(test_attractor)):
        img[test_attractor[pixel][0]][test_attractor[pixel][1]] = img[test_cluster[pixel][0]][test_cluster[pixel][1]]

def cluster(img, cur_cluster, cur_pixel)-> list:
    global radius
    # method to cluster points together
    # returns a list of x,y for each pixel within the cluster

    cur_cluster.append(cur_pixel)
    # print(cur_pixel)
    for y in range(len(img)):
        for x in range(len(img[y])):

            if img[cur_pixel[1]][cur_pixel[0]][0] + radius > img[y][x][0] > img[cur_pixel[1]][cur_pixel[0]][0] - radius:
                if img[cur_pixel[1]][cur_pixel[0]][1] + radius > img[y][x][1] > img[cur_pixel[1]][cur_pixel[0]][1] - radius:
                    if img[cur_pixel[1]][cur_pixel[0]][2] + radius > img[y][x][2] > img[cur_pixel[1]][cur_pixel[0]][2] - radius:
                        if [x,y] not in cur_cluster:
                            # print("new loop")
                            # print(x, y)
                            # print(cur_cluster)
                            cur_cluster.append(cluster(img,cur_cluster,[x,y]))
    return cur_cluster




if __name__ == "__main__":
    main()