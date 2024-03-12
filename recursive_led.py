from pprint import pprint

'''
'digit number' = 'led required'.
total_led = [1,1,1,1,1,1,1]
0 = [1,1,1,1,1,1,0]
1 = [0,1,1,0,0,0,0]
2 = [1,1,0,1,1,0,1]
3 = [1,1,1,1,0,0,1]
4 = [0,1,1,0,0,1,1]
5 = [1,0,1,1,0,1,1]
6 = [1,0,1,1,1,1,1]
7 = [1,1,1,0,0,0,0]
8 = [1,1,1,1,1,1,1]
9 = [1,1,1,0,0,1,1]

Q. There are switches can light on connected leds.
 For a sequential number as input, you gonna activate switchs.
 When you input a list which has sequence numbers as elements,
 find a list which has least switch numbers to activate as elements.
'''

ip_list = ['381', '92']

def recursive(tensor, overlapped):
    pprint(tensor)
    zipped = [[list(i) for i in zip(*batch) if (0 in i and 1 in i)] for batch in tensor]
    unzipped = [[list(i) for i in zip(*batch) if 1 in i] for batch in zipped]
    unzipped = [[[]] if len(batch) == 0 else batch for batch in unzipped ]
    overlapped_new = [1 if len(batch[0]) < len(tensor[i][0]) else 0 for i, batch in enumerate(unzipped)]
    print('overlap+:', overlapped_new)
    overlapped_new = [sum(i) for i in zip(overlapped, overlapped_new)]
    print('overl_total:', overlapped_new)
    if sum(overlapped_new) > sum(overlapped):
        return recursive(unzipped, overlapped_new)
    else:
        remain = [len(batch) if batch[0] != [] else 0 for batch in unzipped]
        print('non_overl_remain:', remain)
        return [sum(i) for i in zip(overlapped_new, remain)]

def solution(ip):
    led_dict = {0 : [1,1,1,1,1,1,0],
                1 : [0,1,1,0,0,0,0],
                2 : [1,1,0,1,1,0,1],
                3 : [1,1,1,1,0,0,1],
                4 : [0,1,1,0,0,1,1],
                5 : [1,0,1,1,0,1,1],
                6 : [1,0,1,1,1,1,1],
                7 : [1,1,1,0,0,0,0],
                8 : [1,1,1,1,1,1,1],
                9 : [1,1,1,0,0,1,1]
                }
    encoded_list = [[led_dict[int(seq)] for seq in batch] for batch in ip]
    answer = [0 for _ in encoded_list]
    answer = recursive(encoded_list, answer)
    return answer

print(solution(ip_list))
