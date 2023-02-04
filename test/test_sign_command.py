from pybluesecur import sign_command

key = bytearray.fromhex('cd4a41e82431d22c0a0db172861e3638af5898481522b8ef0c093f0837c7a9c7')
challenge = bytearray.fromhex('837FDAD10EBE5C96')
timestamp = 0x0000000063dbde6f

signed = sign_command(key, challenge, 22, timestamp=0x0000000063dbde6f)
print(signed.hex())

correct = '013100010016002e006fdedb6300000000280654e8a702b46488120a1983ee33ab6745ee251f32a193886162a7926d365c'
assert signed.hex() == correct

