append_text='\nthis is appended words'

my_file=open('my file.text','a')
my_file.write(append_text)
my_file.close()
