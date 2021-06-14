from collections import deque
def solution(bridge_length, weight, truck_weights):

    truck_weights = deque(truck_weights)
    crossing_truck = deque([0]*bridge_length)
    time = 0

    while(crossing_truck):
        time += 1
        crossing_truck.popleft()
        if truck_weights:
            if (sum(crossing_truck) + truck_weights[0]) <= weight:
                crossing_truck.append(truck_weights.popleft())
            else:
                crossing_truck.append(0)



    return time

solution(2, 10, [7,4,5,6])