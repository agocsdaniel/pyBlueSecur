#### These are some findings about the protocol that BlueSecur uses

* This protocol is little-endian.

Receiving challenge
```
Subscribe on BC_RX
Then you will get something like this: 837FDCD10EBE5C9604000C00

837FDCD10EBE5C96 - Challenge
04 00 - uint16; signed notification type
0C 00 - uint16; length

In some cases you can get more data based on the type
```

Sent command structure
```
01 - byte; constant
31 00 - uint16; total length: 0x0031 = 48
-- payload
  01 00 - uint16; rootID: 0x0001 = 1
  16 00 - uint16; Command: 0x0016 = 22
  2E 00 - uint16; payload length: 0x002e = 46
  6FDEDB6300000000 - filler - epoch 0x0000000063dbde6f = 2023.02.01 17:01...
  2B7BB69B49EB9E2EB5140B4D1EE1D4A62DC700215AFC9944ED49DAED8414E8D4 - HMAC SHA256 signature from rootID + challenge
--
```

Device actions
```
{ DeviceAction.CHANNEL_1, "Impuls" }, 0x11
{ DeviceAction.CHANNEL_2, "Licht" }, 0x12
{ DeviceAction.CHANNEL_3, "Teil-Auf" }, 0x13
{ DeviceAction.CHANNEL_4, "Auf" }, 0x14
{ DeviceAction.CHANNEL_5, "Zu" }, 0x15
{ DeviceAction.CHANNEL_6, "Lüftungs-Position" } 0x16
```

Advertisements
```
We read the manufacturerData value
Manufacturer ID is 1972

There are two kinds of advertisements
The first
02023d200000

The second
 x PositionState
 |
14000000000000000063b918a97e0f3204  closed  not moving  0%  
141e0000000000000063b918a97e0f3204  closed  opening     15% 
13c80000000000000063b918a97e0f3204  opened  not moving  100%
137a0000000000000063b918a97e0f3204  opened  closing     61% 

15180000000000000063b918a97e0f3204  halfway not moving      
17240000000000000063b918a97e0f3204  halfway closing         

```