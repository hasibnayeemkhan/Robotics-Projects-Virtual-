from controller import Robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

time_step = 64
max_speed = 7
#motor
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)


#IR sensor
right_ir = robot.getDevice('RIGHT')
right_ir.enable(time_step)
mid_ir = robot.getDevice('MID')
mid_ir.enable(time_step)
left_ir = robot.getDevice('LEFT')
left_ir.enable(time_step)


#simulation 
#main loop:
while robot.step(time_step) != -1:
    right_ir_val = right_ir.getValue()
    mid_ir_val = mid_ir.getValue()
    left_ir_val = left_ir.getValue()
    print("left: {} mid: {} right: {}".format(left_ir_val, mid_ir_val, right_ir_val))
    
    left_speed = max_speed
    right_speed = max_speed
    #Process sensor data
    if left_ir_val<600 and right_ir_val<600 and mid_ir_val>=600:
    	left_motor.setVelocity(left_speed)
    	right_motor.setVelocity(right_speed)
    if left_ir_val<600 and right_ir_val>=600 and mid_ir_val>=600:
    	left_motor.setVelocity(left_speed)
    	right_motor.setVelocity(0)
    if left_ir_val>=600 and right_ir_val<600 and mid_ir_val>=600:
    	left_motor.setVelocity(0)
    	right_motor.setVelocity(right_speed)
    if left_ir_val>=600 and right_ir_val<600 and mid_ir_val<600:
    	left_motor.setVelocity(0)
    	right_motor.setVelocity(right_speed)
    if left_ir_val<600 and right_ir_val>=600 and mid_ir_val<600:
    	left_motor.setVelocity(left_speed)
    	right_motor.setVelocity(0)
    if left_ir_val<600 and right_ir_val<600 and mid_ir_val<600:
    	left_motor.setVelocity(left_speed)
    	right_motor.setVelocity(right_speed)
    pass