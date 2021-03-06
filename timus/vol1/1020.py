#!/usr/bin/env python3

import math

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
'''

def find_distance_between_2_points_in_2D_coordinates(a, b):
    '''
    Find distance between 2 points from their 2d coordinates.
    Function parameters: a, b. They are objects of Point class
    Each parameter is a tuple of 2 numbers having 2 coordinates (x, y)
    '''
    #return math.sqrt( (a.x-b.x)**2 + (a.y-b.y)**2 )
    return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )



def main():
    line = input().split()
    n = int(line[0])
    r = float(line[1])
    points = []
    c = 2 * math.pi * r

    for i in range(n):
        points.append([float(x) for x in input().split()])
    #print(points)

    total_distance = 0
    if n == 1:
        total_distance = c

    elif n == 2:
        distance = find_distance_between_2_points_in_2D_coordinates(points[0], points[1])
        total_distance = 2 * distance + c

    else:
        for i in range(n-1):
            distance = find_distance_between_2_points_in_2D_coordinates(points[i], points[i+1])
            total_distance += distance

        distance = find_distance_between_2_points_in_2D_coordinates(points[0], points[n-1])
        total_distance += distance
        total_distance += c
    #print('{0:.2f}'.format(total_distance))

    #rope_length_at_nails = 2 * math.pi * r / 4 * n
    #total_distance += rope_length_at_nails

    #decimal.getcontext().rounding = 'ROUND_HALF_UP'
    print('{0:.2f}'.format(total_distance))
    #print(round(decimal.Decimal(str(total_distance)), 2))

main()
