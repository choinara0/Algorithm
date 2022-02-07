import math

def minute(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

def solution(fees, records):
    answer = []

    dic = dict()
    for record in records:
        time, car_num, check = record.split()
        car_num = int(car_num)
        if car_num in dic:
            dic[car_num].append([minute(time), check])
        else:
            dic[car_num] = [[minute(time), check]]

    rList = list(dic.items())
    rList.sort(key=lambda x : x[0])

    for r in rList:
        t = 0
        for rr in r[1]:
            if rr[1] == 'IN':
                t -= rr[0]
            else:
                t += rr[0]

        if r[1][-1][1] == 'IN':
            t += minute('23:59')

        if t < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil(((t - fees[0]) / fees[2]))) * fees[3])

    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
solution([1, 461, 1, 10], ["00:00 1234 IN"])
#[14600, 34400, 5000]
#[0, 591]
#[14841]
