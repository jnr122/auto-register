import constants
import urllib.request
import re

# first make a link to the schedule of course for the given term
soc_link = 'https://giraffe.uvm.edu/~rgweb/batch/swrsectc_spring_soc_'+constants.TERM+'/all_sections.html'
data = urllib.request.urlopen(soc_link).read(10000)
text = data.decode("utf-8") # change it from bytes type to string
classes = text.split(' ')
#classes1 = text.remove('<a href="https://aisweb1.uvm.edu/pls/owa_prod/bwckschd.p_disp_listcrse?term_in=202001&amp;subj_in=AS&amp;crse_in=095&amp;crn_in=')
for i in range(len(classes)):
    if classes[i] =='':
        classes[i] = 'HEY'
classes.remove("HEY")
for temp in classes:
    print(temp)