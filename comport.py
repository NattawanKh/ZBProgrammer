import time
import serial.tools.list_ports
from ZBProgramer import *
import threading
import aleart

programmin_logic_auto = True
stop_event = threading.Event()

def flash_even(ui,mode,flashmode):
    thr = threading.Thread(target=list_com_ports, args=[ui,mode,flashmode])
    thr.start() 
    ui.zdb_status_2.setText(
            "Status : <span style=\"color:orange\">In Progress</span></p>")  
    
def auto_flash_even(ui, mode, flashmode, interval, start):
    """
    Starts or stops the flashing operation.
    """
    global stop_event
    print("No active thread to stop.")
    if start:  # Start the thread
        if not hasattr(ui, 'worker_thread') or not ui.worker_thread.is_alive():
            stop_event.clear()  # Reset stop_event before starting
            ui.worker_thread = threading.Thread(
                target=run_interval, 
                args=(ui, mode, flashmode, interval), 
                daemon=True  # Ensure thread exits with the main program
            )
            ui.worker_thread.start()
            ui.zdb_status_2.setText(
                "Status : <span style=\"color:orange\">Automatic In Progress</span></p>"
            )
        else:
            print("Thread is already running.")
    else:  # Stop the thread
        
        if hasattr(ui, 'worker_thread') and ui.worker_thread.is_alive():
            stop_event.set()  # Signal the thread to stop
            ui.worker_thread.join(timeout=2)  # Wait for the thread to stop (with a timeout)
            if ui.worker_thread.is_alive():
                print("Thread did not stop cleanly. Force stopping.")
            else:
                ui.zdb_status_2.setText(
                    "Status : <span style=\"color:Orange\">Automatic Mode Stopped</span></p>"
                )
        else:
            print("No active thread to stop.")


def list_com_ports(ui,mode,flashmode):
    global programmin_logic_auto
    ports = serial.tools.list_ports.comports()
    if mode == 1 :
        ui.zdb_status_2.setText(
                    "Status : <span style=\"color:orange\">Automatic In Progress</span></p>"
                )
    available_ports = []
    available_devices=[]
    for port in ports:
        port_info = {
            'device': port.device,
            'description': port.description
        }
        if port.description.startswith("Silicon Labs CP210x USB to UART Bridge") :
            available_ports.append(port_info['device'])
            available_devices.append(port_info['description'])
            
    port_count = len(available_ports)
    if port_count != 0 :
        if programmin_logic_auto : 
            for port in available_ports :
                print(port)
                print("Logic : "+ str(programmin_logic_auto))
                sonoff_usb(ui,port,flashmode)
            programmin_logic_auto = False
            print("Flash Finish")   
            selected_file = ui.rf_type_box_3.currentIndex()
            if selected_file > 0 :
                ui.zdb_status_2.setText(
                    "Status : <span style=\"color:#4CAF50\"> Process Finish </span></p>") 
                note = "Process Finish"
                aleart.alert_helper.show_alert_signal.emit(note)   
            else :
                ui.zdb_status_2.setText(
                    "Status : <span style=\"color:RED\"> Please Select Type</span></p>") 
                note = "Please Select Devices Type"
                aleart.alert_helper.show_alert_signal.emit(note)
                if mode == 1 :
                    auto_flash_even(ui, 1, 0, 1, False)     
                    mode == 0
            if mode == 0 :
                programmin_logic_auto = True
                
        else :
            #print("Please Remove Your Dongle and Insert New Devices")
            ui.zdb_status_2.setText(
                    "Status : <span style=\"color:orange\"> Remove and Insert New</span></p>")
            if mode == 0 :
                note = " Remove and Insert New Devices"
                aleart.alert_helper.show_alert_signal.emit(note)
                programmin_logic_auto = True  
             

            
    else :
        programmin_logic_auto = True
        # print("Please Connect The Dongle")
        # ui.zdb_status_2.setText(
        #         "Status : <span style=\"color:Red\"> Devices No Found</span></p>")

def run_interval(ui, mode, flashmode, interval):
    """
    Periodically executes the list_com_ports function.
    Stops when `stop_event` is set.
    """
    while not stop_event.is_set():
        try:
            # Your actual logic here
            list_com_ports(ui, mode, flashmode)
        except Exception as e:
            print(f"Error in thread: {e}")
        
        # Sleep in smaller increments to allow frequent stop checks
        for _ in range(int(interval * 10)):
            if stop_event.is_set():
                break
            time.sleep(0.1)
    print("Thread stopped.")

        
#list_com_ports()
#run_interval(list_com_ports, 1,True)