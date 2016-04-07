MESSAGE_SEPARATOR = '\x1E'
MESSAGE_PART_SEPARATOR = '\x1F'

TOPIC_AUTH = 'A'
TOPIC_ERROR = 'X'
TOPIC_EVENT = 'E'
TOPIC_RECORD = 'R'
TOPIC_RPC = 'P'
TOPIC_WEBRTC = 'W'
TOPIC_PRIVATE = 'PRIVATE/'

ACTIONS_ACK = 'A'
ACTIONS_ERROR = 'E'
ACTIONS_EVENT = 'EVT'
ACTIONS_REQUEST = 'REQ'
ACTIONS_RESPONSE = 'RES'
ACTIONS_REJECTION = 'REJ'
ACTIONS_SUBSCRIBE = 'S'
ACTIONS_UNSUBSCRIBE = 'US'
ACTIONS_INVOKE = 'I'
ACTIONS_SUBSCRIPTION_FOR_PATTERN_FOUND = 'SP'
ACTIONS_SUBSCRIPTION_FOR_PATTERN_REMOVED = 'SR'
ACTIONS_LISTEN = 'L'
ACTIONS_UNLISTEN = 'UL'

CONNECTION_STATE_CLOSED = 'CLOSED'
CONNECTION_STATE_AWAITING_AUTHENTICATION = 'AWAITING_AUTHENTICATION'
CONNECTION_STATE_AUTHENTICATING = 'AUTHENTICATING'
CONNECTION_STATE_OPEN = 'OPEN'
CONNECTION_STATE_ERROR = 'ERROR'
CONNECTION_STATE_RECONNECTING = 'RECONNECTING'

EVENT_TOO_MANY_AUTH_ATTEMPTS = 'TOO_MANY_AUTH_ATTEMPTS'
EVENT_IS_CLOSED = 'IS_CLOSED'
EVENT_ACK_TIMEOUT = 'ACK_TIMEOUT'
EVENT_UNSOLICITED_MESSAGE = 'UNSOLICITED_MESSAGE'
EVENT_LISTENER_EXISTS = 'LISTENER_EXISTS'
EVENT_NOT_LISTENING = 'NOT_LISTENING'
