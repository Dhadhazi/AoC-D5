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


highest_boarding_id = 0

for line in data:
    seat = seat_decoder(line)
    seat_id = seat["row"] * 8 + seat["column"]
    if seat_id > highest_boarding_id:
        highest_boarding_id = seat_id

print(f"Highest boarding id: {highest_boarding_id}")
