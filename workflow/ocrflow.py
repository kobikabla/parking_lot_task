from utils.ocr_request import ocr_space_file


'''retrieve ocr data from image file and return the text or error details'''
def data_from_licens_plate_from_file(file_name):
    test_file = ocr_space_file(filename=file_name, language='eng')
    if test_file.json()['IsErroredOnProcessing'] == True or (test_file.json()['ParsedResults'][0]['ParsedText'] == ''):
        r = {'result': 'fail', 'content': test_file.json()['ParsedResults'][0]['ErrorDetails']}
        return r
    else:
        r = {'result': 'pass', 'content': test_file.json()['ParsedResults'][0]['ParsedText']}
        return r