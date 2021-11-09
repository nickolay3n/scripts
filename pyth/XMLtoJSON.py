#!/usr/bin/env python
#sudo apt install python3-pip
#apt install python-pip
#pip3 install simplejson
#pip3 install xmltodict

"""
how to use
find . -name "*.xml" -exec python3 ./my.py {} \;
"""

from sys import argv
import sys
import re
#from xml.etree import ElementTree as ET
#from xml.dom import minidom
import simplejson as json
import xmltodict
import codecs
import os 
#import traceback
'''
def parse_element(element):
    dict_data = dict()
    if element.nodeType == element.TEXT_NODE:
        dict_data['data'] = element.data
    if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_NODE, 
                                element.DOCUMENT_TYPE_NODE]:
        for item in element.attributes.items():
            dict_data[item[0]] = item[1]
    if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_TYPE_NODE]:
        for child in element.childNodes:
            child_name, child_dict = parse_element(child)
            if child_name in dict_data:
                try:
                    dict_data[child_name].append(child_dict)
                except AttributeError:
                    dict_data[child_name] = [dict_data[child_name], child_dict]
            else:
                dict_data[child_name] = child_dict 
    return element.nodeName, dict_data

def parseXmlToJson(xml):
  response = {}
  for child in xml.iter():
    if len(list(child)) > 0:
      response[child.tag] = parseXmlToJson(child)
    else:
      response[child.tag] = child.text or ''
  return response
'''

#функция обхода и получения схемы
def getScheme(obj):
  myScheme='None'
  for keys,values in obj.items():
    if myScheme =='None':
      try:
        myScheme = obj.get('@xmlns')
      except Exception:  # при любом возникшем исключении код продолжит просто работать дальше:
        pass     
      if str(type(values)).__contains__("OrderedDict"):
        myScheme = getScheme(values)
  return myScheme

#возвращает имя файла схемы по соответствию в словаре
def getSchemeFilePath(myScheme):
  SchemeFilePath = 'None'
  mySchemeDict = {'http:// naming sceme': '/hotels/Справочники/scheme.csv',
   'http:// naming sceme 2': '/hotels/Справочники/scheme2.csv'}
  SchemeFilePath = os.path.dirname(os.path.realpath(__file__))+mySchemeDict.get(myScheme)
  return SchemeFilePath

#возвращает словарь созданный из схемы
def getDictScheme(SchemeFilePath):
  SchemeDict = {}
  file1 = codecs.open(SchemeFilePath, 'r', encoding='utf-8', errors='ignore')
  while True:
    line = file1.readline()
    if not line:
        break
    line.replace('"', '')#убираем кавычки
    line = re.sub("^\s+|\n|\r|\s+$", '', line)#убираем пробелы в начале и конце строки и символы переноса строки
    my_list = line.split(",")#строчку в массив
    if len(my_list)>=2:
      elementstr = str(my_list[len(my_list)-1])
      if elementstr == '':
        elementstr = str(my_list[len(my_list)-2])
      if elementstr == '':
        elementstr = str(my_list[len(my_list)-3])
      SchemeDict.update({my_list[0]: elementstr})
  file1.close
  return SchemeDict

#замены элементов в считанном файле XML данными словаря схемы
def XmlSubstitute(obj,SchemeDict):
  for keys,values in obj.items():
    try:
      if keys == 'element':
        elementID = obj.get('element')
        if str(SchemeDict.get(elementID)) != "None":
          obj.update({'element':str(SchemeDict.get(elementID).replace('"', ''))})
    except Exception:  # при любом возникшем исключении код продолжит просто работать дальше:
      pass     
      #traceback.print_exc()
    if str(type(values)).__contains__("OrderedDict"):
      values = XmlSubstitute(values,SchemeDict)
  return obj

if __name__ == "__main__":
  file_path = ""
  if len(sys.argv) == 2:
    script, file_path = argv
  else:
    print("no imput xml file")
  #myfunc(file_path)
  #dom = minidom.parse(file_path)
  #f = open('data.json', 'w')
  #f.write(json.dumps(parse_element(dom), sort_keys=True, indent=4))
  #print(json.dumps(parse_element(dom), indent=2))
  #f.close()
  #with open(file_path,"r",encoding="utf-8") as f:
  with open(file_path,"r") as f:
    obj = xmltodict.parse(f.read())
    nameScheme = getScheme(obj)#распечатать название схемы из файла
    SchemeFilePath = getSchemeFilePath(nameScheme)#распечатать имя файла схемы
    SchemeDict = getDictScheme(SchemeFilePath)
    obj = XmlSubstitute(obj,SchemeDict)
    #print(json.dumps(obj)) #old easy printing
    json_unicode_escape_string = json.dumps(obj)
    print(codecs.decode(json_unicode_escape_string, 'unicode-escape')) 