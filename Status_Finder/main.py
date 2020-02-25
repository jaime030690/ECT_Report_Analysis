#Dependencies
import pyperclip

#Open sstsp file
sstsp_file = open('C:/temp/sstsp.txt', 'r')

#Strings for mathing status
case_text = '[SS.TSP]KEY='
status_text = '[SS.TSP.AUDIT]STATUS='
date_text = '[SS.TSP.AUDIT]DATE='
time_text = '[SS.TSP.AUDIT]TIME='
comment_txt = '[SS.TSP.AUDIT]COMMENT='

#Variable and lists
case = ''
status_list = []
date_list = []
time_list = []
comment_list = []
index = 0
target_status = 'CQ'

#Iterate through the file
for line in sstsp_file:

    if case_text in line:
        case = line.split('=', )[1].replace('\n', '')

    elif status_text in line:
        status_list.append(line.split('=', )[1].replace('\n', ''))

    elif date_text in line:
        date_list.append(line.split('=', )[1].replace('\n', ''))
    
    elif time_text in line:
        time_list.append(line.split('=', )[1].replace('\n', ''))

    elif comment_txt in line:
        comment_list.append(line.split('=', )[1].replace('\n', ''))

#Find status on the list, break loop if  found
for status in status_list:
    
    if status == target_status:
        break
    index += 1

#Print out results, no index found error if not
try:
    ts = date_list[index] + ' ' + time_list[index]

    print(f'Case number: {case}')
    print(f'Status: {target_status}')
    print(f'Comment: {comment_list[index]}')
    print(f'Timestamp: {ts}')
    pyperclip.copy(ts)
    pyperclip.paste()
    print('Timestamp copied to clipboard!')

except IndexError as error:
    print("Status not found, please look manually...")