from core_calculations import *
a=(732070.662735484,3738153.67527624)
b=(732063.616153953,3738027.00263699)
			

dst = get_distance_between_two_consecutive_images(a,b)
print(('{} meters').format(dst))
