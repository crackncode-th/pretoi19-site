import csv
import codecs

# anon_list = [7, 26, 28, 34, 44, 45, 47, 54, 55, 63, 66, 67, 72, 76, 79, 84, 92, 94, 97, 101, 104, 110, 112, 116, 117, 120, 121, 122, 126, 127, 128, 129]

data = dict()

def addData(fileName, key, idx, total):
    with open(fileName, newline="", encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == 'Username':
                continue

            username = row[0]

            '''
            if int(username.split('user_')[1]) not in anon_list:
                data[username]['name'] = row[1].strip()
            else:
                data[username]['name'] = ""
            '''

            data[username]['name'] = row[1].strip()

            for x in range(0, 3):
                value = int(float(row[idx[x]]))
                data[username][key[x]] = value
                data[username][total] += value
                data[username]['total'] += value


for i in range(1, 129 + 1):
    new_row = dict()
    username = "user_" + str(i).zfill(3)
    new_row['username'] = username
    new_row['name'] = ""
    new_row['wordbuilder'] = 0
    new_row['busan'] = 0
    new_row['mineral'] = 0
    new_row['mangoes'] = 0
    new_row['oranges'] = 0
    new_row['tourist'] = 0
    new_row['day 1'] = 0
    new_row['day 2'] = 0
    new_row['total'] = 0
    new_row['rank'] = 0
    data[username] = new_row

addData('ranking_day1.csv', ['wordbuilder', 'busan', 'mineral'], [2, 4, 6], "day 1")
addData('ranking_day2.csv', ['mangoes', 'oranges', 'tourist'], [2, 4, 6], "day 2")

scores = dict()

for username in data.keys():
    if data[username]['total'] in scores.keys():
        scores[data[username]['total']].append(username)
    else:
        scores[data[username]['total']] = [username]

all_scores = list()

for username in data.keys():
    all_scores.append(data[username]['total'])

all_scores = list(set(all_scores))
sorted_scores = sorted(all_scores)[::-1]

rank = 1
cnt = 0

key_list = ['wordbuilder', 'busan', 'mineral', 'mangoes', 'oranges', 'tourist']

with codecs.open('data.json', 'w', 'utf-8-sig') as f:
    f.write('[\n')
    for x in sorted_scores:
        for username in scores[x]:
            cnt += 1
            data[username]['rank'] = rank
            f.write('\t{\n')
            f.write('\t\t"Username": "{}",\n'.format(username))
            for key in key_list:
                f.write('\t\t"{}": {},\n'.format(key, data[username][key]))
            f.write('\t\t"Day 1": {},\n'.format(data[username]['day 1']))
            f.write('\t\t"Day 2": {},\n'.format(data[username]['day 2']))
            f.write('\t\t"Name": "{}",\n'.format(data[username]['name']))
            f.write('\t\t"Rank": {}\n'.format(data[username]['rank']))
            if cnt < 129:
                f.write('\t},\n')
            else:
                f.write('\t}\n')
        rank += len(scores[x])
    f.write(']')
