import math

with open("input.txt") as file:
    data = file.read().splitlines()


def decoder(code, min=0, max=127):
    if len(code) == 0 or min == max:
        return min
    if code[0] == "F" or code[0] == "L":
        return decoder(code[1:], min, math.floor(max-(max-min)/2))
    if code[0] == "B" or code[0] == "R":
        return decoder(code[1:], math.ceil(min+(max-min)/2), max)


def seat_decoder(seat_code):
    row = decoder(code=seat_code[:7], max=127)
    column = decoder(code=seat_code[-3:], max=7)
    return {"column": column, "row": row}


def get_seat_id(seat_code):
    row = decoder(code=seat_code[:7], max=127)
    column = decoder(code=seat_code[-3:], max=7)
    return row * 8 + column


highest_boarding_id = 0


for line in data:
    seat_id = get_seat_id(line)
    if seat_id > highest_boarding_id:
        highest_boarding_id = seat_id

print(f"Highest boarding id: {highest_boarding_id}")

#Part two
all_seat_id = []
for line in data:
    all_seat_id.append(get_seat_id(line))

all_seat_id.sort()

for i in range(len(all_seat_id)):
    if all_seat_id[i] + 1 != all_seat_id[i+1]:
        print(f"Your seat ID is: {all_seat_id[i] + 1}")
        break
