

def check_hits(velocity, target):

    step = 0
    height = 0
    while True:
        height += max(velocity, 0)
        step += 1
        target = [y - velocity for y in target]
        velocity -= 1

        if 0 in target:
            return "hit", step, height
        elif min(target) > 0:
            return "miss", step, height

        continue

target_y = list(range(-90,-56,1))
target_x = list(range(240,293,1))

print(check_hits(velocity=89,target=target_y))

def check_hits_x_y(velocity_x, target_x, velocity_y, target_y):

    while True:
        target_y = [y - velocity_y for y in target_y]
        velocity_y -= 1

        target_x = [y - velocity_x for y in target_x]
        velocity_x = max(0, velocity_x - 1)

        if (0 in target_x) and (0 in target_y):
            return "hit"
        elif (min(target_y) > 0) or (max(target_x) < 0):
            return "miss"

        continue


target_y = list(range(-90,-56,1))
target_x = list(range(240,293,1))
success_counter = 0

# calc x velocities
for i in range(294):
    for j in range(-90, 90):

        test_hit = check_hits_x_y(velocity_x=i, target_x=target_x,velocity_y=j, target_y=target_y)
        if test_hit == "hit":
            success_counter += 1

print(success_counter)
