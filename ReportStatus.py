import os
from ttk import *
from Tkinter import *
from xml.etree import ElementTree

# In ms enter the delay to update
updateDelay = 1000
file_name = 'status.xml'
full_file = os.path.abspath(os.path.join(file_name))


def update_fields():
    global i, flag, network_label, contact_label, hardware_label, software_label, errors, warnings
    global dFlag, last_run, diagnostic_label, sys_time, peripheral, peripheral_label
    # System Info - Hardware and Software
    hardware_label[0] = Label(tab1, text='Hardware Information', padx=5, pady=5, font=("Arial Bold", 12))
    hardware_label[1] = Label(tab1, text='Serial', padx=5, pady=5, font=("Arial", 12))
    hardware_label[2] = Label(tab1, text='Temperature', padx=5, pady=5, font=("Arial", 12))
    hardware_label[3] = Label(tab1, text='Fan Speeds', padx=5, pady=5, font=("Arial", 12))

    software_label[0] = Label(tab1, text='Software Information', padx=5, pady=5, font=("Arial Bold", 12))
    software_label[1] = Label(tab1, text='Name', padx=5, pady=5, font=("Arial", 12))
    software_label[2] = Label(tab1, text='Version', padx=5, pady=5, font=("Arial", 12))
    software_label[3] = Label(tab1, text='Release Date', padx=5, pady=5, font=("Arial", 12))
    software_label[4] = Label(tab1, text='Encryption', padx=5, pady=5, font=("Arial", 12))
    software_label[5] = Label(tab1, text='Multi-Site', padx=5, pady=5, font=("Arial", 12))
    software_label[6] = Label(tab1, text='Premium-Resolution', padx=5, pady=5, font=("Arial", 12))
    software_label[7] = Label(tab1, text='Remote-Monitoring', padx=5, pady=5, font=("Arial", 12))

    if flag[0] == 1:
        flag[0] = 0
        for i in range(len(hardware)):
            hardware_label[4+i] = Label(tab1, text=hardware[i], padx=5, pady=5, font=("Arial", 12))
        for i in range(len(software)):
            software_label[8 + i] = Label(tab1, text=software[i], padx=5, pady=5, font=("Arial", 12))
    else:
        for i in range(len(hardware)):
            hardware_label[4+i].config(text=hardware[i], padx=5, pady=5, font=("Arial", 12))
        for i in range(len(software)):
            software_label[8+i].config(text=software[i], padx=5, pady=5, font=("Arial", 12))

    hardware_label[0].grid(column=0, row=0, sticky=W)
    hardware_label[1].grid(column=0, row=1, sticky=W)
    hardware_label[2].grid(column=0, row=2, sticky=W)
    hardware_label[3].grid(column=0, row=3, sticky=W)
    hardware_label[4].grid(column=1, row=1, sticky=W)
    hardware_label[5].grid(column=1, row=2, sticky=W)
    hardware_label[6].grid(column=1, row=3, sticky=W)

    software_label[0].grid(column=0, row=4, sticky=W)
    software_label[1].grid(column=0, row=5, sticky=W)
    software_label[2].grid(column=0, row=6, sticky=W)
    software_label[3].grid(column=0, row=7, sticky=W)
    software_label[4].grid(column=0, row=8, sticky=W)
    software_label[5].grid(column=0, row=9, sticky=W)
    software_label[6].grid(column=0, row=10, sticky=W)
    software_label[7].grid(column=0, row=11, sticky=W)
    software_label[8].grid(column=1, row=5, sticky=W)
    software_label[9].grid(column=1, row=6, sticky=W)
    software_label[10].grid(column=1, row=7, sticky=W)
    software_label[11].grid(column=1, row=8, sticky=W)
    software_label[12].grid(column=1, row=9, sticky=W)
    software_label[13].grid(column=1, row=10, sticky=W)
    software_label[14].grid(column=1, row=11, sticky=W)

    # System Info - Diagnostic Information
    diagnostic_label[0] = Label(tab6, text='SysInfo - Diagnosis', padx=5, pady=5, font=("Arial Bold", 12))
    diagnostic_label[1] = Label(tab6, text='Last Run', padx=5, pady=5, font=("Arial", 12))
    diagnostic_label[2] = Label(tab6, text='System Time', padx=5, pady=5, font=("Arial", 12))
    diagnostic_label[5] = Label(tab6, text='ERRORS', padx=5, pady=5, font=("Arial", 12), fg='RED')
    diagnostic_label[6] = Label(tab6, text='WARNINGS', padx=5, pady=5, font=("Arial", 12), fg='BLUE')

    global temp, temp2
    temp = []
    temp2 = []
    temp = "\n\n".join(str(e) for e in errors)
    temp2 = "\n\n".join(str(w) for w in warnings)
    if dFlag == 1:
        dFlag = 0
        diagnostic_label[3] = Label(tab6, text=last_run, padx=5, pady=5, font=("Arial", 12))
        diagnostic_label[4] = Label(tab6, text=sys_time, padx=5, pady=5, font=("Arial", 12))
        diagnostic_label[7] = Label(tab6, text=temp, padx=5, pady=5, font=("Arial", 12), wraplength=600
                                    , relief=RIDGE, justify=LEFT)
        diagnostic_label[8] = Label(tab6, text=temp2, padx=5, pady=5, font=("Arial", 12), wraplength=600
                                    , relief=RIDGE, justify=LEFT)

    else:
        diagnostic_label[3].config(text=last_run, padx=5, pady=5, font=("Arial", 12))
        diagnostic_label[4].config(text=sys_time, padx=5, pady=5, font=("Arial", 12))
        diagnostic_label[7].config(text=temp, padx=5, pady=5, font=("Arial", 12))
        diagnostic_label[8].config(text=temp2, padx=5, pady=5, font=("Arial", 12))

    diagnostic_label[0].grid(column=0, row=0, sticky=W, columnspan=2)
    diagnostic_label[1].grid(column=0, row=1, sticky=W)
    diagnostic_label[2].grid(column=0, row=2, sticky=W)
    diagnostic_label[3].grid(column=1, row=1, sticky=W)
    diagnostic_label[4].grid(column=1, row=2, sticky=W)
    diagnostic_label[5].grid(column=0, row=3, sticky=W, columnspan=2)
    diagnostic_label[7].grid(column=0, row=4, sticky=W, columnspan=2)
    diagnostic_label[6].grid(column=0, row=5, sticky=W, columnspan=2)
    diagnostic_label[8].grid(column=0, row=6, sticky=W, columnspan=2)


    # Peripherals
    temp = []
    for p in peripheral:
        if p.find('Type').text != 'Camera':
            temp.append("Device: " + p.find('Type').text)
        else:
            temp.append("Device-" + p.find('Type').text + " | HardwareInfo-" + str(p.find('HardwareInfo').text) +
                        " | ID-" + str(p.find('ID').text) + " | Name-" + str(p.find('Name').text) + " | SoftwareInfo-" +
                        str(p.find('SoftwareInfo').text) + " | Status-" + str(p.find('Status').text)
                        + " | UpgradeStatus-" + str(p.find('UpgradeStatus').text))
        temp.append("\n")
    temp = "\n".join(str(p) for p in temp)
    lbl2 = Label(tab2, text='Connected Devices', padx=5, pady=5, font=("Arial Bold", 12))
    lbl2.grid(column=0, row=0, sticky=W, columnspan=2)
    if flag[1] == 1:
        flag[1] = 0
        peripheral_label = Label(tab2, text=temp, padx=5, pady=5, font=("Arial", 12), wraplength=600, justify=LEFT
                                 , relief=RIDGE)
    else:
        peripheral_label.config(text=temp, padx=5, pady=5, font=("Arial", 12), wraplength=600, justify=LEFT
                                , relief=RIDGE)
    peripheral_label.grid(column=0, row=1, sticky=W, columnspan=2)



    # Call-Details
    lbl3 = Label(tab3, text='label2')
    lbl3.grid(column=0, row=0)

    # Network Tab
    for i in range(len(network)):
        network[i] = "Not Available" if not network[i] else network[i]
    if flag[3] == 1:
        flag[3] = 0
        network_label[0] = Label(tab4, text='Network Information', padx=5, pady=5, font=("Arial Bold", 12))
        network_label[1] = Label(tab4, text='MAC', padx=5, pady=5, font=("Arial", 12))
        network_label[3] = Label(tab4, text='IPv4 Address', padx=5, pady=5, font=("Arial", 12))
        network_label[5] = Label(tab4, text='IPv6 Address', padx=5, pady=5, font=("Arial", 12))
        for i in range(len(network)):
            network_label[i*2+2] = Label(tab4, text=network[i], padx=5, pady=5, font=("Arial", 12))
    else:
        for i in range(len(network)):
            network_label[i*2+2].config(text=network[i], padx=5, pady=5, font=("Arial", 12))
    network_label[0].grid(column=0, row=0, sticky=W)
    network_label[1].grid(column=0, row=2, sticky=W)
    network_label[2].grid(column=1, row=2, sticky=W)
    network_label[3].grid(column=0, row=3, sticky=W)
    network_label[4].grid(column=1, row=3, sticky=W)
    network_label[5].grid(column=0, row=4, sticky=W)
    network_label[6].grid(column=1, row=4, sticky=W)

    # Contact Tab
    contact_label[0] = Label(tab5, text='Contact Information:', padx=5, pady=50, font=("Arial Bold", 12))
    if flag[4] == 1:
        flag[4] = 0
        contact_label[1] = Label(tab5, text=contact[0], font=("Arial", 12))
    else:
        contact_label[1].config(text=contact[0], font=("Arial", 12))
    contact_label[0].grid(column=0, row=0, sticky=W)
    contact_label[1].grid(column=1, row=0,sticky=W)
    contact_label[2] = Label(tab5, image=logo, padx=5, pady=5).grid(column=0, row=1, columnspan=2,sticky=W)


def update():
    # with open('status.xml') as fd:
    #     doc = xmltodict.parse(fd.read())
    #     # hardware_serial
    #     hardware[0] = doc['Status']['SystemUnit']['Hardware']['Module']['SerialNumber']
    #     # hardware_temp
    #     hardware[1] = doc['Status']['SystemUnit']['Hardware']['Temperature']
    #     # hardware_fanSpeeds
    #     hardware[2] = [fan['Status'] for fan in doc['Status']['SystemUnit']['Hardware']['Monitoring']['Fan']]
    #     #
    #     software[0] = doc['Status']['SystemUnit']['Software']['Name']
    #     software[1] = doc['Status']['SystemUnit']['Software']['Version']
    #     software[2] = doc['Status']['SystemUnit']['Software']['ReleaseDate']
    #     software[3] = doc['Status']['SystemUnit']['Software']['OptionKeys']['Encryption']
    #     software[4] = doc['Status']['SystemUnit']['Software']['OptionKeys']['MultiSite']
    #     software[5] = doc['Status']['SystemUnit']['Software']['OptionKeys']['PremiumResolution']
    #     software[6] = doc['Status']['SystemUnit']['Software']['OptionKeys']['RemoteMonitoring']
    #     #
    #     last_run[0] = doc['Status']['SystemUnit']['Diagnostics']['LastRun']['#text']
    #
    #     errors[:] = []
    #     warnings[:] = []
    #     for message in doc['Status']['SystemUnit']['Diagnostics']['Message']:
    #         # print type([message['Level']])
    #         if [message['Level']['#text']] == ['Error']:
    #             errors.append(message['Description']['#text'])
    #         else:
    #             warnings.append(message['Description']['#text'])
    #     #
    #     peripherals = doc['Status']['Peripherals']['ConnectedDevice']
    #     # If camera show complete details
    #     # for device in doc['Status']['Peripherals']['ConnectedDevice']:
    #     # if device['Type']['#text'] == ['Camera']:
    #     #
    #     # mac_address
    #     network[0] = doc['Status']['Network']['Ethernet']['MacAddress']
    #     #IPv4
    #     network[1] = doc['Status']['Network']['IPv4']['Address']
    #     #IPv6
    #     network[2] = doc['Status']['Network']['IPv6']['Address']
    #     #
    #     sys_time[0] = doc['Status']['Time']['SystemTime']
    #     #
    #     contact[0] = doc['Status']['UserInterface']['ContactInfo']['Name']
    #     #
    #     # CALL

    dom = ElementTree.parse(full_file)
    hardware[0] = dom.find('SystemUnit').find('Hardware').find('Module').find('SerialNumber').text
    hardware[1] = dom.find('SystemUnit').find('Hardware').find('Temperature').text
    fans = dom.find('SystemUnit').find('Hardware').find('Monitoring').findall('Fan')
    hardware[2] = " | ".join(str(fan.find('Status').text) for fan in fans)

    software[0] = dom.find('SystemUnit').find('Software').find('Name').text
    software[1] = dom.find('SystemUnit').find('Software').find('Version').text
    software[2] = dom.find('SystemUnit').find('Software').find('ReleaseDate').text
    software[3] = dom.find('SystemUnit').find('Software').find('OptionKeys').find('Encryption').text
    software[4] = dom.find('SystemUnit').find('Software').find('OptionKeys').find('MultiSite').text
    software[5] = dom.find('SystemUnit').find('Software').find('OptionKeys').find('PremiumResolution').text
    software[6] = dom.find('SystemUnit').find('Software').find('OptionKeys').find('RemoteMonitoring').text

    last_run[0] = dom.find('SystemUnit').find('Diagnostics').find('LastRun').text
    sys_time[0] = dom.find('Time').find('SystemTime').text
    errors[:] = []
    warnings[:] = []
    for message in dom.find('SystemUnit').find('Diagnostics').findall('Message'):
        if message.find('Level').text == 'Error':
            errors.append(message.find('Description').text)
        elif message.find('Level').text == 'Warning':
            warnings.append(message.find('Description').text)

    contact[0] = dom.find('UserInterface').find('ContactInfo').find('Name').text

    network[0] = dom.find('Network').find('Ethernet').find('MacAddress').text
    network[1] = dom.find('Network').find('IPv4').find('Address').text
    network[2] = dom.find('Network').find('IPv6').find('Address').text

    global peripheral
    peripheral = []
    for peripheral_device in dom.find('Peripherals').findall('ConnectedDevice'):
        peripheral.append(peripheral_device)

    update_fields()
    window.after(updateDelay, update)


hardware = ['']*3
hardware_label = ['']*7
network = ['']*3
network_label = ['']*7
contact = ['']
contact_label = ['']*3
software = ['']*7
software_label = ['']*15
last_run = ['']
diagnostic_label = ['']*50
errors = []
warnings = []
flag = [1]*5
dFlag = 1
sys_time = ['']
i = 0
peripheral = []
peripheral_label = ''

window = Tk()
window.title("Cisco Video Endpoint Diagnostic Tool")
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)
tab_control = Notebook(window)
logo = PhotoImage(file="logo_bg_clear.gif")

tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)
tab4 = Frame(tab_control)
tab5 = Frame(tab_control)
tab6 = Frame(tab_control)

tab_control.add(tab1, text='System Information ')
tab_control.add(tab6, text='Diagnostic Information ')
tab_control.add(tab2, text='Peripherals ')
tab_control.add(tab3, text='Call Details ')
tab_control.add(tab4, text='Network Information ')
tab_control.add(tab5, text='Contact')
tab_control.pack(expand=1, fill='both')

window.after(100, update)
window.wm_iconbitmap('ir_dark.ico')
window.mainloop()
