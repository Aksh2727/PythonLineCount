""" Importing Modules"""
import sys
import os


def get_files(file_path,file_ext):
    """ Function to get all required files"""
    # Creating a lit of all files with desired file extension
    file_list = []
    for root, _ , files in os.walk(file_path, topdown=True):
        for name in files:
            file = os.path.join(root, name)
            if file.endswith(file_ext) is True:
                file_list.append(file)
    return file_list

def line_count_func(input_file_path,file_extension='txt'):
    """ Function to count lines"""
    list_of_file = get_files(input_file_path,file_extension)
    output_list = []
    if len(list_of_file) == 0:
        print("No file present")
        output_list.append("No file present")
    else:
        file_dic = {} # Creating empty dictionary to store files and their line count
        total_lines = 0
        for i in list_of_file: # Looping through list of files
            line_count = 0
            with open(i, encoding = 'utf-8') as file_handle:
                for _ in file_handle: # Counting total number of lines in each file
                    line_count += 1

            file_dic[i] = line_count
            total_lines += line_count # Counting total number of lines in all files
        # Printing required output
        for key,value in file_dic.items():
            print(key,' : ',value)
            output_list.append(key+' : '+str(value))
        print("===============")
        num_files = len(list_of_file)
        print('Number of files found: ',num_files)
        output_list.append('Number of files found : ' + str(num_files))
        print('Total number of lines: ',total_lines)
        output_list.append('Total number of lines : ' + str(total_lines))
        print('Average lines per file:',f'{(total_lines/num_files):.2f}')
        output_list.append('Average lines per file : ' + str(f'{(total_lines/num_files):.2f}'))
    return output_list

# Main Function
if __name__ == "__main__":

    # Default value of arguments
    INPUT_FILE_PATH = 'not_given'
    FILE_EXTENSION  = '.txt'

    # Checking for passed arguments
    if len(sys.argv) >= 2:
        INPUT_FILE_PATH = sys.argv[1]
        if len(sys.argv) == 3:
            FILE_EXTENSION = sys.argv[2]
    line_count_func(INPUT_FILE_PATH,FILE_EXTENSION)
