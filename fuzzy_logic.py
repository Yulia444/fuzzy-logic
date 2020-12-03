
def Q(arguments):
    area = arguments['area']
    ceiling = arguments['ceiling']
    insolation = arguments['insolation']
    number_of_people = arguments['number_of_people']
    number_of_computers = arguments['number_of_computers']
    is_highest_floor = arguments['is_highest_floor']
    glazing_area = arguments['glazing_area']

    q1 = Q1(area, ceiling, insolation, glazing_area, is_highest_floor)
    q2 = Q2(number_of_people)
    q3 = Q3(number_of_computers)
    q = q1 + q2 + q3
    return q


def Q1(area, ceiling, insolation, 
       glazing_area, is_highest_floor):
    q1 = area * ceiling
    if insolation == 'Слабка':
        q1 *= 30 / 1000
        if glazing_area > 2:
            q1 += 0.1
    elif insolation == 'Середня':
        q1 *= 35 / 1000
        if glazing_area > 2:
            q1 += 0.2
    elif insolation == 'Сильна':
        q1 *= 40 / 1000
        if glazing_area > 2:
            q1 += 0.3
    if is_highest_floor:
        q1 += q1 * 0.15
    return q1


def Q2(number_of_people):
    return number_of_people * 0.15


def Q3(number_of_computers):
    return number_of_computers * 0.3
 

def m_temperature_low(temperature):
    if temperature <= 18:
        return 1
    elif temperature >= 22:
        return 0
    elif 18 <= temperature <= 22:
        return (22 - temperature) / 4


def m_temperature_high(temperature):
    if temperature >= 22:
        return 1
    elif temperature <= 18:
        return 0
    elif 18 <= temperature <= 22:
        return 1 - (22 - temperature) / 4
    


def m_temperature_middle(temperature):
    if 18 <= temperature <= 22:
        return 1
    elif temperature <= 18:
        return 1 - (18 - temperature) / 4
    elif temperature >= 22:
        return 1 + (22 - temperature) / 4


def temp_is_low(temperature):
    return temperature < 18


def temp_is_optional(temperature):
    return 18 <= temperature <= 22


def temp_is_high(temperature):
    return temperature > 22


def OR(A, B):
    return min([A, B])


def AND(A, B):
    return max([A, B])


def NOT(A):
    return 1 - A


def temp_difference_high(current, output):
    return current - output > 6


def temp_difference_middle(current, output):
    return 6 >= current-output >= 3


def temp_difference_low(current, output):
    return current - output < 3


def temperature_difference_high(difference):
    if difference >= 6:
        return 1
    elif 6 >= difference >= 3:
        return 1 - (6 - difference) / 4
    elif difference <= 3:
        return 0

def temperature_difference_low(difference):
    if difference >= 6:
        return 0
    elif 3 <= difference <= 6:
        return (6 - difference) / 3
    else:
        return 1

def temperature_difference_middle(difference):
    if difference >= 6:
        return 1 - (difference - 6) / 4
    elif 6 >= difference >= 3:
        return 1
    else:
        return 1 - (3 - difference) / 4 

