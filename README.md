# auto-register
So I don't have to wake up to register for my classes, or schedule them

# Reqs
1. Python3
2. requests
3. html/lxml

# Usage - register
1. Store username on first line and password on second line of an adjacent login.txt file
2. Store registration term (e.g. 201909 for fall 2019 or 202001 for spring 2020) followed by all CRNs to add on their own lines in adjacent register_classes.txt file
3. In CLI run <eval sleep 0.1 && python3 auto_login.py | at 7:00 tomorrow> to have it wait for the following morning at 
   7:00am, wait a tenth of a second, and then register
