from datetime import datetime
import logging

from workflow.ocrflow import data_from_licens_plate_from_file

logging.basicConfig(filename='ruls.log', filemode='w')


def enter_to_parking_ruls(plate_num):
    """turning the response to only numbers ,get the lest two digits and check if the car can enter"""
    num = ''
    for p in plate_num:
        if p.isdigit():
            num = num + p
    lenghe = len(num)
    last_two = num[lenghe - 2:]
    logging.info('license plate last 2 digits - ', last_two)

    '''check acording to the rules'''

    if (last_two == '25') or (last_two == '26'):
        decision = {'plate_num': num, 'enter': True, 'code': 'public', 'last_two': last_two,
                    'time_stamp': datetime.now().strftime("%d/%m/%Y-%H:%M:%S")}
        logging.info('first rule apply: 25,26 last tow digits', last_two)
        return decision
    elif (last_two == '85') or (last_two == '86') or (last_two == '87') or (last_two == '88') or (last_two == '89') or (
            last_two == 00):
        decision = {'plate_num': num, 'enter': False, 'code': 'error no1', 'last_two': last_two,
                    'time_stamp': datetime.now().strftime("%d/%m/%Y-%H:%M:%S")}
        logging.info('second rule apply: 85-99 last tow digits', last_two)
        return decision
    elif (lenghe == 7) and ((num[lenghe - 1] == '0') or (num[lenghe - 1] == '5')):
        decision = {'plate_num': num, 'enter': False, 'code': 'error no2', 'last_two': num[lenghe - 1],
                    'time_stamp': datetime.now().strftime("%d/%m/%Y-%H:%M:%S")}
        logging.info('third rule apply:lenghe=7 and lst digit is 0 or 5 , last tow digits', last_two)
        return decision
    else:
        decision = {'plate_num': num, 'enter': True, 'code': 'not defined', 'last_two': last_two,
                    'time_stamp': datetime.now().strftime("%d/%m/%Y-%H:%M:%S")}
        logging.info('the numbers that are not defined')
        return decision

'''check the plate number from image with the rules'''
def valedate_plate_num(file_name):
    plate_num = data_from_licens_plate_from_file(file_name=file_name)
    if plate_num['result'] == 'pass':
        decision = enter_to_parking_ruls(plate_num['content'])
        return decision
    else:
        return False