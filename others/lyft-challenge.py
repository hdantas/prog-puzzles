# Programming Challenge (Optional)

# Calculate the detour distance between two different rides.
# Given four latitude / longitude pairs, where driver one is traveling
# from point A to point B and driver two is traveling from point C to point D,
# write a function (in your language of choice) to calculate the shorter of the
# detour distances the drivers would need to take to pick-up and drop-off the other driver.

import math

def distance_points(coord1, coord2, *arg):
	# Calculates the distance between coordinates according to the Spherical Law of Cosines in km
	# src: http://www.movable-type.co.uk/scripts/latlong.html

	if len(arg) > 0:
		return distance_points(coord2, arg[0], *(arg[1:])) + distance_points(coord1, coord2)
	
	(phi1, phi2) = (math.radians(coord1[0]), math.radians(coord2[0]))
	delta_lambda = math.radians(coord2[1] - coord1[1])
	R = 6371 # earth's radius in km
	return math.acos(math.sin(phi1) * math.sin(phi2) + math.cos(phi1) * math.cos(phi2) * math.cos(delta_lambda)) * R;


def shorter_detour(A, B, C, D):
	detour1 = distance_points(A, C, D, B) - distance_points(A, B) # driver 1: A -> B, w/ detour: A -> C -> D -> B
	detour2 = distance_points(C, A, B, D) - distance_points(C, D) # driver 2: C -> D, w/ detour: C -> A -> B -> D
	return min(detour1, detour2)
