# learn how to open a web browser in python script

import webbrowser

print("Devployment completed")
# webbrowser.open("https://bus-med.1337.ma/")
c = webbrowser.get('firefox')
c.open('https://bus-med.1337.ma/')
c.open_new_tab('https://bus-med.1337.ma/')