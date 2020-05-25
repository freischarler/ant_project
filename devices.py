import usb.core
import usb.util
import sys

dev=usb.core.find()
if dev is None:
	raise ValueError('Device not found')


dev.set_configuration()
cfg=dev.get_active_configuration()
intf=cfg[(0,0)]

ep=usb.util.find_descriptor(intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

ep.write('test')
