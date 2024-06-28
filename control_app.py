import streamlit as st
from streamlit_option_menu import option_menu
import pyvisa

class InstrumentManager(object):
    def __init__(self):
        self.side_menu = ["Init", "Measurements", "Monitor", "Reports"]
        self.rm = pyvisa.ResourceManager()
        self.instruments = self.rm.list_resources()
        self.selected_instruments = {}  # Dictionary to store initialized instruments (resource name as key)
        self.initialized = False  # Flag to track initialization status

    def initialize_instrument(self, resource):
        try:
            instrument = self.rm.open_resource(resource)
            # Add additional initialization steps as needed (e.g., reset, configure)
            self.selected_instruments[resource] = instrument
            st.success(f"Instrument {resource} initialized successfully.")
            self.initialized = True  # Set initialized flag after successful initialization
        except Exception as e:
            st.error(f"Error initializing instrument {resource}: {e}")

    def trigger_measurement(self):
        st.subheader("Trigger Measurement")
        if self.initialized:
            if available_instruments := self.get_available_instruments():  # Check for available instruments
                measurement_type = st.selectbox("Select Measurement Type", ["voltage", "current", "resistance"])
                if st.button(f"Start {measurement_type} Measurement"):
                    # Implement measurement triggering logic here (use appropriate resource from selected_instruments)
                    for resource, instrument in available_instruments.items():
                        try:
                            # Implement measurement specific logic for each instrument
                            st.write(f"Triggering {measurement_type} measurement on instrument {resource}...")
                            # Replace with actual measurement commands
                            instrument.write(f"MEAS:{measurement_type}")  # Placeholder command
                            # Implement data acquisition and display logic here
                        except Exception as e:
                            st.error(f"Error during measurement on {resource}: {e}")
        else:
            st.write("Please initialize instruments before triggering measurements.")

    def monitor_instruments(self):
        st.subheader("Monitor Instruments")
        # Implement monitoring logic here
        st.write("Monitoring instruments...")

    def generate_reports(self):
        st.subheader("Generate Reports")
        # Implement report generation logic here
        st.write("Generating reports...")

    def get_available_instruments(self):
        """Returns a dictionary of available instruments (resource as key, instrument object as value)."""
        available_instruments = {}
        for resource, instrument in self.selected_instruments.items():
            try:
                instrument.write("*IDN?")  # Send identification query (replace with instrument specific query if needed)
                instrument.read()  # Read response (replace with appropriate response handling)
                available_instruments[resource] = instrument
            except Exception:
                st.warning(f"Instrument {resource} may be disconnected or unresponsive.")
        return available_instruments

    def display_init_section(self):
        st.title('Initialize Instruments')

        # UI controls for instrument initialization
        for resource in self.instruments:
            if st.button(f"Initialize {resource}"):
                self.initialize_instrument(resource)
    def main(self):
        with st.sidebar:
            side_mode =  option_menu(None, self.side_menu)
        if side_mode == "Init":
            st.title('Initialize Instruments')

            # UI controls for instrument initialization
            for resource in self.instruments:
                if st.button(f"Initialize {resource}"):
                    self.initialize_instrument(resource)
        elif side_mode == "Measurements":
            self.trigger_measurement()
        elif side_mode == "Monitor":
            self.monitor_instruments()
        elif side_mode == "Reports":
            self.generate_reports()

if __name__ == "__main__":
    manager = InstrumentManager()
    manager.main()
