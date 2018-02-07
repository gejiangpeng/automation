import os
import argparse
import datetime

class Configuration:
    def __init__(self):
        self.run_test_loc=os.path.join('..','framework','runtest.py')
        if(not os.path.isfile(self.run_test_loc)):
            self.run_test_loc=os.path.join('..','framework','runtest.pyc')
    
    def load(self, filepath):
        temp_settings_dict={}
        if(not os.path.isfile(filepath)):
            raise IOError('{0} is not a file'.format(filepath))
        with open(filepath, 'rb') as f:
            exec(f.read(), {},temp_settings_dict)
            for key in temp_settings_dict.keys():
                setattr(self, key, temp_settings_dict[key])

def main():
    exit_code=0
    run_set_name='run_set_'+datetime.datetime.now().strftime('%Y_%m_%d-%H-%M-%S')
    return run_set_name
           
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('configuration_file', type=str, help='A python file with parameters')
    args=parser.parse_args()
    config_file=args.configuration_file
    configuration=Configuration()
    configuration.load(config_file)
    for para in configuration.__dict__:
        print(para, ':',configuration.__dict__[para])
    print(main())