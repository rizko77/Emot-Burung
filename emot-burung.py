import ascii_magic

try :
    my_art = ascii_magic.from_image_file('images/burung.png')
    ascii_magic.to_terminal(my_art)
except Exception as e:
    print('Error Bang Hehe |',e)