input = '108457-562041'
pw_min, pw_max = [int(num) for num in input.split('-')]


def pw_criteria_match(password, match_lambda):
    if len(password) != 6 or any(password[i] > password[i+1] for i in range(5)):
        return False
    groups = [password.count(cnt) for cnt in set(password)]
    return any(match_lambda(group) for group in groups)


partOne = sum(pw_criteria_match(str(pass_num), lambda x: x >= 2)
              for pass_num in range(pw_min, pw_max+1))

partTwo = sum(pw_criteria_match(str(pass_num), lambda x: x == 2)
              for pass_num in range(pw_min, pw_max+1))

print("Part 1: %d" % partOne)
print("Part 2: %d" % partTwo)
