from copy import *
import math
from math import *
from ex5_helper import *
import sys


def separate_channels(image):
    rows = len(image)
    columns = len(image[rows - 1])
    channels = len(image[rows - 1][columns - 1])
    new_img = []
    for k in range(channels):
        lst2 = []
        for i in range(rows):
            lst = []
            for j in range(columns):
                lst.append(image[i][j][k])
            lst2.append(lst)
        new_img.append(lst2)
    return new_img


def combine_channels(channels):
    rows = len(channels)
    columns = len(channels[rows - 1])
    image = len(channels[rows - 1][columns - 1])
    new_img = []
    for k in range(columns):
        lst2 = []
        for i in range(image):
            lst = []
            for j in range(rows):
                lst.append(channels[j][k][i])
            lst2.append(lst)
        new_img.append(lst2)
    return new_img


def calculate_grayscale(lst):
    return int(round(lst[0] * 0.2999 + lst[1] * 0.587 + lst[2] * 0.114))


def RGB2grayscale(colored_image):
    new_colored_image = []
    for i in range(len(colored_image)):
        lst = []
        for j in range(len(colored_image[i])):
            x = calculate_grayscale(colored_image[i][j])
            lst.append(x)
        new_colored_image.append(lst)
    return new_colored_image


def blur_kernel(size):
    if size < 0:
        size = abs(size)
    kernel_array = []
    for i in range(size):
        lst = []
        for j in range(size):
            x = (1 / (size * size))
            lst.append(x)
        kernel_array.append(lst)
    return kernel_array


def conv(mat1, mat2):
    summary = 0
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            summary += mat1[i][j] * mat2[i][j]
    if summary >= 255:
        return 255
    if summary <= 0:
        return 0
    return round(summary)


def get_k_mat(image, row, col, k):
    temp = [[image[row][col] for i in range(k)] for j in range(k)]
    index = k // 2
    z = 0
    y = 0
    for i in range(row - index, row + index + 1):
        for j in range(col - index, col + index + 1):
            if i >= len(image) or i < 0:
                y += 1
                continue
            if j >= len(image[row]) or j < 0:
                y += 1
                continue
            temp[z][y] = image[i][j]
            y += 1
        z += 1
        y = 0
    return temp


def apply_kernel(image, kernel):
    copy_image = []
    for i in range(len(image)):
        lst = []
        for j in range(len(image[i])):
            lst.append(image[i][j])
        copy_image.append(lst)
    for i in range(len(image)):
        for j in range(len(image[i])):
            m = get_k_mat(image, i, j, len(kernel))
            copy_image[i][j] = conv(m, kernel)
    return copy_image


def bilinear_interpolation(image, y, x):
    x1 = floor(x)
    x2 = ceil(x)
    y1 = floor(y)
    y2 = ceil(y)
    if x1 == x2 and y1 == y2:
        return image[round(y)][round(x)]
    a = image[y1][x1]
    b = image[y2][x1]
    c = image[y1][x2]
    d = image[y2][x2]
    wx = x - x1
    wy = y - y1
    return int(round(a * (1 - wx) * (1 - wy) + b * wy * (1 - wx) + c * wx * (1 - wy) + d * wx * wy))


def resize(image, new_height, new_width):
    new_image = [[0 for i in range(new_width)] for j in range(new_height)]
    for i in range(new_height):
        for j in range(new_width):
            y = (i / (new_height - 1)) * (len(image) - 1)
            x = (j / (new_width - 1)) * (len(image[0]) - 1)
            new_image[i][j] = bilinear_interpolation(image, y, x)
    return new_image


def rotate_90(image, direction):
    if direction == "R":
        finallst = []
        for i in range(len(image[0])):
            lst = []
            k = len(image) - 1
            for j in range(len(image)):
                lst.append(image[k][i])
                k -= 1
            finallst.append(lst)
        return finallst
    if direction == "L":
        finallst = []
        for i in range(len(image[0]) - 1, -1, -1):
            lst = []
            for j in range(len(image)):
                lst.append(image[j][i])
            finallst.append(lst)
        return finallst


def get_edges(image, blur_size, block_size, c):
    blured_image = apply_kernel(image, blur_kernel(blur_size))
    threshold = apply_kernel(blured_image, blur_kernel(block_size))
    newimage = deepcopy(threshold)
    for i in range(len(blured_image)):
        for j in range(len(blured_image[0])):
            if threshold[i][j] - c < blured_image[i][j]:
                newimage[i][j] = 255
            else:
                newimage[i][j] = 0
    return newimage


def quantize(image, N):
    result = []
    for i in range(len(image)):
        lst = []
        for j in range(len(image[i])):
            lst.append(round(floor(image[i][j] * (N / 255)) * 255 / N))
        result.append(lst)
    return result


def quantize_colored_image(image, N):
    channels = separate_channels(image)
    new_channels = []
    for i in range(len(channels)):
        new_c = quantize(channels[i], N)
        new_channels.append(new_c)
    return combine_channels(new_channels)


def add_mask(image1, image2, mask):
    if type(image1[0][0]) is int:
        finalim = []
        for i in range(len(image1)):
            image = []
            for j in range(len(image1[0])):
                lst = round(image1[i][j] * mask[i][j] + image2[i][j] * (1 - mask[i][j]))
                image.append(lst)
            finalim.append(image)
        return finalim

    image1 = separate_channels(image1)
    image2 = separate_channels(image2)
    image = []
    for i in range(len(image1[0])):
        sechelp = []
        for j in range(len(image1[0][0])):
            helplst = []
            for k in range(len(image1)):
                lst = round(image1[k][i][j] * mask[i][j] + image2[k][i][j] * (1 - mask[i][j]))
                helplst.append(lst)
            sechelp.append(helplst)
        image.append(sechelp)
    return image


def cartoonify(image, blur_size, th_block_size, th_c, quant_num_shades):
    BW = RGB2grayscale(image)
    egBW = get_edges(BW, blur_size, th_block_size, th_c)
    quim = quantize_colored_image(image, quant_num_shades)
    lsm = []
    mask_01 = copy.deepcopy(egBW)
    for i in range(len(egBW)):
        for j in range(len(egBW[i])):
            if egBW[i][j] == 255:
                mask_01[i][j] = 1
    lsm.append(egBW)
    lstcom = combine_channels(lsm * 3)
    return add_mask(quim, lstcom, mask_01)


if __name__ == '__main__':
    if len(sys.argv) != 8:
        print("the number of args not correct!")
    else:
        image_s = sys.argv[1]
        cartoon_dest = sys.argv[2]
        max_im_size = int(sys.argv[3])
        blur_size = int(sys.argv[4])
        th_block_size = int(sys.argv[5])
        th_c = int(sys.argv[6])
        quant_num_shades = int(sys.argv[7])
        image = load_image(image_s)
        width = len(image[0][0])
        height = len(image[0])
        sizeim = width * height
        if height>max_im_size or width>max_im_size:
            sep = separate_channels(image)
            for i in range(3):
                sep[i] = resize(sep[i], max_im_size, max_im_size)
            image= combine_channels(sep)
        im=cartoonify(image,blur_size,th_block_size,th_c,quant_num_shades)
        save_image(im,cartoon_dest)

