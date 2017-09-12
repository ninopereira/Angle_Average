import math

# helper_functions
def to_rad(angle):
    return angle*math.pi/180.0

def to_deg(angle):
    return angle*180.0/math.pi

# this list is a numpy array
def average_angle(list_angles, angle_type = 'deg'):

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

# TEST average_angle
tol = 0.1
assert_similar (average_angle([10,20,350]),6.6666,tol)
assert_similar (average_angle([10,20,180,180,340]),2.0,tol)
assert_similar (average_angle([15,355,25,-15]),5.0,tol)
print ("All tests passed!")

# example
list_angles = [15,175,25,-15]
print("average_angle (15,175,25,-15) = ",average_angle(list_angles))