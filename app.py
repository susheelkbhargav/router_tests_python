import subprocess as cmd
import logging
import xml.etree.ElementTree as ET


logging.basicConfig(filename='example.log', level= logging.DEBUG)
logging.info('Started Tests')


tree= ET.parse('tests.xml')
root= tree.getroot()

print "list of options:"

list_of_options= ["all", "ip forwarding", "interface state check", "ping"]
for options in list_of_options:
    print options

choice = raw_input("choose an option:")
logging.info(choice)

if choice.strip()== "all":
    for child in root:
        print "Executing test:"+ child[0].text
        logging.info("Executing test:"+ child[0].text)
        arguments= child[1].text.split()
        result= cmd.check_output(arguments)
        print child[2].text
            if str(result.strip())is str(child[2].text):
                print "Test"+ child[0].text+"passed"
                logging.info("Test"+ child[0].text+"passed")
            else:
                logging.warning("Test"+ child[0].text+ "failed. expected:"+ str(child[2].text)+"got :"+str(result).strip())

    print "Execution complete"
    logging.info("Execution complete")

else:
    for child in root:
        if str(child.attrib==choice):
            print "Executing test:"+ child[0].text
            logging.info("Executing test:"+ child[0].text)
            arguments= child[1].text.split()
            result= cmd.check_output(arguments)
            print child[2].text
                if str(result.strip())is str(child[2].text):
                    print "Test"+ child[0].text+"passed"
                    logging.info("Test"+ child[0].text+"passed")
                else:
                    print "Test"+ child[0].text+ "failed. expected:"+
                             child[2].text 
                    logging.warning("Test"+ child[0].text+ "failed. expected:"+
                             child[2].text)

