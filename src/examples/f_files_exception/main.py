#main program
import files

def main():
    file_name = 'pickle_dictionary.bin'
    #files.output_dictionary_to_file(file_name)
    files.read_dictionary_from_file(file_name)
    

main()