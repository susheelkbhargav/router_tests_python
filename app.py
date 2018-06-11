import subprocess as cmd
import logging
import xml.etree.ElementTree as ET

logging.basicConfig(filename='output.log', level= logging.DEBUG)
logging.info('Started Tests')


tree= ET.parse('tests.xml')
root= tree.getroot()

def log_and_print_execution(arguments):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Executing test: "+ arguments)
    print "Executing test:"+ arguments

def log_and_print_result_passed(arguments1):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Test"+ arguments1+"passed")
    print "Test"+ arguments1+"passed"

def log_and_print_no_output_fail(arguments1):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Test"+ arguments1+"failed as command gave no output")
    print "Test"+ arguments1+"failed as command gave no output"

def log_and_print_fail_expected(arguments1,arguments2, arguments3):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Test"+ arguments1+ " failed. expected: "+ arguments2+" got : "+ arguments3)
    print "Test"+ arguments1+ " failed. expected: "+ arguments2+" got : "+ arguments3

def log_and_print_skipped(arguments1):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Test"+ arguments1+"skipped")
    print "Test"+ arguments1+"skipped"


def create_map(child):
    test_data = dict()
    for field in child:
        test_data[field.tag] = field.text
    return test_data
    
for child in root:
    test_data = create_map(child)
    print "Executing test:"+ test_data['name']
    if child.attrib['run_test'] == "yes":
        logging.info("Executing test:"+ test_data['name'])
        arguments = test_data['command'].split()
        result = str(cmd.check_output(arguments)).strip()
        if 'not_empty' in child.attrib:
            if result:
                log_and_print_result_passed(test_data['name'])
            else:
                log_and_print_no_output_fail(test_data['name'])
        else:
            if result == str(test_data['expected_result']):
                log_and_print_result_passed(test_data['name'])
               
            else:
                log_and_print_fail_expected(test_data['name'], str(test_data['expected_result']),str(result).strip())
    else:
        log_and_print_skipped(test_data['name'])

print "Execution complete"
