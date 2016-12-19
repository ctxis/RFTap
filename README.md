# RFTap
Modified RFTap dissector for Wireshark
## Changes
Added signal bandwidth (KHz) and receiver gain (dBi).
## Setup
With wireshark >2.3 copy to ../wireshark/epan/dissectors then make.  
## Usage
Send a UDP packet containing the 100 byte RFTap header. See the Python example.
