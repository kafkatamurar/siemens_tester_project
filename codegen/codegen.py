#Import libraries
import sys
import json


#Constants
# with multi-line template strings
str_templ1 = '''#include "modules/TestDevice.hpp"
#include "iolink/iolink.hpp"

#define True true
#define False false

DeviceAB::DeviceAB(uint8_t slot):
 Module(slot, "IODevice")
{
 initItems();
 initCollections();
}

DeviceAB::~DeviceAB()
{
}

void DeviceAB::initItems()
{
'''
str_templ2 = '''}
void DeviceAB::initCollections(){
 std::shared_ptr<Iolink> Colection = Iolink::getInstance();
'''
str_templ3 = '''}
'''

# with output filename
filename_output = "output.cpp"



#Parse filename from first argument
filename_input = sys.argv[1]
#Open file
with open(filename_input) as fin:
    #Parse JSON from file
    json_string = json.load(fin)

    #Open output file
    with open(filename_output, 'w') as fout:
        #Write first part in .cpp file
        fout.write(str_templ1)

        #Double iteration in JSON item values
        for collection in json_string:
            for item in json_string[collection]:
                #Concatenate item values
                fout.write('    initDataItem("' + str(item["name"]) + '", ' + str(item["tag"]) + ', "' + str(item["type"]) + '", ' + str(item["size"]) + ');\n')
        
        #Write 2nd part ...
        fout.write(str_templ2)

        #Double iteration in JSON collection names
        for collection in json_string:
            for item in json_string[collection]:
                #Concatenate item values
                fout.write('    Colection.' + str(collection) + '->push("' + str(item["name"]) + '");\n')
        
        #Write 3rd part ...
        fout.write(str_templ3)


