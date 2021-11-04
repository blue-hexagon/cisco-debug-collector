from tkinter import *

from cisco_director import *
from gui.component.config_panel import ConfigPanel
from gui.component.control_panel import ControlButtonPanel
from gui.component.host_panel import HostPanel
from gui.component.io_panel import IOPanel
from gui.component.menubar import Menubar
from gui.component.statusbar import Statusbar




class TkinterInitializer:
    def __init__(self):
        self.device_manager = DeviceManager()
        self.root = Tk()
        self.root.title("Cisco Debug Collector")
        self.program_config = ProgramConfig()

        self.config_panel = LabelFrame(text="", padx=4, pady=4)
        self.hosts_panel = LabelFrame(text="IPv4/6 Hosts", padx=4, pady=4)
        self.logging_panel = LabelFrame(text="IO Direction", padx=4, pady=4)
        self.statusbar_panel = PanedWindow()

        self.config_panel.grid(column=0, row=0, columnspan=80, sticky="we", padx=4, pady=4)
        self.hosts_panel.grid(column=0, row=1, padx=4, pady=4)
        self.logging_panel.grid(column=1, row=1, padx=4, pady=4, sticky="news")
        self.statusbar_panel.grid(column=0, row=10, columnspan=80, sticky="we")

        self.statusbar = Statusbar(self.statusbar_panel)
        self.menubar = Menubar(self.root)
        self.checkbox_panel = ConfigPanel(self.config_panel, self.statusbar)
        self.control_button_panel = ControlButtonPanel(self.config_panel)
        self.hosts_panel = HostPanel(self.hosts_panel, self.program_config, self.device_manager, 13)
        self.io_panel = IOPanel(self.logging_panel)

        self.root.mainloop()
