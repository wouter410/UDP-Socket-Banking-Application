
TEST_HEADER = b"\x01"

KEEP_ALIVE = b"\x10"

DISCONNECT_CLIENT = b'\x11'

LOGIN_REQUEST_HEADER = b"\x20"
STATUS_REQUEST_HEADER = b"\x21"
TRANSFER_REQUEST_HEADER = b"\x22"

MODIFY_SAVINGS_HEADER = b"\x23"
MODIFY_SAVINGS_SUCCESS_HEADER = b"\x24"
MODIFY_SAVINGS_ERROR_HEADER = b'\x25'

VIEW_SAVINGS_REQUEST_HEADER = b'\x51'
VIEW_SAVINGS_SUCCESS_RESPONSE = b'\x52'

LOGIN_SUCCESS_HEADER = b"\30"
STATUS_SUCCESS_HEADER = b"\31"
TRANSFER_SUCCESS_HEADER = b"\32"
GENERIC_ERROR_HEADER = b"\40"
LOGIN_ERROR_HEADER = b"\41"
TRANSFER_ERROR_NOTARGET_HEADER = b"\42"
TRANSFER_ERROR_NOMONEY_HEADER = b"\43"