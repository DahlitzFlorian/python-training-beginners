# This is a possible solution for exercise_08.py
given_input = "07:05:45PM"

if given_input[8] == "P":
    if given_input[0] + given_input[1] == "12":
        given_input = (
            given_input[0]
            + given_input[1]
            + given_input[2]
            + given_input[3]
            + given_input[4]
            + given_input[5]
            + given_input[6]
            + given_input[7]
        )
        print(given_input)
    else:
        tmp = int(given_input[0] + given_input[1])
        tmp += 12
        tmp = str(tmp)
        given_input = (
            tmp[0]
            + tmp[1]
            + given_input[2]
            + given_input[3]
            + given_input[4]
            + given_input[5]
            + given_input[6]
            + given_input[7]
        )
        print(given_input)
else:
    if given_input[0] + given_input[1] == "12":
        given_input = (
            "00"
            + given_input[2]
            + given_input[3]
            + given_input[4]
            + given_input[5]
            + given_input[6]
            + given_input[7]
        )
        print(given_input)
    else:
        given_input = (
            given_input[0]
            + given_input[1]
            + given_input[2]
            + given_input[3]
            + given_input[4]
            + given_input[5]
            + given_input[6]
            + given_input[7]
        )
        print(given_input)
