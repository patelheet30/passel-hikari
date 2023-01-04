 # Mode 1 = Once the channel reaches 49 pins, the 50th pin is sent to the pin channel
 #          and unpinned immediately
 # Mode 2 = Once the channel reaches 49 pins, the 1st pin of the channel is unpinned
 #          and sent to the pin channel allowing for newer pins to be filled into
 #          the pins tab
mode: int = SET_TO_1_OR_2

# Choose if all pins should be sent to the pins channel instead of when pins are full for channel
sendall: bool = SET_TO_TRUE_OR_FALSE

# Set the pin_message_id variable's value to the ID of the channel where you want to send the pins
pin_message_id: int = SET_VALUE_HERE  # Example: 1059366200712364083

# Add the IDs of channels you want to blacklist from being sent to pin channel
blacklist_ids: list = [ADD_IDS_IN_STRING_FORM_HERE]  # Example: ["1059367790554927114", "1059367810981167154"]
