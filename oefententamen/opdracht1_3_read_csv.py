filenames = ['jan21_meting1.csv', 'jan23_meting1.csv', 'test1.csv', 'jan23_meting2.dat', 'feb23_meting4.csv', 'test4.csv', 'jan23_meting.dat', 'meting3.csv']
selected_files = [filename for filename in filenames if filename.startswith('jan23')]
# or
selected_files = [filename for filename in filenames if filename[0:5] == 'jan23']
