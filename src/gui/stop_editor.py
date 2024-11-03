"""
Stop Editor Gui

Needed Parameters for Editing:
    Stop Information Frame - ttk LabelFrame
    

    Rank Information Frame - ttk LabelFrame
    Rank Information - Frame
    General Harmonic Settings - Frame
    General ADSR Settings - Frame

    Pipe Information Frame - ttk LabelFrame
    Pipe Information - Frame
    Option for Adjusting Harmonics
    ADSR Adjustments

    Save and Cancel buttons

"""
import tkinter as tk
from tkinter import ttk


class SettingsStop(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__ui_widgets()
        self.__ui_layout()

    def __ui_widgets(self):
        # Stop Name
        self.stopname_label = ttk.Label(
            master=self,
            text="Stop Name:"
        )
        self.stopname_entry = ttk.Entry(
            master=self
        )
        # Stop Family
        self.stopfamily_label = ttk.Label(
            master=self,
            text="Stop Family:"
        )
        self.stopfamily_combo = ttk.Combobox(
            master=self
        )
        # Number of Ranks
        self.numranks_label = ttk.Label(
            master=self,
            text="Number of Ranks"
        )
        self.numranks_spin = ttk.Spinbox(
            master=self
        )

    def __ui_layout(self):
        widgets = (
            (self.stopname_label, self.stopname_entry),
            (self.stopfamily_label, self.stopfamily_combo),
            (self.numranks_label, self.numranks_spin)
        )
        for r, row in enumerate(widgets):
            for c, widget in enumerate(row):
                widget.grid(
                    column=c,
                    row=r,
                    padx=4,
                    pady=4,
                    sticky="nsew"
                )


class SettingsRank(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__ui_widgets()
        self.__ui_layout()

    def __ui_widgets(self):
        # Rank Number
        self.ranknum_label = ttk.Label(
            master=self,
            text="Rank #:"
        )
        self.ranknum_spin = ttk.Spinbox(
            master=self
        )
        # Rank Size
        self.ranksize_label = ttk.Label(
            master=self,
            text="Rank Size:"
        )
        self.ranksize_combo = ttk.Combobox(
            master=self
        )
        # Number of Pipes
        self.numpipes_label = ttk.Label(
            master=self,
            text="Number of Pipes:"
        )
        self.numpipes_spin = ttk.Spinbox(
            master=self
        )
        # Number of Harmonics
        self.numharmonics_label = ttk.Label(
            master=self,
            text="Number of Harmonics:"
        )
        self.numharmonics_spin = ttk.Spinbox(
            master=self
        )

    def __ui_layout(self):
        widgets = (
            (self.ranknum_label, self.ranknum_spin),
            (self.ranksize_label, self.ranksize_combo),
            (self.numpipes_label, self.numpipes_spin),
            (self.numharmonics_label, self.numharmonics_spin)
        )
        for r, row in enumerate(widgets):
            for c, widget in enumerate(row):
                widget.grid(
                    column=c,
                    row=r,
                    padx=4,
                    pady=4,
                    sticky="nsew"
                )


class SettingsPipe(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__ui_widgets()
        self.__ui_layout()
    
    def __ui_widgets(self):
        # Pipe Number
        self.pipenum_label = ttk.Label(
            master=self,
            text="Pipe #:"
        )
        self.pipenum_spin = ttk.Spinbox(
            master=self
        )
        # Keyboard Note
        self.keyboardnote_label = ttk.Label(
            master=self,
            text="Keyboard Note:"
        )
        self.keyboardnote_combo = ttk.Combobox(
            master=self
        )
        # Real Note
        self.realnote_label = ttk.Label(
            master=self,
            text="Real Note:"
        )
        self.realnote_combo = ttk.Combobox(
            master=self
        )
        # Pipe Type
        self.pipetype_label = ttk.Label(
            master=self,
            text="Pipe Type:"
        )
        self.pipetype_combo = ttk.Combobox(
            master=self 
        )

    def __ui_layout(self):
        widgets = (
            (self.pipenum_label, self.pipenum_spin),
            (self.keyboardnote_label, self.keyboardnote_combo),
            (self.realnote_label, self.realnote_combo),
            (self.pipetype_label, self.pipetype_combo)
        )
        for r, row in enumerate(widgets):
            for c, widget in enumerate(row):
                widget.grid(
                    column=c,
                    row=r,
                    padx=4,
                    pady=4,
                    sticky="nsew"
                )


class SettingsHarmonic(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__ui_widgets()
        self.__ui_layout()

    def __ui_widgets(self):
        # Harmonic Number
        self.harmonicnum_label = ttk.Label(
            master=self,
            text="Harmonic #:"
        )
        self.harmonicnum_spin = ttk.Spinbox(
            master=self
        )
        # Amplitude
        self.amplitude_label = ttk.Label(
            master=self,
            text="Amplitude:"
        )
        self.amplitude_spin = ttk.Spinbox(
            master=self
        )
        # Amplitude Adjustment
        self.ampadjust_label = ttk.Label(
            master=self,
            text="Amplitude Adjustment (ADSR ATTACK PHASE):"
        )
        self.ampadjust_spin = ttk.Spinbox(
            master=self
        )
        # Amplitude Adjustment Scale
        self.ampadjustscale_label = ttk.Label(
            master=self,
            text="Amplitude Adjustment Scale:"
        )
        self.ampadjustscale_spin = ttk.Spinbox(
            master=self
        )

    def __ui_layout(self):
        widgets = (
            (self.harmonicnum_label, self.harmonicnum_spin),
            (self.amplitude_label, self.amplitude_spin),
            (self.ampadjust_label, self.ampadjust_spin),
            (self.ampadjustscale_label, self.ampadjustscale_spin)
        )
        for r, row in enumerate(widgets):
            for c, widget in enumerate(row):
                widget.grid(
                    column=c,
                    row=r,
                    padx=4,
                    pady=4,
                    sticky="nsew"
                )


class SettingsADSR(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.__ui_widgets()
        self.__ui_layout()

    def __ui_widgets(self):
        # Attack Time
        self.attack_label = ttk.Label(
            master=self,
            text="Attack Time (s):"
        )
        self.attack_spin = ttk.Spinbox(
            master=self
        )
        # Decay Time
        self.decay_label = ttk.Label(
            master=self,
            text="Decay Time (s):"
        )
        self.decay_spin = ttk.Spinbox(
            master=self
        )
        # Sustain Level
        self.sustain_label = ttk.Label(
            master=self,
            text="Sustain Level (%):"
        )
        self.sustain_spin = ttk.Spinbox(
            master=self
        )
        # Release Time
        self.release_label = ttk.Label(
            master=self,
            text="Release Time (s):"
        )
        self.release_spin = ttk.Spinbox(
            master=self
        )

    def __ui_layout(self):
        widgets = (
            (self.attack_label, self.attack_spin),
            (self.decay_label, self.decay_spin),
            (self.sustain_label, self.sustain_spin),
            (self.release_label, self.release_spin)
        )
        for r, row in enumerate(widgets):
            for c, widget in enumerate(row):
                widget.grid(
                    column=c,
                    row=r,
                    padx=4,
                    pady=4,
                    sticky="nsew"
                )
