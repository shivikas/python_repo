import re
import os
import os.path


print os.path.basename('/Users/user/Documents/workspace/shivika/modData.txt')
print os.path.dirname('/Users/user/Documents/workspace/shivika/modData.txt')
#print f.readlines()
class ConfParser(object):
    def __init__(self,file_path = '/Users/user/Documents/workspace/shivika/modData.txt'):
        self.__config_dict = {}
        section = None
        with open(file_path,'r') as f:
            for line in f:
                #print line
                section_regex = re.compile(r'^\[(.*)\]$')
                val_regex = re.compile(r'(.*)[\s]*:[\s]*(.*)')
                comment_regex = re.compile(r'^\#.*')
                line = line.strip()
                if not comment_regex.match(line):
                    #print line
                    match = section_regex.search(line)
                    #print match
                    if match:
                        
                        section = match.group(1)
                       # print section
                    else:
                        match = val_regex.match(line)
                        if match:
                            key = match.group(1)
                            val = match.group(2)
                            if section:
                                temp = self.__config_dict.get(section,{})
                                temp[key] = val
                                self.__config_dict[section] = temp
                    
    def dump_config(self):
        print self.__config_dict 
    
    def get_section_data(self,section):
        return self.__config_dict.get(section,None)
    
    def get_config_data(self,section,key):
        if self.__config_dict.has_key(section) and self.__config_dict[section].has_key(key):
            return self.__config_dict[section].get(key,None)
        else:
            return None
        
if __name__ == "__main__":
    obj = ConfParser()
    obj.dump_config()