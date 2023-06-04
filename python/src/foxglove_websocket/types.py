from typing import List, Union, Optional
from enum import IntEnum

ChannelId = int
SubscriptionId = int
ClientChannelId = int
ServiceId = int


class Parameter(dict):
    name: str
    value: Union[int, float, bool, str, List[int], List[float], List[bool], List[str]]
    type: Optional[str]


class Subscription(dict):
    id: SubscriptionId
    channelId: ChannelId


class ClientChannel(dict):
    id: ClientChannelId
    topic: str
    encoding: str
    schemaName: str


class Subscribe(dict):
    op: str
    subscriptions: List[Subscription]


class Unsubscribe(dict):
    op: str
    subscriptionIds: List[SubscriptionId]


class ClientAdvertise(dict):
    op: str
    channels: List[ClientChannel]


class ClientUnadvertise(dict):
    op: str
    channelIds: List[ClientChannelId]


class GetParameters(dict):
    op: str
    parameterNames: List[str]
    id: Optional[str]


class SetParameters(dict):
    op: str
    parameters: List[Parameter]
    id: Optional[str]


class SubscribeParameterUpdates(dict):
    op: str
    parameterNames: List[str]


class UnsubscribeParameterUpdates(dict):
    op: str
    parameterNames: List[str]


ClientJsonMessage = Union[
    Subscribe,
    Unsubscribe,
    ClientAdvertise,
    ClientUnadvertise,
    GetParameters,
    SetParameters,
    SubscribeParameterUpdates,
    UnsubscribeParameterUpdates,
]


class BinaryOpcode(IntEnum):
    MESSAGE_DATA = 1
    TIME = 2
    SERVICE_CALL_RESPONSE = 3


class ClientBinaryOpcode(IntEnum):
    MESSAGE_DATA = 1
    SERVICE_CALL_REQUEST = 2


class ServerInfo(dict):
    op: str
    name: str
    capabilities: List[str]
    supportedEncodings: Optional[List[str]]
    metadata: Optional[dict]
    sessionId: Optional[str]


class StatusLevel(IntEnum):
    INFO = 0
    WARNING = 1
    ERROR = 2


class StatusMessage(dict):
    op: str
    level: StatusLevel
    message: str


class ChannelWithoutId(dict):
    topic: str
    encoding: str
    schemaName: str
    schema: str
    schemaEncoding: Optional[str]


class Channel(ChannelWithoutId):
    id: ChannelId


class ServiceWithoutId(dict):
    name: str
    type: str
    requestSchema: str
    responseSchema: str


class Service(ServiceWithoutId):
    id: ServiceId


class Advertise(dict):
    op: str
    channels: List[Channel]


class Unadvertise(dict):
    op: str
    channelIds: List[ChannelId]


class AdvertiseServices(dict):
    op: str
    services: List[Service]


class UnadvertiseServices(dict):
    op: str
    serviceIds: List[ServiceId]


class ParameterValues(dict):
    op: str
    parameters: List[Parameter]
    id: Optional[str]


ServerJsonMessage = Union[
    ServerInfo,
    StatusMessage,
    Advertise,
    Unadvertise,
    AdvertiseServices,
    UnadvertiseServices,
    ParameterValues,
]
