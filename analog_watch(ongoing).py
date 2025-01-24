# Analog watch
# It alarms when sec is collabsed with min, hour.

# 0 <= h1, h2 <= 23
# 0 <= m1, m2 <= 59
# 0 <= s1, s2 <= 59


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    loc_h1 = (h1 + (1 / 60) * m1 + (1 / 3600) * s1) * 5
    loc_m1 = m1 + (1 / 60) * s1
    loc_s1 = s1
    diff_s = h2 * 3600 + m2 * 60 + s2 - (h1 * 3600 + m1 * 60 + s1)
    loc_h2 = (h2 + (1 / 60) * m2 + (1 / 3600) * s2) * 5
    loc_m2 = m2 + (1 / 60) * s2
    loc_s2 = s2
    print("diff_sec", diff_s, "into h:", diff_s / 3600)
    print("h1", loc_h1, "m1", loc_m1, "s1", loc_s1)
    print("h2", loc_h2, "m2", loc_m2, "s2", loc_s2)

    if loc_h1 >= 60:
        loc_h1 -= 60
    if loc_h2 >= 60:
        loc_h2 -= 60

    if diff_s / 60 >= 1:
        answer += int(diff_s / 60) * 2
        # if :
        #     answer -= 1
        diff_s = (diff_s / 60 - int(diff_s / 60)) * 60
        loc_h1 = loc_h2 - 1 / 12
        loc_m1 = loc_m2 - 1

    else:
        if loc_s1 == loc_h1 or loc_s1 == loc_m1:
            answer += 1

    if loc_h1 - loc_s1 < 0:
        shifted_h = 60 - loc_s1 + loc_h1
    else:
        shifted_h = loc_h1 - loc_s1
    if loc_m1 - loc_s1 < 0:
        shifted_m = 60 - loc_s1 + loc_m1
    else:
        shifted_m = loc_m1 - loc_s1
    print("h1", loc_h1, "m1", loc_m1, "s1", loc_s1)
    # print('h2', loc_h2, 'm2', loc_m2, 's2', loc_s2)
    if loc_s2 == loc_h2 and loc_s2 == loc_m2:
        answer += 1
        print("sametime")
    else:
        if loc_s1 != loc_h1:
            if diff_s >= shifted_h:
                answer += 1
                print("passing h", diff_s, shifted_h)
        if loc_s1 != loc_m1:
            if diff_s >= shifted_m:
                answer += 1
                print("passing m", diff_s, shifted_m)

    return answer


# print(solution(0,5,30,0,7,0))
# print(solution(12,0,0,12,0,30))
# print(solution(0,6,1,0,6,6))
# print(solution(11,59,30,12,0,0))
# print(solution(11,58,59,11,59,0))
# print(solution(1,5,5,1,5,6))
print(solution(0, 0, 0, 23, 59, 59))  ## should be 2852
