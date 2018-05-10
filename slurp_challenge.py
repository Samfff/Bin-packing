'''

So basically there are a few options, let's first go through of what we actually want to accomplish:
- We want to minimize the amount of boxes used for the orders
- We want to fit every single order into the boxes (duh)

What can we do:
- We can twist the ordered bags in direction (x,y,z) - difficult to implement
- We can always take a new box without having to fill up the last one - indeed
- We can fit the bags into the boxes in any order we'd like - fuck yeah

The Algorithm (Alpha):
1) Put an item into the box that it first fits into, 
if it does not fit into the box, open a new one 
 (I found this very intuitive, let's see if it is efficient in any way)
 (Too bad there is no comparison algorithm to race against)
2) Always pick the biggest item left out into the pile
3) This way, the probability of space being left out for smaller one increases

What do we need functions for? 

1)Of course some kind of class for the items and the box.
It would take 4 parameters

2) Something to calculate is there space

3) Something to reduce the added item volume from the box volume
'''


class Bin_pack(small_bag, medium_bag, large_bag, box_side):

	box_dimensions = [box_side, box_side, box_side] #length, width, height
	# box_volume = box_side * box_side * box_side
	SMALL_DIMENSION = [16,23,2]
	MEDIUM_DIMENSION = [22,26,2]
	LARGE_DIMENSION = [14,26,10]
	item_list = large_bag * [LARGE_DIMENSION] + medium_bag * [MEDIUM_DIMENSION] + small_bag * [SMALL_DIMENSION]
	# Starting with one open 
	boxes_open = [box_dimensions]
	# Here is the function that checks if there is space, if yes, it returns true
	# We always try to find space starting from the bottom of the box, as close to
	# point (0,0,0) as we can get
	# If the Dimensions are smaller or equal to the ones of the box in the current coordinates
	# Then the bag will fit
	# the only thing we need it the height because if 

	# Box dimensions should be though as the volume of the box that is left

	def find_space(bag_dimensions):
		height = 0
		while (height + bag_dimensions[2]) <= box_dimensions[2]:
			if ((box_dimensions[0] >= bag_dimensions[0]) and
			(box_dimensions[1] >= bag_dimensions[1])):
				return True
		# if the bag doesn't fit right away, we move it by the height of the bag
			else:
				height += bag_dimensions[2]
		return False

	# If there is space for the bag, we place it into the box, thereby the box dimensions are changed
	def change_box_dimensions(box_dimensions, bag_dimensions):
		box_dimensions = map(lambda x,y: x-y, box_dimensions, bag_dimensions)

	def delete_bag_from_items(bag_dimensions):
		del item_list[0]

	def open_new_box:
		boxes_open.append([box_side, box_side, box_side])

	# This function tries to find space and if it does, then it places it inside the box,
	# If there is no space, then the function opens a new box and tries again,
	# until space is found. After this we change the box dimensions and delete the bag from 
	# original items list.
	# 

	def fit_bags(box):
		#for bag in item_list:
		if find_space(bag) = True:
			change_box_dimensions(box_dimensions, bag)
		elif find_space(bag) = False:
			open_new_box()





























