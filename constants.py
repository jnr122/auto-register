
# nav links
AIS_LOGIN_URL = "https://aisweb1.uvm.edu/pls/owa_prod/twbkwbis.P_ValLogin"
AIS_MENU_URL = "https://aisweb1.uvm.edu/pls/owa_prod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu"
AIS_TERM_SELECTION_URL = "https://aisweb1.uvm.edu/pls/owa_prod/bwskfreg.P_AltPin"
ADD_URL = "https://aisweb1.uvm.edu/pls/owa_prod/bwckcoms.P_Regs"
DUMMY = "RSTS_IN=DUMMY&assoc_term_in=DUMMY&CRN_IN=DUMMY&start_date_in=DUMMY&end_date_in=DUMMY&SUBJ=DUMMY&CRSE=DUMMY&SEC=DUMMY&LEVL=DUMMY&CRED=DUMMY&GMOD=DUMMY&TITLE=DUMMY&MESG=DUMMY&REG_BTN=DUMMY&UVM_REQ_WD_IND_IN=DUMMY&MESG=DUMMY&"
MYUVM_LOGIN_URL = "https://myuvm.uvm.edu"

# so I look like a browser
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"

# info
CLASSES_TEXT = "aux/classes.txt"
LOGIN_TEXT = "aux/login.txt"
REGISTER_CLASSES_TEXT = "aux/register_classes.txt"

# term info
TERM = "202009"
# Url for the "Look for a class to add" site
# CLASS_SCHEDULE = "https://myuvm.uvm.edu/web/home-community/registrar?p_p_id=56_INSTANCE_UHUqm6dYpw1z&p_p_lifecycle=0&p_p_state=maximized&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=3&link_id=19"


CLASS_SEARCH = "https://aisweb1.uvm.edu/pls/owa_prod/bwskfcls.p_sel_crse_search"
CLASS_SCHEDULE="https://aisweb1.uvm.edu/pls/owa_prod/bwckgens.p_proc_term_date"
LOGIN_CLASS_SCHEDULE = "https://aisweb1.uvm.edu/pls/owa_prod/twbkwbis.P_ValLogin"

ALL_COURSES_LINK = "https://aisweb1.uvm.edu/pls/owa_prod/bwskfcls.P_GetCrse_Advanced"
POST_ALL_COURSES = "rsts=dummy&crn=dummy&term_in=" + TERM + "&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_crse=&sel_title=%25&sel_insm=%25&sel_from_cred=&sel_to_cred=&sel_camp=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a&SUB_BTN=Section+Search&path=1"
ADD_CLASS_REFERER = "https://myuvm.uvm.edu/web/home-community/registrar?p_p_id=56_INSTANCE_UHUqm6dYpw1z&p_p_lifecycle=0&p_p_state=maximized&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=3&link_id=19"
