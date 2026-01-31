import math


def mutual_information(joint: list[list[float]]) -> float:
    px = [sum(row) for row in joint]
    py = [sum(joint[i][j] for i in range(len(joint))) for j in range(len(joint[0]))]
    mi = 0.0
    for i in range(len(joint)):
        for j in range(len(joint[0])):
            pxy = joint[i][j]
            if pxy > 0 and px[i] > 0 and py[j] > 0:
                mi += pxy * math.log(pxy / (px[i] * py[j]))
    return mi
