import os
import threading
# Path to the cc2538-bsl tool
cc2538_bsl_path = "Firmware/cc2538-bsl.py"
# Path to the firmware file
#--------------------------------------------------------------------
# Present Firmware
firmware_file = ["","Firmware/Coordinator_ch25_tx20_Release_9-6-2024.hex","Firmware/CC1352P2_CC2652P_launchpad_router_20221102.hex"]
# Hyper Firmware
#firmware_file = "Firmware/Coordinator_ch25_tx20_Release_9-6-2024.hex"
# Router Firmware
#firmware_file = "Firmware/CC1352P2_CC2652P_launchpad_router_20221102.hex"
#--------------------------------------------------------------------
# Serial port to which the launchpad is connected

def flash_firmware(ui,cc2538_bsl_path, firmware_file, serial_port):
    command = f"python {cc2538_bsl_path} -p {serial_port} -e -v -w --bootloader-sonoff-usb {firmware_file}"
    # Execute the command
    print("Executing command:", command)
    result = os.system(command)
    #print_even(ui,command)
    if result == 0 :
        print("Firmware flashed successfully.")
    else:
        print("Error occurred while flashing the firmware. Return code:", str(result))

def erase_firmware(ui,serial_port):
    # Example command to disable bootloader, replace with actual command if different
    
    erase_cmd = f"python {cc2538_bsl_path} -p {serial_port} -e  {firmware_file[0]}"
    disable_fw = os.system(erase_cmd)

    if disable_fw == 0 :
        print("Erase Firmware successfully.")
    else:
        print("Error occurred while Erase Firmware. Return code:", str(disable_fw))

def sonoff_usb(ui,port,flashmode) :
    selected_file = ui.rf_type_box_3.currentIndex()
    print("cc2538-bsl path:", cc2538_bsl_path)
    print("Serial port:", port)
    print("Firmware file:", firmware_file[selected_file])
    # Verify that the paths and files exist
    if not os.path.isfile(cc2538_bsl_path):
        print(f"Error: The cc2538-bsl script at '{cc2538_bsl_path}' was not found.")
    elif not os.path.isfile(firmware_file[selected_file]):
        print(f"Error: The firmware file was not found.")
    elif flashmode == 0 :
        flash_firmware(ui,cc2538_bsl_path, firmware_file[selected_file], port)
    elif flashmode == 1 : 
        erase_firmware(ui,port)

