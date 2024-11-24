import comport as flasher

def button_interface(ui) :
    def connect_buttons(buttons, function):
        for button in buttons:
            button.clicked.connect(function)
    connect_buttons([ui.zb_flash_btn_2], lambda: flasher.flash_even(ui,0,0))
    connect_buttons([ui.zb_erase_btn_3], lambda: flasher.flash_even(ui,0,1))
    connect_buttons([ui.auto_start], lambda: flasher.auto_flash_even(ui, 1, 0, 1, True))
    connect_buttons([ui.auto_stop_2], lambda: flasher.auto_flash_even(ui, 1, 0, 1, False))