from core_calculations import *
a=(740632.3316,3743139.219)
b=(740633.1485,3743139.087)

dst = get_distance_between_two_consecutive_images(a,b)
print(('{} meters').format(dst))