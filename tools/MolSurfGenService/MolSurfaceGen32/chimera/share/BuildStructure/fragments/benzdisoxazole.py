from BuildStructure.Fragment import Fragment, RING65
frag = Fragment("benz[d]isoxazole", [
	("C", (-1.31483, -4.0696, -2.72952)),
	("H", (-2.13217, -3.35057, -2.72924)),
	("C", (0.00965977, -3.60631, -2.72996)),
	("H", (0.221905, -2.54143, -2.73007)),
	("C", (1.04447, -4.55527, -2.73015)),
	("C", (2.45387, -4.55527, -2.73015)),
	("H", (3.13006, -3.71272, -2.73008)),
	("N", (2.96518, -5.79038, -2.7303)),
	("O", (1.86515, -6.64008, -2.7303)),
	("C", (0.721891, -5.90107, -2.73011)),
	("C", (-0.579955, -6.39475, -2.72989)),
	("H", (-0.783554, -7.45847, -2.72999)),
	("C", (-1.60246, -5.43901, -2.72945)),
	("H", (-2.64003, -5.76841, -2.72908)),
	], [
	((0,1), None),
	((0,2), None),
	((2,3), None),
	((4,2), (-0.28687, -4.99434, -2.72985)),
	((4,5), None),
	((5,6), None),
	((5,7), (1.81011, -5.48841, -2.7302)),
	((7,8), None),
	((9,8), None),
	((10,9), (-0.28687, -4.99434, -2.72985)),
	((10,11), None),
	((12,10), None),
	((12,13), None),
	((0,12), (-0.28687, -4.99434, -2.72985)),
	((9,4), None),
	])

fragInfo = [RING65, frag]