"""Stop Editor"""
from organ import organlib
#-----------------------------------------------------------------------------------------------------------------------
from typing import Callable
#-----------------------------------------------------------------------------------------------------------------------
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QWidget,
    QScrollArea,
    QScrollBar,
    QGroupBox,
    QLabel,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QPushButton,
    QCheckBox,
    QFormLayout,
    QHBoxLayout,
    QVBoxLayout
)
from PySide6.QtCore import Qt
from icecream import ic  # type: ignore


#=======================================================================================================================
class StopEditor(QFrame):
    def __init__(self) -> None:
        ic("Initializing Stop Editor...")
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        #self.__ui_layout()
        self.__rank_harmonics_checked()
        self.__rank_adsr_checked()
        self.__pipe_harmonics_checked()
        self.__pipe_adsr_checked()
        ic("Stop Editor Initialized.")

    #===================================================================================================================
    # Widgets
    #===================================================================================================================
    def __init_ui(self) -> None:
        ic("Initializing Widgets...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__init_ui_header()
        self.__init_ui_editor()
        self.__init_ui_options()
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout_editor: QVBoxLayout = QVBoxLayout()
        ic(layout_editor)
        widgets: tuple[QWidget, ...] = (
            self.__header_widget,
            self.__editor_scroll
        )
        ic(widgets)
        for widget in widgets:
            ic(widget)
            layout_editor.addWidget(widget)
            ic(f"{widget} added to {layout_editor}")
        layout: QHBoxLayout = QHBoxLayout()
        ic(layout)
        layout.addLayout(layout_editor)
        layout.addWidget(self.__options_widget)
        ic(f"{self.__options_widget} added to {layout}")
        self.setLayout(layout)
        ic(self.layout())
        ic("Layout Created.")
        ic("Widgets Initialized.")

    #*******************************************************************************************************************
    # Header
    #*******************************************************************************************************************
    def __init_ui_header(self) -> None:
        ic("Initializing Header...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__header_widget: QWidget = QWidget()
        ic(self.__header_widget)
        self.__header_label: QLabel = QLabel("Stop:")
        ic(self.__header_label)
        self.__header_edit: QLineEdit = QLineEdit()
        ic(self.__header_edit)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QHBoxLayout = QHBoxLayout()
        ic(layout)
        widgets: tuple[QWidget, ...] = (
            self.__header_label,
            self.__header_edit
        )
        ic(widgets)
        for widget in widgets:
            ic(widget)
            layout.addWidget(widget)
            ic(f"{widget} added to {layout}")
        self.__header_widget.setLayout(layout)
        ic(self.__header_widget.layout())
        ic("Layout Created.")
        ic("Header Initialized.")

    #*******************************************************************************************************************
    # Editor
    #*******************************************************************************************************************
    def __init_ui_editor(self) -> None:
        ic("Initializing Editor...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__editor_scroll: QScrollArea = QScrollArea()
        ic(self.__editor_scroll)
        self.__editor_scroll.setWidgetResizable(True)
        self.__editor_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        ic(self.__editor_scroll.verticalScrollBarPolicy())
        self.__editor_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        ic(self.__editor_scroll.horizontalScrollBarPolicy())
        self.__editor_scroll.setVerticalScrollBar(QScrollBar())
        ic(self.__editor_scroll.verticalScrollBar())
        self.__editor_widget: QWidget = QWidget()
        ic(self.__editor_widget)
        self.__init_ui_stop_settings()
        self.__init_ui_rank_settings()
        self.__init_ui_pipe_settings()
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QVBoxLayout = QVBoxLayout()
        ic(layout)
        widgets: tuple[QWidget, ...] = (
            self.__stop_settings_group,
            self.__rank_settings_group,
            self.__pipe_settings_group
        )
        ic(widgets)
        for widget in widgets:
            ic(widget)
            layout.addWidget(widget)
            ic(f"{widget} added to {layout}")
            layout.addSpacing(10)
        self.__editor_widget.setLayout(layout)
        ic(self.__editor_widget.layout())
        self.__editor_scroll.setWidget(self.__editor_widget)
        ic(self.__editor_scroll.widget())
        ic("Layout Created.")
        ic("Editor Initialized.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Stop Settings
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init_ui_stop_settings(self) -> None:
        ic("Initializing Stop Settings...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__stop_settings_group: QGroupBox = QGroupBox("Stop Settings")
        ic(self.__stop_settings_group)
        # Stop Name
        self.__stop_name_label: QLabel = QLabel("Stop Name:")
        ic(self.__stop_name_label)
        self.__stop_name_combo: QComboBox = QComboBox()
        ic(self.__stop_name_combo)
        # Stop Family
        self.__stop_family_label: QLabel = QLabel("Stop Family:")
        ic(self.__stop_family_label)
        self.__stop_family_combo = QComboBox()
        ic(self.__stop_family_combo)
        # Organ Division
        self.__organ_division_label: QLabel = QLabel("Organ Division:")
        ic(self.__organ_division_label)
        self.__organ_division_combo: QComboBox = QComboBox()
        ic(self.__organ_division_combo)
        # Number of Ranks
        self.__number_ranks_label: QLabel = QLabel("Number of Ranks:")
        ic(self.__number_ranks_label)
        self.__number_ranks_spin: QSpinBox = QSpinBox()
        ic(self.__number_ranks_spin)
        # Rank Series
        self.__rank_series_label: QLabel = QLabel("Rank Series:")
        ic(self.__rank_series_label)
        self.__rank_series_combo: QComboBox = QComboBox()
        ic(self.__rank_series_combo)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QFormLayout = QFormLayout()
        ic(layout)
        widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__stop_name_label, self.__stop_name_combo),
            (self.__stop_family_label, self.__stop_family_combo),
            (self.__organ_division_label, self.__organ_division_combo),
            (self.__number_ranks_label, self.__number_ranks_spin),
            (self.__rank_series_label, self.__rank_series_combo)
        )
        ic(widgets)
        for label, widget in widgets:
            ic(label, widget)
            layout.addRow(label, widget)
            ic(f"{label} and {widget} added to {layout}")
        self.__stop_settings_group.setLayout(layout)
        ic(self.__stop_settings_group.layout())
        ic("Layout Created.")
        ic("Stop Settings Initialized.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Rank Settings
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init_ui_rank_settings(self) -> None:
        ic("Initializing Rank Settings...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__rank_settings_group: QGroupBox = QGroupBox("Rank Settings")
        ic(self.__rank_settings_group)
        self.__init_ui_rank_settings_header()
        self.__rank_harmonics_button: QCheckBox = QCheckBox("Edit Harmonics")
        ic(self.__rank_harmonics_button)
        self.__init_ui_rank_harmonics_settings()
        self.__rank_harmonics_adsr_button: QCheckBox = QCheckBox("Edit Harmonics ADSR")
        ic(self.__rank_harmonics_adsr_button)
        self.__init_ui_rank_harmonics_adsr_settings()
        self.__rank_adsr_button: QCheckBox = QCheckBox("Edit ADSR")
        ic(self.__rank_adsr_button)
        self.__init_ui_rank_adsr_settings()
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QVBoxLayout = QVBoxLayout()
        ic(layout)
        widgets: tuple[QWidget, ...] = (
            self.__rank_settings_header_widget,
            self.__rank_harmonics_button,
            self.__rank_harmonics_group,
            self.__rank_harmonics_adsr_button,
            self.__rank_harmonics_adsr_group,
            self.__rank_adsr_button,
            self.__rank_adsr_group
        )
        ic(widgets)
        for widget in widgets:
            ic(widget)
            layout.addWidget(widget)
            ic(f"{widget} added to {layout}")
            layout.addSpacing(10)
        self.__rank_settings_group.setLayout(layout)
        ic(self.__rank_settings_group.layout())
        ic("Layout Created.")

    #-------------------------------------------------------------------------------------------------------------------
    def __init_ui_rank_settings_header(self) -> None:
        ic("Initializing Rank Settings Header...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__rank_settings_header_widget: QWidget = QWidget()
        # Rank Number
        self.__rank_number_label: QLabel = QLabel("Rank #:")
        ic(self.__rank_number_label)
        self.__rank_number_spin: QSpinBox = QSpinBox()
        ic(self.__rank_number_spin)
        # Rank Size
        self.__rank_size_label: QLabel = QLabel("Rank Size:")
        ic(self.__rank_size_label)
        self.__rank_size_combo = QComboBox()
        ic(self.__rank_size_combo)
        # Number of Pipes
        self.__number_pipes_label: QLabel = QLabel("Number of Pipes:")
        ic(self.__number_pipes_label)
        self.__number_pipes_spin: QSpinBox = QSpinBox()
        ic(self.__number_pipes_spin)
        # Pipe Type
        self.__pipe_type_label: QLabel = QLabel("PipeType:")
        ic(self.__pipe_type_label)
        self.__pipe_type_combo: QComboBox = QComboBox()
        ic(self.__pipe_type_combo)
        # Starting Note
        self.__starting_note_label: QLabel = QLabel("Starting Note:")
        ic(self.__starting_note_label)
        self.__starting_note_combo: QComboBox = QComboBox()
        ic(self.__starting_note_combo)
        # Frequency Offset
        self.__frequency_offset_label: QLabel = QLabel("Frequency Offset (Hz):")
        ic(self.__frequency_offset_label)
        self.__frequency_offset_spin: QSpinBox = QSpinBox()
        ic(self.__frequency_offset_spin)
        # Number of Harmonics
        self.__number_harmonics_label: QLabel = QLabel("Number of Harmonics:")
        ic(self.__number_harmonics_label)
        self.__number_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__number_harmonics_spin)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QFormLayout = QFormLayout()
        ic(layout)
        widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__rank_number_label, self.__rank_number_spin),
            (self.__rank_size_label, self.__rank_size_combo),
            (self.__pipe_type_label, self.__pipe_type_combo),
            (self.__starting_note_label, self.__starting_note_combo),
            (self.__frequency_offset_label, self.__frequency_offset_spin),
            (self.__number_pipes_label, self.__number_pipes_spin),
            (self.__number_harmonics_label, self.__number_harmonics_spin)
        )
        ic(widgets)
        for label, widget in widgets:
            ic(label, widget)
            layout.addRow(label, widget)
            ic(f"{label} and {widget} added to {layout}")
        self.__rank_settings_header_widget.setLayout(layout)
        ic(self.__rank_settings_header_widget.layout())
        ic("Rank Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def __init_ui_rank_harmonics_settings(self) -> None:
        ic("Initializing Rank Harmonics Settings...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__rank_harmonics_group: QGroupBox = QGroupBox("Harmonic Settings - Rank")
        ic(self.__rank_harmonics_group)
        # Harmonic Number
        self.__harmonic_number_rank_label: QLabel = QLabel("Harmonic #:")
        ic(self.__harmonic_number_rank_label)
        self.__harmonic_number_rank_spin: QSpinBox = QSpinBox()
        ic(self.__harmonic_number_rank_spin)
        # Amplitude
        self.__amplitude_rank_label: QLabel = QLabel("Amplitude (%):")
        ic(self.__amplitude_rank_label)
        self.__amplitude_rank_spin: QSpinBox = QSpinBox()
        ic(self.__amplitude_rank_spin)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QFormLayout = QFormLayout()
        ic(layout)
        widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__harmonic_number_rank_label, self.__harmonic_number_rank_spin),
            (self.__amplitude_rank_label, self.__amplitude_rank_spin)
        )
        ic(widgets)
        for label, widget in widgets:
            ic(label, widget)
            layout.addRow(label, widget)
            ic(f"{label} and {widget} added to {layout}")
        self.__rank_harmonics_group.setLayout(layout)
        ic(self.__rank_harmonics_group.layout())
        ic("Layout Created.")
        ic("Rank Harmonics Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def __init_ui_rank_harmonics_adsr_settings(self) -> None:
        ic("Initializing Rank Harmonic ADSR Settings...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__rank_harmonics_adsr_group: QGroupBox = QGroupBox("Harmonic ADSR Settings - Rank")
        ic(self.__rank_harmonics_adsr_group)
        # Attack
        self.__attack_time_rank_harmonics_label: QLabel = QLabel("Attack Time (ms):")
        ic(self.__attack_time_rank_harmonics_label)
        self.__attack_time_rank_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__attack_time_rank_harmonics_spin)
        # Decay
        self.__decay_time_rank_harmonics_label: QLabel = QLabel("Decay Time (ms):")
        ic(self.__decay_time_rank_harmonics_label)
        self.__decay_time_rank_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__decay_time_rank_harmonics_spin)
        # Sustain
        self.__sustain_level_rank_harmonics_label: QLabel = QLabel("Sustain Level (%):")
        ic(self.__sustain_level_rank_harmonics_label)
        self.__sustain_level_rank_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__sustain_level_rank_harmonics_spin)
        # Release
        self.release_time_rank_harmonics_label: QLabel = QLabel("Release Time (ms):")
        ic(self.release_time_rank_harmonics_label)
        self.__release_time_rank_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__release_time_rank_harmonics_spin)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QFormLayout = QFormLayout()
        ic(layout)
        widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__attack_time_rank_harmonics_label, self.__attack_time_rank_harmonics_spin),
            (self.__decay_time_rank_harmonics_label, self.__decay_time_rank_harmonics_spin),
            (self.__sustain_level_rank_harmonics_label, self.__sustain_level_rank_harmonics_spin),
            (self.release_time_rank_harmonics_label, self.__release_time_rank_harmonics_spin)
        )
        ic(widgets)
        for label, widget in widgets:
            ic(label, widget)
            layout.addRow(label, widget)
            ic(f"{label} and {widget} added to {layout}")
        self.__rank_harmonics_adsr_group.setLayout(layout)
        ic(self.__rank_harmonics_adsr_group.layout())
        ic("Layout Created.")
        ic("Rank Harmonic ADSR Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def __init_ui_rank_adsr_settings(self) -> None:
        ic("Initializing Rank ADSR Settings...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__rank_adsr_group: QGroupBox = QGroupBox("ADSR Settings - Rank")
        ic(self.__rank_adsr_group)
        # Attack
        self.__attack_time_rank_label: QLabel = QLabel("Attack Time (ms):")
        ic(self.__attack_time_rank_label)
        self.__attack_time_rank_spin: QSpinBox = QSpinBox()
        ic(self.__attack_time_rank_spin)
        # Decay
        self.__decay_time_rank_label: QLabel = QLabel("Decay Time (ms):")
        ic(self.__decay_time_rank_label)
        self.__decay_time_rank_spin: QSpinBox = QSpinBox()
        ic(self.__decay_time_rank_spin)
        # Sustain
        self.__sustain_level_rank_label: QLabel = QLabel("Sustain Level (%):")
        ic(self.__sustain_level_rank_label)
        self.__sustain_level_rank_spin: QSpinBox = QSpinBox()
        ic(self.__sustain_level_rank_spin)
        # Release
        self.__release_time_rank_label: QLabel = QLabel("Release Time (ms):")
        ic(self.__release_time_rank_label)
        self.__release_time_rank_spin: QSpinBox = QSpinBox()
        ic(self.__release_time_rank_spin)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QFormLayout = QFormLayout()
        ic(layout)
        widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__attack_time_rank_label, self.__attack_time_rank_spin),
            (self.__decay_time_rank_label, self.__decay_time_rank_spin),
            (self.__sustain_level_rank_label, self.__sustain_level_rank_spin),
            (self.__release_time_rank_label, self.__release_time_rank_spin)
        )
        ic(widgets)
        for label, widget in widgets:
            ic(label, widget)
            layout.addRow(label, widget)
            ic(f"{label} and {widget} added to {layout}")
        self.__rank_adsr_group.setLayout(layout)
        ic(self.__rank_adsr_group.layout())
        ic("Rank ADSR Settings Initialized.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Pipe Settings
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def __init_ui_pipe_settings(self) -> None:
        ic("Initializing Pipe Settings...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__pipe_settings_group: QGroupBox = QGroupBox("Pipe Settings")
        ic(self.__pipe_settings_group)
        self.__init_ui_pipe_settings_header()
        self.__pipe_harmonics_button: QCheckBox = QCheckBox("Edit Harmonics")
        ic(self.__pipe_harmonics_button)
        self.__init_ui_pipe_harmonics_settings()
        self.__pipe_harmonics_adsr_button: QCheckBox = QCheckBox("Edit Harmonics ADSR")
        ic(self.__pipe_harmonics_adsr_button)
        self.__init_ui_pipe_harmonic_adsr_settings()
        self.__pipe_adsr_button: QCheckBox = QCheckBox("Edit ADSR")
        ic(self.__pipe_adsr_button)
        self.__init_ui_pipe_adsr_settings()
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QVBoxLayout = QVBoxLayout()
        ic(layout)
        widgets: tuple[QWidget, ...] = (
            self.__pipe_settings_header,
            self.__pipe_harmonics_button,
            self.__pipe_harmonics_group,
            self.__pipe_harmonics_adsr_button,
            self.__pipe_harmonics_adsr_group,
            self.__pipe_adsr_button,
            self.__pipe_adsr_group
        )
        ic(widgets)
        for widget in widgets:
            ic(widget)
            layout.addWidget(widget)
            ic(f"{widget} added to {layout}")
            layout.addSpacing(10)
        self.__pipe_settings_group.setLayout(layout)
        ic(self.__pipe_settings_group.layout())
        ic("Layout Created.")
        ic("Pipe Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def __init_ui_pipe_settings_header(self) -> None:
        ic("Initializing Pipe Settings Header...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__pipe_settings_header: QWidget = QWidget()
        ic(self.__pipe_settings_header)
        # Rank Number
        self.__rank_number_pipe_label: QLabel = QLabel("Rank #:")
        ic(self.__rank_number_pipe_label)
        self.__rank_number_pipe_spin: QSpinBox = QSpinBox()
        ic(self.__rank_number_pipe_spin)
        # Pipe #
        self.__pipe_number_label: QLabel = QLabel("Pipe #:")
        ic(self.__pipe_number_label)
        self.__pipe_number_spin: QSpinBox = QSpinBox()
        ic(self.__pipe_number_spin)        
        # Note
        self.__note_label: QLabel = QLabel("Note:")
        ic(self.__note_label)
        self.__note_combo: QComboBox = QComboBox()
        ic(self.__note_combo)
        # Relative Note
        self.__relative_note_label: QLabel = QLabel("Relative Note:")
        ic(self.__relative_note_label)
        self.__relative_note_combo: QComboBox = QComboBox()
        ic(self.__relative_note_combo)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QFormLayout = QFormLayout()
        ic(layout)
        widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__rank_number_pipe_label, self.__rank_number_pipe_spin),
            (self.__pipe_number_label, self.__pipe_number_spin),
            (self.__note_label, self.__note_combo),
            (self.__relative_note_label, self.__relative_note_combo)
        )
        ic(widgets)
        for label, widget in widgets:
            ic(label, widget)
            layout.addRow(label, widget)
            ic(f"{label} and {widget} added to {layout}")
        self.__pipe_settings_header.setLayout(layout)
        ic(self.__pipe_settings_header.layout())
        ic("Pipe Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def __init_ui_pipe_harmonics_settings(self) -> None:
        ic("Initializing Pipe Harmonics Settings...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__pipe_harmonics_group: QGroupBox = QGroupBox("Harmonic Settings - Pipe")
        ic(self.__pipe_harmonics_group)
        # Harmonic #
        self.__harmonic_number_pipe_label: QLabel = QLabel("Harmonic #:")
        ic(self.__harmonic_number_pipe_label)
        self.__harmonic_number_pipe_spin: QSpinBox = QSpinBox()
        ic(self.__harmonic_number_pipe_spin)
        # Amplitude
        self.__amplitude_pipe_label: QLabel = QLabel("Amplitude (%):")
        ic(self.__amplitude_pipe_label)
        self.__amplitude_pipe_spin: QSpinBox = QSpinBox()
        ic(self.__amplitude_pipe_spin)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QFormLayout = QFormLayout()
        ic(layout)
        widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__harmonic_number_pipe_label, self.__harmonic_number_pipe_spin),
            (self.__amplitude_pipe_label, self.__amplitude_pipe_spin)
        )
        ic(widgets)
        for label, widget in widgets:
            ic(label, widget)
            layout.addRow(label, widget)
            ic(f"{label} and {widget} added to {layout}")
        self.__pipe_harmonics_group.setLayout(layout)
        ic(self.__pipe_harmonics_group.layout())
        ic("Layout Created.")
        ic("Pipe Harmonics Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def __init_ui_pipe_harmonic_adsr_settings(self) -> None:
        ic("Initializing Pipe Harmonic ADSR Settings...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        # Harmonic ADSR Group
        self.__pipe_harmonics_adsr_group: QGroupBox = QGroupBox("Harmonic ADSR Settings - Pipe")
        ic(self.__pipe_harmonics_adsr_group)
        # Attack
        self.__attack_time_pipe_harmonics_label: QLabel = QLabel("Attack Time (ms):")
        ic(self.__attack_time_pipe_harmonics_label)
        self.__attack_time_pipe_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__attack_time_pipe_harmonics_spin)
        # Decay
        self.__decay_time_pipe_harmonics_label: QLabel = QLabel("Decay Time (ms):")
        ic(self.__decay_time_pipe_harmonics_label)
        self.__decay_time_pipe_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__decay_time_pipe_harmonics_spin)
        # Sustain
        self.__sustain_level_pipe_harmonics_label: QLabel = QLabel("Sustain Level (%):")
        ic(self.__sustain_level_pipe_harmonics_label)
        self.__sustain_level_pipe_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__sustain_level_pipe_harmonics_spin)
        # Release
        self.__release_time_pipe_harmonics_label: QLabel = QLabel("Release Time (ms):")
        ic(self.__release_time_pipe_harmonics_label)
        self.__release_time_pipe_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__release_time_pipe_harmonics_spin)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QFormLayout = QFormLayout()
        ic(layout)
        widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__attack_time_pipe_harmonics_label, self.__attack_time_pipe_harmonics_spin),
            (self.__decay_time_pipe_harmonics_label, self.__decay_time_pipe_harmonics_spin),
            (self.__sustain_level_pipe_harmonics_label, self.__sustain_level_pipe_harmonics_spin),
            (self.__release_time_pipe_harmonics_label, self.__release_time_pipe_harmonics_spin)
        )
        ic(widgets)
        for label, widget in widgets:
            ic(label, widget)
            layout.addRow(label, widget)
            ic(f"{label} and {widget} added to {layout}")
        self.__pipe_harmonics_adsr_group.setLayout(layout)
        ic(self.__pipe_harmonics_adsr_group.layout())
        ic("Layout Created.")
        ic("Pipe Harmonic ADSR Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def __init_ui_pipe_adsr_settings(self) -> None:
        ic("Initializing Pipe ADSR Settings...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__pipe_adsr_group: QGroupBox = QGroupBox("ADSR Settings - Pipe")
        ic(self.__pipe_adsr_group)
        # Attack
        self.__attack_time_pipe_label: QLabel = QLabel("Attack Time (ms):")
        ic(self.__attack_time_pipe_label)
        self.__attack_time_pipe_spin: QSpinBox = QSpinBox()
        ic(self.__attack_time_pipe_spin)
        # Decay
        self.__decay_time_pipe_label: QLabel = QLabel("Decay Time (ms):")
        ic(self.__decay_time_pipe_label)
        self.__decay_time_pipe_spin: QSpinBox = QSpinBox()
        ic(self.__decay_time_pipe_spin)
        # Sustain
        self.__sustain_level_pipe_label: QLabel = QLabel("Sustain Level (%):")
        ic(self.__sustain_level_pipe_label)
        self.__sustain_level_pipe_spin: QSpinBox = QSpinBox()
        ic(self.__sustain_level_pipe_spin)
        # Release
        self.__release_time_pipe_label: QLabel = QLabel("Release Time (ms):")
        ic(self.__release_time_pipe_label)
        self.__release_time_pipe_spin: QSpinBox = QSpinBox()
        ic(self.__release_time_pipe_spin)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QFormLayout = QFormLayout()
        ic(layout)
        widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__attack_time_pipe_label, self.__attack_time_pipe_spin),
            (self.__decay_time_pipe_label, self.__decay_time_pipe_spin),
            (self.__sustain_level_pipe_label, self.__sustain_level_pipe_spin),
            (self.__release_time_pipe_label, self.__release_time_pipe_spin)
        )
        ic(widgets)
        for label, widget in widgets:
            ic(label, widget)
            layout.addRow(label, widget)
            ic(f"{label} and {widget} added to {layout}")
        self.__pipe_adsr_group.setLayout(layout)
        ic(self.__pipe_adsr_group.layout())
        ic("Layout Created.")
        ic("Pipe ADSR Settings Initialized.")

    #*******************************************************************************************************************
    # Options
    #*******************************************************************************************************************
    def __init_ui_options(self) -> None:
        ic("Initializing Options...")
        #---------------------------------------------------------------------------------------------------------------
        # Widgets
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Widgets...")
        self.__options_widget: QWidget = QWidget()
        ic(self.__options_widget)
        self.__load_button: QPushButton = QPushButton("Load Stop")
        ic(self.__load_button)
        self.__cancel_button: QPushButton = QPushButton("Cancel Changes")
        ic(self.__cancel_button)
        self.__save_button: QPushButton = QPushButton("Save Stop")
        ic(self.__save_button)
        ic("Widgets Created.")
        #---------------------------------------------------------------------------------------------------------------
        # Layout
        #---------------------------------------------------------------------------------------------------------------
        ic("Creating Layout...")
        layout: QVBoxLayout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        ic(layout)
        widgets: tuple[QWidget, ...] = (
            self.__load_button,
            self.__cancel_button,
            self.__save_button
        )
        ic(widgets)
        for widget in widgets:
            ic(widget)
            layout.addWidget(widget)
            ic(f"{widget} added to {layout}")
        self.__options_widget.setLayout(layout)
        ic(self.__options_widget.layout())
        ic("Layout Created.")
        ic("Options Initialized.")

    #===================================================================================================================
    # Settings
    #===================================================================================================================
    def __ui_settings(self) -> None:
        ic("Setting Up Widgets...")
        self.setWindowTitle("pyOrgan - Stop Editor")
        ic(self.windowTitle())
        self.__ui_settings_header()
        self.__ui_settings_editor()
        ic("Widgets Settings Complete.")

    #*******************************************************************************************************************
    # Header
    #*******************************************************************************************************************
    def __ui_settings_header(self) -> None:
        ic("Setting Up Header...")
        self.__header_edit.setReadOnly(True)
        ic(self.__header_edit.isReadOnly())
        self.__header_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ic(self.__header_edit.alignment())
        ic("Header Settings Complete.")

    #*******************************************************************************************************************
    # Editor
    #*******************************************************************************************************************
    def __ui_settings_editor(self) -> None:
        ic("Setting Up Editor...")
        self.__ui_settings_editor_groupboxes()
        self.__ui_settings_editor_labels()
        self.__ui_settings_editor_comboboxes()
        self.__ui_settings_editor_spinboxes()
        self.__ui_settings_editor_checkboxes()
        ic("Editor Settings Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __ui_settings_editor_groupboxes(self) -> None:
        ic("Setting Up Group Boxes...")
        group_boxes: tuple[QGroupBox, ...] = (
            self.__stop_settings_group,
            self.__rank_settings_group,
            self.__pipe_settings_group,
            self.__rank_harmonics_group,
            self.__pipe_harmonics_group,
            self.__rank_harmonics_adsr_group,
            self.__rank_adsr_group,
            self.__pipe_harmonics_adsr_group,
            self.__pipe_adsr_group
        )
        ic(group_boxes)
        for group_box in group_boxes:
            ic(group_box)
            group_box.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
            ic(group_box.alignment())
        top_level: tuple[QGroupBox, ...] = (
            self.__stop_settings_group,
            self.__rank_settings_group,
            self.__pipe_settings_group
        )
        ic(top_level)
        for group_box in top_level:
            ic(group_box)
            group_box.setFixedWidth(270)
            ic(group_box.width())
        ic("Group Boxes Settings Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __ui_settings_editor_labels(self) -> None:
        ic("Setting Up Labels...")
        labels: tuple[QLabel, ...] = (
            self.__stop_name_label,
            self.__stop_family_label,
            self.__organ_division_label,
            self.__number_ranks_label,
            self.__rank_series_label,
            self.__rank_number_label,
            self.__rank_size_label,
            self.__number_pipes_label,
            self.__starting_note_label,
            self.__pipe_type_label,
            self.__frequency_offset_label,
            self.__number_harmonics_label,
            self.__harmonic_number_rank_label,
            self.__amplitude_rank_label,
            self.__attack_time_rank_harmonics_label,
            self.__decay_time_rank_harmonics_label,
            self.__sustain_level_rank_harmonics_label,
            self.release_time_rank_harmonics_label,
            self.__attack_time_rank_label,
            self.__decay_time_rank_label,
            self.__sustain_level_rank_label,
            self.__release_time_rank_label,
            self.__rank_number_pipe_label,
            self.__pipe_number_label,
            self.__note_label,
            self.__relative_note_label,
            self.__harmonic_number_pipe_label,
            self.__amplitude_pipe_label,
            self.__attack_time_pipe_harmonics_label,
            self.__decay_time_pipe_harmonics_label,
            self.__sustain_level_pipe_harmonics_label,
            self.__release_time_pipe_harmonics_label,
            self.__attack_time_pipe_label,
            self.__decay_time_pipe_label,
            self.__sustain_level_pipe_label,
            self.__release_time_pipe_label
        )
        ic(labels)
        for label in labels:
            ic(label)
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            ic(label.alignment())
        ic("Labels Settings Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __ui_settings_editor_comboboxes(self) -> None:
        ic("Setting Up Combo Boxes...")
        #---------------------------------------------------------------------------------------------------------------
        # General ComboBox Settings
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up General ComboBox Settings...")
        comboboxes: tuple[QComboBox, ...] = (
            self.__stop_name_combo,
            self.__stop_family_combo,
            self.__organ_division_combo,
            self.__rank_series_combo,
            self.__rank_size_combo,
            self.__pipe_type_combo,
            self.__starting_note_combo,
            self.__note_combo,
            self.__relative_note_combo,
        )
        ic(comboboxes)
        for widget in comboboxes:
            ic(widget)
            widget.setEditable(True)
            ic(widget.isEditable())
            edit: QLineEdit = widget.lineEdit() # type: ignore
            ic(edit)
            edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            ic(edit.alignment())
            if widget == self.__stop_name_combo:
                edit.setReadOnly(False)
            else:
                edit.setReadOnly(True)
            ic(edit.isReadOnly())
        ic("General ComboBox Settings Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Stop Name ComboBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Stop Name ComboBox...")
        stop_names: tuple[str, ...] = ("",) + organlib.STOP_NAMES
        ic(stop_names)
        self.__stop_name_combo.addItems(stop_names)
        ic(f"{stop_names} added to {self.__stop_name_combo}")
        ic("Stop Name ComboBox Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Stop Family ComboBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Stop Family ComboBox...")
        stop_families: tuple[str, ...] = ("",) + organlib.STOP_FAMILIES
        ic(stop_families)
        self.__stop_family_combo.addItems(stop_families)
        ic(f"{stop_families} added to {self.__stop_family_combo}")
        ic("Stop Family ComboBox Set Up Complete.")
        self.__note_combo.setEnabled(False)
        ic(self.__note_combo.isEnabled())
        ic("Combo Boxes Settings Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Organ Division ComboBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Organ Division ComboBox...")
        organ_divisions: tuple[str, ...] = ("",) + organlib.ORGAN_DIVISIONS
        ic(organ_divisions)
        self.__organ_division_combo.addItems(organ_divisions)
        ic(f"{organ_divisions} added to {self.__organ_division_combo}")
        ic("Organ Division ComboBox Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Rank Series ComboBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Rank Series ComboBox...")
        rank_series: tuple[str, ...] = ("",) + organlib.RANK_SERIES
        ic(rank_series)
        self.__rank_series_combo.addItems(rank_series)
        ic(f"{rank_series} added to {self.__rank_series_combo}")
        ic("Rank Series ComboBox Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Rank Size ComboBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Rank Size ComboBox...")
        rank_sizes: tuple[str, ...] = ("",) + organlib.RANK_SIZES
        ic(rank_sizes)
        self.__rank_size_combo.addItems(rank_sizes)
        ic(f"{rank_sizes} added to {self.__rank_size_combo}")
        ic("Rank Size ComboBox Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Pipe Type ComboBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Pipe Type ComboBox...")
        pipe_types: tuple[str, ...] = ("",) + organlib.PIPE_TYPES
        ic(pipe_types)
        self.__pipe_type_combo.addItems(pipe_types)
        ic(f"{pipe_types} added to {self.__pipe_type_combo}")
        ic("Pipe Type ComboBox Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Note ComboBoxes
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Note ComboBoxes...")
        notes: tuple[str, ...] = ("",) + organlib.NOTES
        ic(notes)
        note_combos: tuple[QComboBox, ...] = (
            self.__starting_note_combo,
            self.__note_combo,
            self.__relative_note_combo
        )
        ic(note_combos)
        for widget in note_combos:
            ic(widget)
            widget.addItems(notes)
            ic(f"{notes} added to {widget}")
        ic("Note ComboBoxes Set Up Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __ui_settings_editor_spinboxes(self) -> None:
        ic("Setting Up Spin Boxes...")
        #---------------------------------------------------------------------------------------------------------------
        # General SpinBox Settings
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up General SpinBox Settings...")
        spin_boxes: tuple[QSpinBox, ...] = (
            self.__number_ranks_spin,
            self.__rank_number_spin,
            self.__number_pipes_spin,
            self.__frequency_offset_spin,
            self.__number_harmonics_spin,
            self.__harmonic_number_rank_spin,
            self.__amplitude_rank_spin,
            self.__attack_time_rank_harmonics_spin,
            self.__decay_time_rank_harmonics_spin,
            self.__sustain_level_rank_harmonics_spin,
            self.__release_time_rank_harmonics_spin,
            self.__attack_time_rank_spin,
            self.__decay_time_rank_spin,
            self.__sustain_level_rank_spin,
            self.__release_time_rank_spin,
            self.__rank_number_pipe_spin,
            self.__pipe_number_spin,
            self.__harmonic_number_pipe_spin,
            self.__amplitude_pipe_spin,
            self.__attack_time_pipe_harmonics_spin,
            self.__decay_time_pipe_harmonics_spin,
            self.__sustain_level_pipe_harmonics_spin,
            self.__release_time_pipe_harmonics_spin,
            self.__attack_time_pipe_spin,
            self.__decay_time_pipe_spin,
            self.__sustain_level_pipe_spin,
            self.__release_time_pipe_spin
        )
        ic(spin_boxes)
        for spin_box in spin_boxes:
            ic(spin_box)
            spin_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            ic(spin_box.alignment())
        ic("General SpinBox Settings Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Number of Ranks SpinBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Number of Ranks SpinBox...")
        self.__number_ranks_spin.setRange(1, 10)
        ic(f"{self.__number_ranks_spin.minimum()} to {self.__number_ranks_spin.maximum()}")
        ic("Spin Boxes Settings Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Rank, Pipe, Harmonic Number SpinBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Rank, Pipe, Harmonic Number SpinBox...")
        number_spins: tuple[QSpinBox, ...] = (
            self.__rank_number_spin,
            self.__pipe_number_spin,
            self.__harmonic_number_rank_spin,
            self.__harmonic_number_pipe_spin
        )
        ic(number_spins)
        for spin_box in number_spins:
            ic(spin_box)
            spin_box.setMinimum(1)
            ic(spin_box.minimum())
        ic("Rank Number SpinBox Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Number of Pipes SpinBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Number of Pipes SpinBox...")
        self.__number_pipes_spin.setRange(1, 61)
        ic(f"{self.__number_pipes_spin.minimum()} to {self.__number_pipes_spin.maximum()}")
        ic("Number of Pipes SpinBox Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Frequency Offset SpinBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Frequency Offset SpinBox...")
        self.__frequency_offset_spin.setRange(-7, 7)
        ic(f"{self.__frequency_offset_spin.minimum()} to {self.__frequency_offset_spin.maximum()}")
        ic("Frequency Offset SpinBox Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Number of Harmonics SpinBox
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Number of Harmonics SpinBox...")
        self.__number_harmonics_spin.setRange(1, 20)
        ic(f"{self.__number_harmonics_spin.minimum()} to {self.__number_harmonics_spin.maximum()}")
        ic("Number of Harmonics SpinBox Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Amplitude and Level SpinBoxes
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Amplitude and Level SpinBoxes...")
        amplitude_spins: tuple[QSpinBox, ...] = (
            self.__amplitude_rank_spin,
            self.__amplitude_pipe_spin,
            self.__sustain_level_rank_harmonics_spin,
            self.__sustain_level_pipe_harmonics_spin,
            self.__sustain_level_rank_spin,
            self.__sustain_level_pipe_spin
        )
        ic(amplitude_spins)
        for spin_box in amplitude_spins:
            ic(spin_box)
            spin_box.setRange(0, 100)
            ic(f"{spin_box.minimum()} to {spin_box.maximum()}")
        ic("Amplitude and Level SpinBoxes Set Up Complete.")
        #---------------------------------------------------------------------------------------------------------------
        # Attack, Decay, Release SpinBoxes
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Up Attack, Decay, Release SpinBoxes...")
        attack_decay_release_spins: tuple[QSpinBox, ...] = (
            self.__attack_time_rank_harmonics_spin,
            self.__decay_time_rank_harmonics_spin,
            self.__release_time_rank_harmonics_spin,
            self.__attack_time_rank_spin,
            self.__decay_time_rank_spin,
            self.__release_time_rank_spin,
            self.__attack_time_pipe_harmonics_spin,
            self.__decay_time_pipe_harmonics_spin,
            self.__release_time_pipe_harmonics_spin,
            self.__attack_time_pipe_spin,
            self.__decay_time_pipe_spin,
            self.__release_time_pipe_spin
        )
        ic(attack_decay_release_spins)
        for spin_box in attack_decay_release_spins:
            ic(spin_box)
            spin_box.setRange(0, 2000)
            ic(f"{spin_box.minimum()} to {spin_box.maximum()}")
        ic("Attack, Decay, Release SpinBoxes Set Up Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __ui_settings_editor_checkboxes(self) -> None:
        ic("Setting Up Check Boxes...")
        self.__rank_harmonics_button.checkStateChanged.connect(self.__rank_harmonics_checked)
        ic(f"{self.__rank_harmonics_button} connected to {self.__rank_harmonics_checked}")
        self.__rank_harmonics_adsr_button.checkStateChanged.connect(self.__rank_harmonics_adsr_checked)
        ic(f"{self.__rank_harmonics_adsr_button} connected to {self.__rank_harmonics_adsr_checked}")
        self.__rank_adsr_button.checkStateChanged.connect(self.__rank_adsr_checked)
        ic(f"{self.__rank_adsr_button} connected to {self.__rank_adsr_checked}")
        self.__pipe_harmonics_button.checkStateChanged.connect(self.__pipe_harmonics_checked)
        ic(f"{self.__pipe_harmonics_button} connected to {self.__pipe_harmonics_checked}")
        self.__pipe_harmonics_adsr_button.checkStateChanged.connect(self.__pipe_harmonics_adsr_checked)
        ic(f"{self.__pipe_harmonics_adsr_button} connected to {self.__pipe_harmonics_adsr_checked}")
        self.__pipe_adsr_button.checkStateChanged.connect(self.__pipe_adsr_checked)
        ic(f"{self.__pipe_adsr_button} connected to {self.__pipe_adsr_checked}")
        ic("Check Boxes Settings Complete.")

    #===================================================================================================================
    # Actions
    #===================================================================================================================
    #*******************************************************************************************************************
    # Widget Manipulation
    #*******************************************************************************************************************
    def __rank_harmonics_checked(self) -> None:
        ic("Initiating Rank Harmonics CheckBox Clicked...")
        widgets: tuple[QWidget, ...] = (
            self.__rank_harmonics_group,
            self.__harmonic_number_rank_label,
            self.__harmonic_number_rank_spin,
            self.__amplitude_rank_label,
            self.__amplitude_rank_spin,
            self.__rank_harmonics_adsr_button
        )
        ic(widgets)
        rank_harmonics_checked: bool = self.__rank_harmonics_button.isChecked()
        ic(rank_harmonics_checked)
        match rank_harmonics_checked:
            case True:
                for widget in widgets:
                    ic(widget)
                    widget.setEnabled(True)
                    ic(widget.isEnabled())
            case False:
                self.__rank_harmonics_adsr_button.setChecked(False)
                ic(self.__rank_harmonics_adsr_button.isChecked())
                self.__rank_harmonics_adsr_checked()
                for widget in widgets:
                    ic(widget)
                    widget.setEnabled(False)
                    ic(widget.isEnabled())
        ic("Rank Harmonics CheckBox Clicked Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __rank_harmonics_adsr_checked(self) -> None:
        ic("Initiating Rank Harmonic ADSR CheckBox Clicked...")
        widgets: tuple[QWidget, ...] = (
            self.__rank_harmonics_adsr_group,
            self.__attack_time_rank_harmonics_label,
            self.__attack_time_rank_harmonics_spin,
            self.__decay_time_rank_harmonics_label,
            self.__decay_time_rank_harmonics_spin,
            self.__sustain_level_rank_harmonics_label,
            self.__sustain_level_rank_harmonics_spin,
            self.release_time_rank_harmonics_label,
            self.__release_time_rank_harmonics_spin
        )
        ic(widgets)
        rank_harmonics_adsr_checked: bool = self.__rank_harmonics_adsr_button.isChecked()
        ic(rank_harmonics_adsr_checked)
        match rank_harmonics_adsr_checked:
            case True:
                for widget in widgets:
                    ic(widget)
                    widget.setEnabled(True)
                    ic(widget.isEnabled())
            case False:
                for widget in widgets:
                    ic(widget)
                    widget.setEnabled(False)
                    ic(widget.isEnabled())
        ic("Rank Harmonic ADSR CheckBox Clicked Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __rank_adsr_checked(self) -> None:
        ic("Initiating Rank ADSR CheckBox Clicked...")
        widgets: tuple[QWidget, ...] = (
            self.__rank_adsr_group,
            self.__attack_time_rank_label,
            self.__attack_time_rank_spin,
            self.__decay_time_rank_label,
            self.__decay_time_rank_spin,
            self.__sustain_level_rank_label,
            self.__sustain_level_rank_spin,
            self.__release_time_rank_label,
            self.__release_time_rank_spin
        )
        ic(widgets)
        rank_adsr_checked: bool = self.__rank_adsr_button.isChecked()
        ic(rank_adsr_checked)
        match rank_adsr_checked:
            case True:
                for widget in widgets:
                    ic(widget)
                    widget.setEnabled(True)
                    ic(widget.isEnabled())
            case False:
                for widget in widgets:
                    ic(widget)
                    widget.setEnabled(False)
                    ic(widget.isEnabled())
        ic("Rank ADSR CheckBox Clicked Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __pipe_harmonics_checked(self) -> None:
        ic("Initiating Pipe Harmonics CheckBox Clicked...")
        widgets: tuple[QWidget, ...] = (
            self.__pipe_harmonics_group,
            self.__harmonic_number_pipe_label,
            self.__harmonic_number_pipe_spin,
            self.__amplitude_pipe_label,
            self.__amplitude_pipe_spin,
            self.__pipe_harmonics_adsr_button
        )
        ic(widgets)
        pipe_harmonics_checked: bool = self.__pipe_harmonics_button.isChecked()
        ic(pipe_harmonics_checked)
        match pipe_harmonics_checked:
            case True:
                for widget in widgets:
                    ic(widget)
                    widget.setEnabled(True)
                    ic(widget.isEnabled())
            case False:
                self.__pipe_harmonics_adsr_button.setChecked(False)
                ic(self.__pipe_harmonics_adsr_button.isChecked())
                self.__pipe_harmonics_adsr_checked()
                for widget in widgets:
                    ic(widget)
                    widget.setEnabled(False)
                    ic(widget.isEnabled())
        ic("Pipe Harmonics CheckBox Clicked Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __pipe_harmonics_adsr_checked(self) -> None:
        ic("Initiating Pipe Harmonic ADSR CheckBox Clicked...")
        spins: tuple[QWidget, ...] = (
            self.__pipe_harmonics_adsr_group,
            self.__attack_time_pipe_harmonics_label,
            self.__attack_time_pipe_harmonics_spin,
            self.__decay_time_pipe_harmonics_label,
            self.__decay_time_pipe_harmonics_spin,
            self.__sustain_level_pipe_harmonics_label,
            self.__sustain_level_pipe_harmonics_spin,
            self.__release_time_pipe_harmonics_label,
            self.__release_time_pipe_harmonics_spin
        )
        ic(spins)
        pipe_harmonics_adsr_checked: bool = self.__pipe_harmonics_adsr_button.isChecked()
        ic(pipe_harmonics_adsr_checked)
        match pipe_harmonics_adsr_checked:
            case True:
                for spin in spins:
                    ic(spin)
                    spin.setEnabled(True)
                    ic(spin.isEnabled())
            case False:
                for spin in spins:
                    ic(spin)
                    spin.setEnabled(False)
                    ic(spin.isEnabled())
        ic("Pipe Harmonic ADSR CheckBox Clicked Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def __pipe_adsr_checked(self) -> None:
        ic("Initiating Pipe ADSR CheckBox Clicked...")
        spins: tuple[QWidget, ...] = (
            self.__pipe_adsr_group,
            self.__attack_time_pipe_label,
            self.__attack_time_pipe_spin,
            self.__decay_time_pipe_label,
            self.__decay_time_pipe_spin,
            self.__sustain_level_pipe_label,
            self.__sustain_level_pipe_spin,
            self.__release_time_pipe_label,
            self.__release_time_pipe_spin
        )
        ic(spins)
        pipe_adsr_checked: bool = self.__pipe_adsr_button.isChecked()
        ic(pipe_adsr_checked)
        match pipe_adsr_checked:
            case True:
                for spin in spins:
                    ic(spin)
                    spin.setEnabled(True)
                    ic(spin.isEnabled())
            case False:
                for spin in spins:
                    ic(spin)
                    spin.setEnabled(False)
                    ic(spin.isEnabled())
        ic("Pipe ADSR CheckBox Clicked Complete.")

    #********************************************************************************************************************
    # Signal Manipulation
    #********************************************************************************************************************
    def stop_name_combo_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__stop_name_combo.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def stop_name_combo_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__stop_name_combo.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def stop_family_combo_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__stop_family_combo.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def stop_family_combo_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__stop_family_combo.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def organ_division_combo_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__organ_division_combo.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def organ_division_combo_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__organ_division_combo.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def number_ranks_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__number_ranks_spin.blockSignals(True)
        ic("Signals Blocked.")
    #-------------------------------------------------------------------------------------------------------------------
    def number_ranks_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__number_ranks_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_number_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__rank_number_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_number_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__rank_number_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_series_combo_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__rank_series_combo.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_series_combo_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__rank_series_combo.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_size_combo_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__rank_size_combo.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_size_combo_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__rank_size_combo.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def number_pipes_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__number_pipes_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def number_pipes_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__number_pipes_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_type_combo_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__pipe_type_combo.blockSignals(True)
        ic("Signals Blocked.")
    
    #-------------------------------------------------------------------------------------------------------------------
    def pipe_type_combo_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__pipe_type_combo.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def starting_note_combo_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__starting_note_combo.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def starting_note_combo_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__starting_note_combo.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def frequency_offset_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__frequency_offset_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def frequency_offset_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__frequency_offset_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def number_harmonics_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__number_harmonics_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def number_harmonics_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__number_harmonics_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_number_rank_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__harmonic_number_rank_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_number_rank_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__harmonic_number_rank_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_rank_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__amplitude_rank_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_rank_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__amplitude_rank_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_rank_harmonic_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__attack_time_rank_harmonics_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_rank_harmonic_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__attack_time_rank_harmonics_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_rank_harmonic_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__decay_time_rank_harmonics_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_rank_harmonic_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__decay_time_rank_harmonics_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_rank_harmonic_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__sustain_level_rank_harmonics_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_rank_harmonic_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__sustain_level_rank_harmonics_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_rank_harmonic_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__release_time_rank_harmonics_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_rank_harmonic_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__release_time_rank_harmonics_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_rank_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__attack_time_rank_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_rank_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__attack_time_rank_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_rank_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__decay_time_rank_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_rank_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__decay_time_rank_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_rank_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__sustain_level_rank_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_rank_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__sustain_level_rank_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_rank_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__release_time_rank_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_rank_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__release_time_rank_spin.blockSignals(False)
        ic(self.__release_time_rank_spin.signalsBlocked())
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_number_pipe_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__rank_number_pipe_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_number_pipe_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__rank_number_pipe_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_number_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__pipe_number_spin.blockSignals(True)
        ic(self.__pipe_number_spin.signalsBlocked())
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_number_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__pipe_number_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def note_combo_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__note_combo.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def note_combo_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__note_combo.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def relative_note_combo_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__relative_note_combo.blockSignals(True)
        ic("Signals Blocked.")

    def relative_note_combo_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__relative_note_combo.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_number_pipe_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__harmonic_number_pipe_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_number_pipe_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__harmonic_number_pipe_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_pipe_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__amplitude_pipe_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_pipe_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__amplitude_pipe_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_pipe_harmonic_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__attack_time_pipe_harmonics_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_pipe_harmonic_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__attack_time_pipe_harmonics_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_pipe_harmonic_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__decay_time_pipe_harmonics_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_pipe_harmonic_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__decay_time_pipe_harmonics_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_pipe_harmonic_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__sustain_level_pipe_harmonics_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_pipe_harmonic_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__sustain_level_pipe_harmonics_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_pipe_harmonic_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__release_time_pipe_harmonics_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_pipe_harmonic_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__release_time_pipe_harmonics_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_pipe_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__attack_time_pipe_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_pipe_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__attack_time_pipe_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_pipe_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__decay_time_pipe_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_pipe_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__decay_time_pipe_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_pipe_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__sustain_level_pipe_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_pipe_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__sustain_level_pipe_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_pipe_spin_signal_blocking(self) -> None:
        ic("Blocking Signals...")
        self.__release_time_pipe_spin.blockSignals(True)
        ic("Signals Blocked.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_pipe_spin_signal_unblocking(self) -> None:
        ic("Unblocking Signals...")
        self.__release_time_pipe_spin.blockSignals(False)
        ic("Signals Unblocked.")

    #*******************************************************************************************************************
    # Data Manipulation
    #*******************************************************************************************************************
    def update_stop_header(self) -> None:
        ic("Updating Stop Header...")
        match self.number_ranks:
            case 1:
                if self.rank_size != "":
                    stop_name: str = f"{self.stop_name} {self.rank_size}"
                else:
                    stop_name: str = ""
            case 2:
                stop_name: str = f"{self.stop_name} II"
            case 3:
                stop_name: str = f"{self.stop_name} III"
            case 4:
                stop_name: str = f"{self.stop_name} IV"
            case 5:
                stop_name: str = f"{self.stop_name} V"
            case 6:
                stop_name: str = f"{self.stop_name} VI"
            case 7:
                stop_name: str = f"{self.stop_name} VII"
            case 8:
                stop_name: str = f"{self.stop_name} VIII"
            case 9:
                stop_name: str = f"{self.stop_name} IX"
            case 10:
                stop_name: str = f"{self.stop_name} X"
            case _:
                stop_name: str = ""
        ic(stop_name)
        self.__header_edit.setText(stop_name)
        ic(self.__header_edit.text())
        ic("Stop Header Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def stop_name_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Stop Name Change Connection...")
        ic(action)
        self.__stop_name_combo.currentTextChanged.connect(action)
        ic(f"{self.__stop_name_combo} connected to {action}")
        ic("Stop Name Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def stop_family_change_connect(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Stop Family Change Connection...")
        ic(action)
        self.__stop_family_combo.currentTextChanged.connect(action)
        ic(f"{self.__stop_family_combo} connected to {action}")
        ic("Stop Family Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def organ_division_change_connect(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Organ Division Change Connection...")
        ic(action)
        self.__organ_division_combo.currentTextChanged.connect(action)
        ic(f"{self.__organ_division_combo} connected to {action}")
        ic("Organ Division Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_number_ranks(self) -> None:
        ic("Updating Number of Ranks...")
        number_ranks: int = self.__number_ranks_spin.value()
        ic(number_ranks)
        rank_spins: tuple[QSpinBox, ...] = (
            self.__rank_number_spin,
            self.__rank_number_pipe_spin
        )
        ic(rank_spins)
        for spin in rank_spins:
            ic(spin)
            spin.setMaximum(number_ranks)
            ic(spin.maximum())
        ic("Number of Ranks Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def number_ranks_change_connect(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Number of Ranks Change Connection...")
        ic(action)
        self.__number_ranks_spin.valueChanged.connect(action)
        ic(f"{self.__number_ranks_spin} connected to {action}")
        ic("Number of Ranks Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_series_change_connect(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Series Change Connection...")
        self.__rank_series_combo.currentTextChanged.connect(action)
        ic(f"{self.__rank_series_combo} connected to {action}")
        ic("Rank Series Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_rank_number(self) -> None:
        ic("Updating Rank Number...")
        rank_number: int = self.__rank_number_spin.value()
        self.__rank_number_pipe_spin.setValue(rank_number)

    #-------------------------------------------------------------------------------------------------------------------
    def rank_number_change_connect(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Number Change Connection...")
        ic(action)
        self.__rank_number_spin.valueChanged.connect(action)
        ic(f"{self.__rank_number_spin} connected to {action}")
        ic("Rank Number Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_rank_sizes(self) -> None:
        ic("Updating Rank Sizes...")
        rank_sizes: list[str] = ["",]
        ic(rank_sizes)
        rank_series: str = self.__rank_series_combo.currentText()
        ic(rank_series)
        match rank_series:
            case "64' Series":
                rank_sizes += organlib.RANK_SERIES_64
            case "32' Series":
                rank_sizes += organlib.RANK_SERIES_32
            case "16' Series":
                rank_sizes += organlib.RANK_SERIES_16
            case "8' Series":
                rank_sizes += organlib.RANK_SERIES_8
            case "4' Series":
                rank_sizes += organlib.RANK_SERIES_4
            case _:
                rank_sizes += organlib.RANK_SIZES
        ic(rank_sizes)
        self.__rank_size_combo.clear()
        ic(f"{self.__rank_size_combo} cleared.")
        self.__rank_size_combo.addItems(rank_sizes)
        ic(f"{rank_sizes} added to {self.__rank_size_combo}")
        ic("Rank Sizes Updated.")
    
    #-------------------------------------------------------------------------------------------------------------------
    def rank_size_change_connect(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Size Change Connection...")
        ic(action)
        self.__rank_size_combo.currentTextChanged.connect(action)
        ic(f"{self.__rank_size_combo} connected to {action}")
        ic("Rank Size Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_number_pipes(self) -> None:
        ic("Updating Number of Pipes...")
        number_pipes: int = self.__number_pipes_spin.value()
        ic(number_pipes)
        self.__pipe_number_spin.setMaximum(number_pipes)
        ic(self.__pipe_number_spin.maximum())
        ic("Number of Pipes Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def number_pipes_change_connect(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Number of Pipes Change Connection...")
        ic(action)
        self.__number_pipes_spin.valueChanged.connect(action)
        ic(f"{self.__number_pipes_spin} connected to {action}")
        ic("Number of Pipes Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_type_change_connection(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Type Change Connection...")
        ic(action)
        self.__pipe_type_combo.currentTextChanged.connect(action)
        ic(f"{self.__pipe_type_combo} connected to {action}")
        ic("Pipe Type Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def starting_note_change_connection(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Starting Note Change Connection...")
        ic(action)
        self.__starting_note_combo.currentTextChanged.connect(action)
        ic(f"{self.__starting_note_combo} connected to {action}")
        ic("Starting Note Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def frequency_offset_change_connection(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Frequency Offset Change Connection...")
        ic(action)
        self.__frequency_offset_spin.valueChanged.connect(action)
        ic(f"{self.__frequency_offset_spin} connected to {action}")
        ic("Frequency Offset Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_number_harmonics(self) -> None:
        ic("Updating Number of Harmonics...")
        number_harmonics: int = self.__number_harmonics_spin.value()
        ic(number_harmonics)
        harmonic_spins: tuple[QSpinBox, ...] = (
            self.__harmonic_number_rank_spin,
            self.__harmonic_number_pipe_spin
        )
        ic(harmonic_spins)
        for spin in harmonic_spins:
            ic(spin)
            spin.setMaximum(number_harmonics)
            ic(spin.maximum())
        ic("Number of Harmonics Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def number_harmonics_change_connection(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Number of Harmonics Change Connection...")
        ic(action)
        self.__number_harmonics_spin.valueChanged.connect(action)
        ic(f"{self.__number_harmonics_spin} connected to {action}")
        ic("Number of Harmonics Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_harmonic_number_rank(self) -> None:
        ic("Updating Harmonic Number Rank...")
        harmonic_number: int = self.__harmonic_number_rank_spin.value()
        ic(harmonic_number)
        self.__harmonic_number_pipe_spin.setValue(harmonic_number)
        ic(self.__harmonic_number_pipe_spin.value())
        ic("Harmonic Number Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_number_rank_change_connect(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Harmonic Number Change Connect...")
        ic(action)
        self.__harmonic_number_rank_spin.valueChanged.connect(action)
        ic(f"{self.__harmonic_number_rank_spin} connected to {action}")
        ic("Harmonic Number Change Connect Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_rank_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Amplitude Change Connection...")
        ic(action)
        self.__amplitude_rank_spin.valueChanged.connect(action)
        ic(f"{self.__amplitude_rank_spin} connected to {action}")
        ic("Rank Amplitude Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_rank_harmonic_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Harmonic Attack Time Change Connection...")
        ic(action)
        self.__attack_time_rank_harmonics_spin.valueChanged.connect(action)
        ic(f"{self.__attack_time_rank_harmonics_spin} connected to {action}")
        ic("Rank Harmonic Attack Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_rank_harmonic_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Harmonic Decay Time Change Connection...")
        ic(action)
        self.__decay_time_rank_harmonics_spin.valueChanged.connect(action)
        ic(f"{self.__decay_time_rank_harmonics_spin} connected to {action}")
        ic("Rank Harmonic Decay Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_rank_harmonic_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Harmonic Sustain Level Change Connection...")
        ic(action)
        self.__sustain_level_rank_harmonics_spin.valueChanged.connect(action)
        ic(f"{self.__sustain_level_rank_harmonics_spin} connected to {action}")
        ic("Rank Harmonic Sustain Level Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_rank_harmonic_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Harmonic Release Time Change Connection...")
        ic(action)
        self.__release_time_rank_harmonics_spin.valueChanged.connect(action)
        ic(f"{self.__release_time_rank_harmonics_spin} connected to {action}")
        ic("Rank Harmonic Release Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_rank_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Attack Time Change Connection...")
        ic(action)
        self.__attack_time_rank_spin.valueChanged.connect(action)
        ic(f"{self.__attack_time_rank_spin} connected to {action}")
        ic("Rank Attack Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_rank_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Decay Time Change Connection...")
        ic(action)
        self.__decay_time_rank_spin.valueChanged.connect(action)
        ic(f"{self.__decay_time_rank_spin} connected to {action}")
        ic("Rank Decay Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_rank_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Sustain Level Change Connection...")
        ic(action)
        self.__sustain_level_rank_spin.valueChanged.connect(action)
        ic(f"{self.__sustain_level_rank_spin} connected to {action}")
        ic("Rank Sustain Level Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_rank_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Release Time Change Connection...")
        ic(action)
        self.__release_time_rank_spin.valueChanged.connect(action)
        ic(f"{self.__release_time_rank_spin} connected to {action}")
        ic("Rank Release Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_rank_number_pipe(self) -> None:
        ic("Updating Rank Number Pipe...")
        rank_number: int = self.__rank_number_pipe_spin.value()
        ic(rank_number)
        self.__rank_number_spin.setValue(rank_number)
        ic(self.__rank_number_spin.value())
        ic("Rank Number Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def rank_number_pipe_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Number Change Connection...")
        ic(action)
        self.__rank_number_pipe_spin.valueChanged.connect(action)
        ic(f"{self.__rank_number_pipe_spin} connected to {action}")
        ic("Rank Number Change Complete Connection.")

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_number_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Number Change Connection...")
        ic(action)
        self.__pipe_number_spin.valueChanged.connect(action)
        ic(f"{self.__pipe_number_spin} connected to {action}")
        ic("Pipe Number Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def note_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Note Change Connection...")
        ic(action)
        self.__note_combo.currentTextChanged.connect(action)
        ic(f"{self.__note_combo} connected to {action}")
        ic("Note Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def relative_note_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Relative Note Change Connection...")
        ic(action)
        self.__relative_note_combo.currentTextChanged.connect(action)
        ic(f"{self.__relative_note_combo} connected to {action}")
        ic("Relative Note Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_harmonic_number_pipe(self) -> None:
        ic("Updating Pipe Harmonic Number...")
        harmonic_number: int = self.__harmonic_number_pipe_spin.value()
        ic(harmonic_number)
        self.__harmonic_number_rank_spin.setValue(harmonic_number)
        ic(self.__harmonic_number_rank_spin.value())
        ic("Pipe Harmonic Number Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_number_pipe_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Number Change Connection...")
        ic(action)
        self.__harmonic_number_pipe_spin.valueChanged.connect(action)
        ic(f"{self.__harmonic_number_pipe_spin} connected to {action}")
        ic("Pipe Harmonic Number Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_pipe_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Amplitude Change Connection...")
        ic(action)
        self.__amplitude_pipe_spin.valueChanged.connect(action)
        ic(f"{self.__amplitude_pipe_spin} connected to {action}")
        ic("Pipe Amplitude Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_pipe_harmonic_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Attack Time Change Connection...")
        ic(action)
        self.__attack_time_pipe_harmonics_spin.valueChanged.connect(action)
        ic(f"{self.__attack_time_pipe_harmonics_spin} connected to {action}")
        ic("Pipe Harmonic Attack Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_pipe_harmonic_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Decay Time Change Connection...")
        ic(action)
        self.__decay_time_pipe_harmonics_spin.valueChanged.connect(action)
        ic(f"{self.__decay_time_pipe_harmonics_spin} connected to {action}")
        ic("Pipe Harmonic Decay Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_pipe_harmonic_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Sustain Level Change Connection...")
        ic(action)
        self.__sustain_level_pipe_harmonics_spin.valueChanged.connect(action)
        ic("Pipe Harmonic Sustain Level Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_pipe_harmonic_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Release Time Change Connection...")
        ic(action)
        self.__release_time_pipe_harmonics_spin.valueChanged.connect(action)
        ic("Pipe Harmonic Release Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_pipe_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Attack Time Change Connection...")
        ic(action)
        self.__attack_time_pipe_spin.valueChanged.connect(action)
        ic("Pipe Attack Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_pipe_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Decay Time Change Connection...")
        ic(action)
        self.__decay_time_pipe_spin.valueChanged.connect(action)
        ic("Pipe Decay Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_pipe_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Sustain Level Change Connection...")
        ic(action)
        self.__sustain_level_pipe_spin.valueChanged.connect(action)
        ic("Pipe Sustain Level Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_pipe_change_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Release Time Change Connection...")
        ic(action)
        self.__release_time_pipe_spin.valueChanged.connect(action)
        ic(f"{self.__release_time_pipe_spin} connected to {action}")
        ic("Pipe Release Time Change Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def load_stop_action_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Load Stop Action Connection...")
        ic(action)
        self.__load_button.clicked.connect(action)
        ic(f"{self.__load_button} connected to {action}")
        ic("Load Stop Action Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def cancel_changes_action_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Cancel Changes Action Connection...")
        ic(action)
        self.__cancel_button.clicked.connect(action)
        ic(f"{self.__cancel_button} connected to {action}")
        ic("Cancel Changes Action Connection Complete.")

    #-------------------------------------------------------------------------------------------------------------------
    def save_stop_action_connect(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Save Stop Action Connection...")
        ic(action)
        self.__save_button.clicked.connect(action)
        ic(f"{self.__save_button} connected to {action}")
        ic("Save Stop Action Connection Complete.")

    #===================================================================================================================
    # Properties
    #===================================================================================================================
    #*******************************************************************************************************************
    # Stop Header
    #*******************************************************************************************************************
    @property
    def stop_header(self) -> str:
        ic("Getting Stop Header...")
        value: str = self.__header_edit.text()
        ic(value)
        ic("Stop Header Retrieved.")
        return value

    #*******************************************************************************************************************
    # Stop Name
    #*******************************************************************************************************************
    @property
    def stop_name(self) -> str:
        ic("Getting Stop Name...")
        value: str = self.__stop_name_combo.currentText()
        ic(value)
        ic("Stop Name Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @stop_name.setter
    def stop_name(self, value: str) -> None:
        ic("Setting Stop Name...")
        ic(value)
        self.__stop_name_combo.setCurrentText(value)
        ic("Stop Name Set.")

    #*******************************************************************************************************************
    # Stop Family
    #*******************************************************************************************************************
    @property
    def stop_family(self) -> str:
        ic("Getting Stop Family...")
        value: str = self.__stop_family_combo.currentText()
        ic(value)
        ic("Stop Family Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @stop_family.setter
    def stop_family(self, value: str) -> None:
        ic("Setting Stop Family...")
        ic(value)
        self.__stop_family_combo.setCurrentText(value)
        ic("Stop Family Set.")

    #*******************************************************************************************************************
    # Organ Division
    #*******************************************************************************************************************
    @property
    def organ_division(self) -> str:
        ic("Getting Organ Division...")
        value: str = self.__organ_division_combo.currentText()
        ic(value)
        ic("Organ Division Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @organ_division.setter
    def organ_division(self, value: str) -> None:
        ic("Setting Organ Division...")
        ic(value)
        self.__organ_division_combo.setCurrentText(value)
        ic("Organ Division Set.")

    #*******************************************************************************************************************
    # Number of Ranks
    #*******************************************************************************************************************
    @property
    def number_ranks(self) -> int:
        ic("Getting Number of Ranks...")
        value: int = self.__number_ranks_spin.value()
        ic(value)
        ic("Number of Ranks Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @number_ranks.setter
    def number_ranks(self, value: int) -> None:
        ic("Setting Number of Ranks...")
        ic(value)
        self.__number_ranks_spin.setValue(value)
        ic("Number of Ranks Set.")

    #*******************************************************************************************************************
    # Rank Series
    #*******************************************************************************************************************
    @property
    def rank_series(self) -> str:
        ic("Getting Rank Series...")
        value: str = self.__rank_series_combo.currentText()
        ic(value)
        ic("Rank Series Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @rank_series.setter
    def rank_series(self, value: str) -> None:
        ic("Setting Rank Series...")
        ic(value)
        self.__rank_series_combo.setCurrentText(value)
        ic("Rank Series Set.")

    #*******************************************************************************************************************
    # Rank Number
    #*******************************************************************************************************************
    @property
    def rank_number(self) -> int:
        ic("Getting Rank Number...")
        value: int = self.__rank_number_spin.value()
        ic(value)
        ic("Rank Number Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @rank_number.setter
    def rank_number(self, value: int) -> None:
        ic("Setting Rank Number...")
        ic(value)
        self.__rank_number_spin.setValue(value)
        ic("Rank Number Set.")

    #*******************************************************************************************************************
    # Rank Size
    #*******************************************************************************************************************
    @property
    def rank_size(self) -> str:
        ic("Getting Rank Size...")
        value: str = self.__rank_size_combo.currentText()
        ic(value)
        ic("Rank Size Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @rank_size.setter
    def rank_size(self, value: str) -> None:
        ic("Setting Rank Size...")
        ic(value)
        self.__rank_size_combo.setCurrentText(value)
        ic("Rank Size Set.")

    #*******************************************************************************************************************
    # Number of Pipes
    #*******************************************************************************************************************
    @property
    def number_pipes(self) -> int:
        ic("Getting Number of Pipes...")
        value: int = self.__number_pipes_spin.value()
        ic(value)
        ic("Number of Pipes Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @number_pipes.setter
    def number_pipes(self, value: int) -> None:
        ic("Setting Number of Pipes...")
        ic(value)
        self.__number_pipes_spin.setValue(value)
        ic("Number of Pipes Set.")

    #*******************************************************************************************************************
    # Pipe Type
    #*******************************************************************************************************************
    @property
    def pipe_type(self) -> str:
        ic("Getting Pipe Type...")
        value: str = self.__pipe_type_combo.currentText()
        ic(value)
        ic("Pipe Type Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @pipe_type.setter
    def pipe_type(self, value: str) -> None:
        ic("Setting Pipe Type...")
        ic(value)
        self.__pipe_type_combo.setCurrentText(value)
        ic("Pipe Type Set.")

    #*******************************************************************************************************************
    # Starting Note
    #*******************************************************************************************************************
    @property
    def starting_note(self) -> str:
        ic("Getting Starting Note...")
        value: str = self.__starting_note_combo.currentText()
        ic(value)
        ic("Starting Note Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @starting_note.setter
    def starting_note(self, value: str) -> None:
        ic("Setting Starting Note...")
        ic(value)
        self.__starting_note_combo.setCurrentText(value)
        ic("Starting Note Set.")

    #*******************************************************************************************************************
    # Frequency Offset
    #*******************************************************************************************************************
    @property
    def frequency_offset(self) -> int:
        ic("Getting Frequency Offset...")
        value: int = self.__frequency_offset_spin.value()
        ic(value)
        ic("Frequency Offset Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @frequency_offset.setter
    def frequency_offset(self, value: int) -> None:
        ic("Setting Frequency Offset...")
        ic(value)
        self.__frequency_offset_spin.setValue(value)
        ic("Frequency Offset Set.")

    #*******************************************************************************************************************
    # Number of Harmonics
    #*******************************************************************************************************************
    @property
    def number_harmonics(self) -> int:
        ic("Getting Number of Harmonics...")
        value: int = self.__number_harmonics_spin.value()
        ic(value)
        ic("Number of Harmonics Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @number_harmonics.setter
    def number_harmonics(self, value: int) -> None:
        ic("Setting Number of Harmonics...")
        ic(value)
        self.__number_harmonics_spin.setValue(value)
        ic("Number of Harmonics Set.")

    #*******************************************************************************************************************
    # Harmonic Number - Rank
    #*******************************************************************************************************************
    @property
    def harmonic_number_rank(self) -> int:
        ic("Getting Harmonic Number...")
        value: int = self.__harmonic_number_rank_spin.value()
        ic(value)
        ic("Harmonic Number Retrieved.")
        return self.__harmonic_number_rank_spin.value()

    #-------------------------------------------------------------------------------------------------------------------
    @harmonic_number_rank.setter
    def harmonic_number_rank(self, value: int) -> None:
        ic("Setting Harmonic Number...")
        ic(value)
        self.__harmonic_number_rank_spin.setValue(value)
        ic("Harmonic Number Set.")

    #*******************************************************************************************************************
    # Amplitude - Rank
    #*******************************************************************************************************************
    @property
    def amplitude_rank(self) -> int:
        ic("Getting Rank Amplitude...")
        value: int = self.__amplitude_rank_spin.value()
        ic(value)
        ic("Rank Amplitude Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude_rank.setter
    def amplitude_rank(self, value: int) -> None:
        ic("Setting Rank Amplitude...")
        ic(value)
        self.__amplitude_rank_spin.setValue(value)
        ic("Rank Amplitude Set.")

    #*******************************************************************************************************************
    # Attack Time - Harmonic - Rank
    #*******************************************************************************************************************
    @property
    def attack_time_rank_harmonic(self) -> int:
        ic("Getting Rank Harmonic Attack Time...")
        value: int = self.__attack_time_rank_harmonics_spin.value()
        ic(value)
        ic("Rank Harmonic Attack Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @attack_time_rank_harmonic.setter
    def attack_time_rank_harmonic(self, value: int) -> None:
        ic("Setting Rank Harmonic Attack Time...")
        ic(value)
        self.__attack_time_rank_harmonics_spin.setValue(value)
        ic("Rank Harmonic Attack Time Set.")

    #*******************************************************************************************************************
    # Decay Time - Harmonic - Rank
    #*******************************************************************************************************************
    @property
    def decay_time_rank_harmonic(self) -> int:
        ic("Getting Rank Harmonic Decay Time...")
        value: int = self.__decay_time_rank_harmonics_spin.value()
        ic(value)
        ic("Rank Harmonic Decay Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @decay_time_rank_harmonic.setter
    def decay_time_rank_harmonic(self, value: int) -> None:
        ic("Setting Rank Harmonic Decay Time...")
        ic(value)
        self.__decay_time_rank_harmonics_spin.setValue(value)
        ic("Rank Harmonic Decay Time Set.")

    #*******************************************************************************************************************
    # Sustain Level - Harmonic - Rank
    #*******************************************************************************************************************
    @property
    def sustain_level_rank_harmonic(self) -> int:
        ic("Getting Rank Harmonic Sustain Level...")
        value: int = self.__sustain_level_rank_harmonics_spin.value()
        ic(value)
        ic("Rank Harmonic Sustain Level Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_level_rank_harmonic.setter
    def sustain_level_rank_harmonic(self, value: int) -> None:
        ic("Setting Rank Harmonic Sustain Level...")
        ic(value)
        self.__sustain_level_rank_harmonics_spin.setValue(value)
        ic("Rank Harmonic Sustain Level Set.")

    #*******************************************************************************************************************
    # Release Time - Harmonic - Rank
    #*******************************************************************************************************************
    @property
    def release_time_rank_harmonic(self) -> int:
        ic("Getting Rank Harmonic Release Time...")
        value: int = self.__release_time_rank_harmonics_spin.value()
        ic(value)
        ic("Rank Harmonic Release Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @release_time_rank_harmonic.setter
    def release_time_rank_harmonic(self, value: int) -> None:
        ic("Setting Rank Harmonic Release Time...")
        ic(value)
        self.__release_time_rank_harmonics_spin.setValue(value)
        ic("Rank Harmonic Release Time Set.")

    #*******************************************************************************************************************
    # Attack Time - Rank
    #*******************************************************************************************************************
    @property
    def attack_time_rank(self) -> int:
        ic("Getting Rank Attack Time...")
        value: int = int(self.__attack_time_rank_spin.value())
        ic(value)
        ic("Rank Attack Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @attack_time_rank.setter
    def attack_time_rank(self, value: int) -> None:
        ic("Setting Rank Attack Time...")
        ic(value)
        self.__attack_time_rank_spin.setValue(value)
        ic("Rank Attack Time Set.")

    #*******************************************************************************************************************
    # Decay Time - Rank
    #*******************************************************************************************************************
    @property
    def decay_time_rank(self) -> int:
        ic("Getting Rank Decay Time...")
        value: int = self.__decay_time_rank_spin.value()
        ic(value)
        ic("Rank Decay Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @decay_time_rank.setter
    def decay_time_rank(self, value: int) -> None:
        ic("Setting Rank Decay Time...")
        ic(value)
        self.__decay_time_rank_spin.setValue(value)
        ic("Rank Decay Time Set.")

    #*******************************************************************************************************************
    # Sustain Level - Rank
    #*******************************************************************************************************************
    @property
    def sustain_level_rank(self) -> int:
        ic("Getting Rank Sustain Level...")
        value: int = self.__sustain_level_rank_spin.value()
        ic(value)
        ic("Rank Sustain Level Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_level_rank.setter
    def sustain_level_rank(self, value: int) -> None:
        ic("Setting Rank Sustain Level...")
        ic(value)
        self.__sustain_level_rank_spin.setValue(value)
        ic("Rank Sustain Level Set.")

    #*******************************************************************************************************************
    # Release Time - Rank
    #*******************************************************************************************************************
    @property
    def release_time_rank(self) -> int:
        ic("Getting Rank Release Time...")
        value: int = self.__release_time_rank_spin.value()
        ic(value)
        ic("Rank Release Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @release_time_rank.setter
    def release_time_rank(self, value: int) -> None:
        ic("Setting Rank Release Time...")
        ic(value)
        self.__release_time_rank_spin.setValue(value)
        ic("Rank Release Time Set.")

    #*******************************************************************************************************************
    # Rank Number - Pipe
    #*******************************************************************************************************************
    @property
    def rank_number_pipe(self) -> int:
        ic("Getting Rank Number...")
        value: int = self.__rank_number_pipe_spin.value()
        ic(value)
        ic("Rank Number Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @rank_number_pipe.setter
    def rank_number_pipe(self, value: int) -> None:
        ic("Setting Rank Number...")
        ic(value)
        self.__rank_number_pipe_spin.setValue(value)
        ic("Rank Number Set.")

    #*******************************************************************************************************************
    # Pipe Number
    #*******************************************************************************************************************
    @property
    def pipe_number(self) -> int:
        ic("Getting Pipe Number...")
        value: int = self.__pipe_number_spin.value()
        ic(value)
        ic("Pipe Number Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @pipe_number.setter
    def pipe_number(self, value: int) -> None:
        ic("Setting Pipe Number...")
        ic(value)
        self.__pipe_number_spin.setValue(value)
        ic("Pipe Number Set.")

    #*******************************************************************************************************************
    # Note
    #*******************************************************************************************************************
    @property
    def note(self) -> str:
        ic("Getting Note...")
        value: str = self.__note_combo.currentText()
        ic(value)
        ic("Note Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @note.setter
    def note(self, value: str) -> None:
        ic("Setting Note...")
        ic(value)
        self.__note_combo.setCurrentText(value)
        ic("Note Set.")

    #*******************************************************************************************************************
    # Relative Note
    #*******************************************************************************************************************
    @property
    def relative_note(self) -> str:
        ic("Getting Relative Note...")
        value: str = self.__relative_note_combo.currentText()
        ic(value)
        ic("Relative Note Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @relative_note.setter
    def relative_note(self, value: str) -> None:
        ic("Setting Relative Note...")
        ic(value)
        self.__relative_note_combo.setCurrentText(value)
        ic("Relative Note Set.")

    #*******************************************************************************************************************
    # Harmonic Number - Pipe
    #*******************************************************************************************************************
    @property
    def harmonic_number_pipe(self) -> int:
        ic("Getting Pipe Harmonic Number...")
        value: int = self.__harmonic_number_pipe_spin.value()
        ic(value)
        ic("Pipe Harmonic Number Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @harmonic_number_pipe.setter
    def harmonic_number_pipe(self, value: int) -> None:
        ic("Setting Pipe Harmonic Number...")
        ic(value)
        self.__harmonic_number_pipe_spin.setValue(value)
        ic("Pipe Harmonic Number Set.")

    #*******************************************************************************************************************
    # Amplitude - Pipe
    #*******************************************************************************************************************
    @property
    def amplitude_pipe(self) -> int:
        ic("Getting Pipe Amplitude...")
        value: int = self.__amplitude_pipe_spin.value()
        ic(value)
        ic("Pipe Amplitude Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude_pipe.setter
    def amplitude_pipe(self, value: int) -> None:
        ic("Setting Pipe Amplitude...")
        ic(value)
        self.__amplitude_pipe_spin.setValue(value)
        ic("Pipe Amplitude Set.")

    #*******************************************************************************************************************
    # Attack Time - Harmonic - Pipe
    #*******************************************************************************************************************
    @property
    def attack_time_pipe_harmonics(self) -> int:
        ic("Getting Pipe Harmonic Attack Time...")
        value: int = self.__attack_time_pipe_harmonics_spin.value()
        ic(value)
        ic("Pipe Harmonic Attack Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @attack_time_pipe_harmonics.setter
    def attack_time_pipe_harmonics(self, value: int) -> None:
        ic("Setting Pipe Harmonic Attack Time...")
        ic(value)
        self.__attack_time_pipe_harmonics_spin.setValue(value)
        ic("Pipe Harmonic Attack Time Set.")

    #*******************************************************************************************************************
    # Decay Time - Harmonic - Pipe
    #*******************************************************************************************************************
    @property
    def decay_time_pipe_harmonics(self) -> int:
        ic("Getting Pipe Harmonic Decay Time...")
        value: int = self.__decay_time_pipe_harmonics_spin.value()
        ic(value)
        ic("Pipe Harmonic Decay Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @decay_time_pipe_harmonics.setter
    def decay_time_pipe_harmonics(self, value: int) -> None:
        ic("Setting Pipe Harmonic Decay Time...")
        ic(value)
        self.__decay_time_pipe_harmonics_spin.setValue(value)
        ic("Pipe Harmonic Decay Time Set.")

    #*******************************************************************************************************************
    # Sustain Level - Harmonic - Pipe
    #*******************************************************************************************************************
    @property
    def sustain_level_pipe_harmonics(self) -> int:
        ic("Getting Pipe Harmonic Sustain Level...")
        value: int = self.__sustain_level_pipe_harmonics_spin.value()
        ic(value)
        ic("Pipe Harmonic Sustain Level Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_level_pipe_harmonics.setter
    def sustain_level_pipe_harmonics(self, value: int) -> None:
        ic("Setting Pipe Harmonic Sustain Level...")
        ic(value)
        self.__sustain_level_pipe_harmonics_spin.setValue(value)
        ic("Pipe Harmonic Sustain Level Set.")

    #*******************************************************************************************************************
    # Release Time - Harmonic - Pipe
    #*******************************************************************************************************************
    @property
    def release_time_pipe_harmonics(self) -> int:
        ic("Getting Pipe Harmonic Release Time...")
        value: int = self.__release_time_pipe_harmonics_spin.value()
        ic(value)
        ic("Pipe Harmonic Release Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @release_time_pipe_harmonics.setter
    def release_time_pipe_harmonics(self, value: int) -> None:
        ic("Setting Pipe Harmonic Release Time...")
        ic(value)
        self.__release_time_pipe_harmonics_spin.setValue(value)
        ic("Pipe Harmonic Release Time Set.")

    #*******************************************************************************************************************
    # Attack Time - Pipe
    #*******************************************************************************************************************
    @property
    def attack_time_pipe(self) -> int:
        ic("Getting Pipe Attack Time...")
        value: int = self.__attack_time_pipe_spin.value()
        ic(value)
        ic("Pipe Attack Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @attack_time_pipe.setter
    def attack_time_pipe(self, value: int) -> None:
        ic("Setting Pipe Attack Time...")
        ic(value)
        self.__attack_time_pipe_spin.setValue(value)
        ic("Pipe Attack Time Set.")

    #*******************************************************************************************************************
    # Decay Time - Pipe
    #*******************************************************************************************************************
    @property
    def decay_time_pipe(self) -> int:
        ic("Getting Pipe Decay Time...")
        value: int = self.__decay_time_pipe_spin.value()
        ic(value)
        ic("Pipe Decay Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @decay_time_pipe.setter
    def decay_time_pipe(self, value: int) -> None:
        ic("Setting Pipe Decay Time...")
        ic(value)
        self.__decay_time_pipe_spin.setValue(value)
        ic("Pipe Decay Time Set.")

    #*******************************************************************************************************************
    # Sustain Level - Pipe
    #*******************************************************************************************************************
    @property
    def sustain_level_pipe(self) -> int:
        ic("Getting Pipe Sustain Level...")
        value: int = self.__sustain_level_pipe_spin.value()
        ic(value)
        ic("Pipe Sustain Level Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_level_pipe.setter
    def sustain_level_pipe(self, value: int) -> None:
        ic("Setting Pipe Sustain Level...")
        ic(value)
        self.__sustain_level_pipe_spin.setValue(value)
        ic("Pipe Sustain Level Set.")

    #*******************************************************************************************************************
    # Release Time - Pipe
    #*******************************************************************************************************************
    @property
    def release_time_pipe(self) -> int:
        ic("Getting Pipe Release Time...")
        value: int = self.__release_time_pipe_spin.value()
        ic(value)
        ic("Pipe Release Time Retrieved.")
        return value

    #-------------------------------------------------------------------------------------------------------------------
    @release_time_pipe.setter
    def release_time_pipe(self, value: int) -> None:
        ic("Setting Pipe Release Time...")
        ic(value)
        self.__release_time_pipe_spin.setValue(value)
        ic("Pipe Release Time Set.")


#=======================================================================================================================
# Main
#=======================================================================================================================
def main() -> None:
    app: QApplication = QApplication([])
    window: StopEditor = StopEditor()
    window.show()
    app.exec()


#=======================================================================================================================
# Executable
#=======================================================================================================================
if __name__ == "__main__":
    main()
