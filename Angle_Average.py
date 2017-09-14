import math

# helper_functions
def to_rad(angle):
    return angle*math.pi/180.0

def to_deg(angle):
    return angle*180.0/math.pi

# this list is a numpy array
def average_angle(list_angles, angle_type = 'deg'):
    if len(list_angles)<1:
        return 'undefined'
    if len(list_angles)<2:
        return list_angles[0]
    if angle_type == 'deg':
        for i in range(len(list_angles)):
            list_angles[i] = to_rad(list_angles[i])

    # everything is in rads from now on
    # correct angles with respect to the reference angle
    ref_angle = list_angles[0] % math.pi # normalise if necessary
    x_sum = math.cos(ref_angle)
    y_sum = math.sin(ref_angle)
    for i in range(1,len(list_angles)):
        list_angles[i] = list_angles[i] % math.pi # normalise if necessary
        if abs(list_angles[i] - ref_angle) > (math.pi/2.0):
            list_angles[i] = (list_angles[i] + math.pi) % (2.0*math.pi)
        x_sum = x_sum + math.cos(list_angles[i])
        y_sum = y_sum + math.sin(list_angles[i])

    if angle_type == 'deg':
        return to_deg(math.atan2(y_sum,x_sum)) % 180.0
    else:
        return math.atan2(y_sum,x_sum) % math.pi

def assert_similar(num1,num2,tol):
    assert(num1>(num2-tol))
    assert(num1<(num2+tol))

# TESTS SUITE
tol = 1
tol = 1 # 1 degree tolerance

# equivalences:
# 25 = 205
# 50 = 230
# 155 = 335
assert_similar (average_angle([25,   50, 155],'deg'), 16.7, tol)
assert_similar (average_angle([50,  155, 205],'deg'), 16.7, tol)
assert_similar (average_angle([155, 205, 230],'deg'), 16.7, tol)
assert_similar (average_angle([205, 230, 335],'deg'), 16.7, tol)
assert_similar (average_angle([230, 335,  25],'deg'), 16.7, tol)
assert_similar (average_angle([335,  25,  50],'deg'), 16.7, tol)

# 25 = 205
assert_similar (average_angle([205,   50, 155],'deg'), 16.7, tol)
assert_similar (average_angle([50,  155, 25],'deg'), 16.7, tol)
assert_similar (average_angle([155, 25, 230],'deg'), 16.7, tol)
assert_similar (average_angle([25, 230, 335],'deg'), 16.7, tol)
assert_similar (average_angle([230, 335,  205],'deg'), 16.7, tol)
assert_similar (average_angle([335,  205,  50],'deg'), 16.7, tol)

# 50 = 230
assert_similar (average_angle([25,   230, 155],'deg'), 16.7, tol)
assert_similar (average_angle([230,  155, 205],'deg'), 16.7, tol)
assert_similar (average_angle([155, 205, 50],'deg'), 16.7, tol)
assert_similar (average_angle([205, 50, 335],'deg'), 16.7, tol)
assert_similar (average_angle([50, 335,  25],'deg'), 16.7, tol)
assert_similar (average_angle([335,  25,  230],'deg'), 16.7, tol)

# 155 = 335
assert_similar (average_angle([25,   50, 335],'deg'), 16.7, tol)
assert_similar (average_angle([50,  335, 205],'deg'), 16.7, tol)
assert_similar (average_angle([335, 205, 230],'deg'), 16.7, tol)
assert_similar (average_angle([205, 230, 155],'deg'), 16.7, tol)
assert_similar (average_angle([230, 155,  25],'deg'), 16.7, tol)
assert_similar (average_angle([155,  25,  50],'deg'), 16.7, tol)

# Test negative numbers:
#25 = 205 = -335
assert_similar (average_angle([-335,   50, 155],'deg'), 16.7, tol)
assert_similar (average_angle([50,  155, -335],'deg'), 16.7, tol)
assert_similar (average_angle([155, -335, 230],'deg'), 16.7, tol)
assert_similar (average_angle([-335, 230, 335],'deg'), 16.7, tol)
assert_similar (average_angle([230, 335,  -335],'deg'), 16.7, tol)
assert_similar (average_angle([335,  -335,  50],'deg'), 16.7, tol)

# 50 = 230 = -130
assert_similar (average_angle([25,   -130, 155],'deg'), 16.7, tol)
assert_similar (average_angle([-130,  155, 205],'deg'), 16.7, tol)
assert_similar (average_angle([155, 205, -130],'deg'), 16.7, tol)
assert_similar (average_angle([205, -130, 335],'deg'), 16.7, tol)
assert_similar (average_angle([-130, 335,  25],'deg'), 16.7, tol)
assert_similar (average_angle([335,  25,  -130],'deg'), 16.7, tol)

# 335 = 155 = -25
assert_similar (average_angle([25,   50, -25],'deg'), 16.7, tol)
assert_similar (average_angle([50,  -25, 205],'deg'), 16.7, tol)
assert_similar (average_angle([-25, 205, 230],'deg'), 16.7, tol)
assert_similar (average_angle([205, 230, -25],'deg'), 16.7, tol)
assert_similar (average_angle([230, -25,  25],'deg'), 16.7, tol)
assert_similar (average_angle([-25,  25,  50],'deg'), 16.7, tol)

# additional tests
assert_similar (average_angle([70,  -80],'deg'), 85, tol)
assert_similar (average_angle([-80,  70],'deg'), 85, tol)
assert_similar (average_angle([10,20,350]),6.6666,tol)
assert_similar (average_angle([10,20,180,180,340]),2.0,tol)
assert_similar (average_angle([15,355,25,-15]),5.0,tol)
print ("All tests passed!")

# example
list_angles = [15,175,25,-15]
print("Example: average_angle (15,175,25,-15) = ",average_angle(list_angles))
