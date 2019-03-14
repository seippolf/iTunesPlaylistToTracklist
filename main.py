import os
def playlist_to_list(filename):
    # Split file to list by new line
    playlist_as_list = open(filename, 'r').read().split('\n')
    playlist_as_list.pop()
    return(playlist_as_list)

def strip_to_song_and_artist(list_in):
    artist_song_list = ['']*(len(list_in))
    for i in range(len(list_in)):
        split_line = list_in[i].split('	')
        artist_song_list[i] = str(split_line[1] + ' - ' + split_line[0])
    return(artist_song_list)

def generate_list_file(list_in, filename):
    file_from_list = open(filename, 'w')
    for i in range(len(list_in)):
        file_from_list.write(list_in[i] + '\n')

def user_input_handling():
    keep_looping = True
    while(keep_looping):
        input_file_name = raw_input('Filename: ')
        # Check if file exists and ends with .txt
        if(os.path.isfile('./' + input_file_name) and input_file_name.endswith('.txt')):
            # Ask for a filename to export to
            target_file_name = raw_input('Name of output file: ')
            #Check if the filename they entereed end in a .txt
            if(target_file_name.endswith('.txt')):
                #Check if the entered filename exists
                if(os.path.isfile('./' + target_file_name)):
                    overwrite_existing_file =  raw_input('A file by this name already exists. Overwrite? (y/n): ')
                    #yes
                    if(overwrite_existing_file == 'y'):
                        #Generate file
                        print('Generating...')
                        generate_list_file(strip_to_song_and_artist(playlist_to_list(input_file_name)), target_file_name)
                        keep_looping = False
                else:
                    print('Generating...')
                    generate_list_file(strip_to_song_and_artist(playlist_to_list(input_file_name)), target_file_name)    
                    keep_looping = False
            else:
                print('\'.txt\' is the only supported filetype.')
        else:
            print('File either cannot be found, or does not end in \'.txt\'.  ') 
user_input_handling()
# Make sure to do if statement checking if filename is a txt...