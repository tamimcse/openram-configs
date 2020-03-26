# Data word size
word_size = 16
# Number of words in the memory
num_words = 2048
num_rw_ports = 1
num_banks = 32

# Technology to use in $OPENRAM_TECH
tech_name = "freepdk45"
# You can use the technology nominal corner only
nominal_corner_only = True
# Or you can specify particular corners
# Process corners to characterize
# process_corners = ["SS", "TT", "FF"]
# Voltage corners to characterize
# supply_voltages = [ 3.0, 3.3, 3.5 ]
# Temperature corners to characterize
# temperatures = [ 0, 25 100]

# Output directory for the results
output_path = "out/poptrie/dirC"
# Output file base name
output_name = "sram_{0}_{1}_{2}".format(word_size,num_words,tech_name)

# Disable analytical models for full characterization (WARNING: slow!)
#analytical_delay = False

