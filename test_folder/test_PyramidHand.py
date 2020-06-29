from src.PyramidHand import PyramidHand

pyr_hand = [[] for i in range(7)]
pyr_hand[0] = [' ']
pyr_hand[1] = ['SA+']
pyr_hand[2] = ['SQ+', 'DQ+', 'HQ+']
pyr_hand[3] = ['SK+', 'DK+', 'HK+']
pyr_hand[4] = ['SA+', 'DA+', 'HA+']
pyr_hand[5] = ['ST+', 'S9+', 'S7+', 'S5+', 'S3+']
pyr_hand[6] = ['CJ+', 'C9+', 'C7+', 'C5+', 'C3+']
pyramid = PyramidHand(pyr_hand)
print("\n", pyramid.pyramid_compact[1:7])
print ("Is Pyramid Hand Valid?", pyramid.is_valid()[0], ",", pyramid.is_valid()[1])

pyr_hand[0] = [' ']
pyr_hand[1] = ['SA+']
pyr_hand[2] = ['SQ+', 'DQ+']
pyr_hand[3] = ['SK+', 'DK+', 'HK+']
pyr_hand[4] = ['SA+', 'DA+', 'HA+']
pyr_hand[5] = ['ST+', 'S9+', 'S7+', 'S5+', 'S3+']
pyr_hand[6] = ['CJ+', 'C9+', 'C7+', 'C5+', 'C3+']
pyramid = PyramidHand(pyr_hand)
print("\n", pyramid.pyramid_compact[1:7])
print ("Is Pyramid Hand Valid?", pyramid.is_valid()[0], ",", pyramid.is_valid()[1])

pyr_hand[0] = []
pyr_hand[1] = ['SA+']
pyr_hand[3] = ['SQ+', 'DQ+', 'CQ+']
pyr_hand[2] = ['SK+', 'DK+', 'HK+']
pyr_hand[4] = ['SA+', 'DA+', 'HA+']
pyr_hand[5] = ['ST+', 'S9+', 'S7+', 'S5+', 'S3+']
pyr_hand[6] = ['CJ+', 'C9+', 'C7+', 'C5+', 'C3+']
pyramid = PyramidHand(pyr_hand)
print("\n", pyramid.pyramid_compact[1:7])
print ("Is Pyramid Hand Valid?", pyramid.is_valid()[0], ",", pyramid.is_valid()[1])