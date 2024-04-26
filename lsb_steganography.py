import random
import numpy as np
import imageio

def message_to_bits(message):
    message_bits = []
    for m in message:
        message_bits.extend([(ord(m) >> i) & 1 for i in range(8)])
    message_bits.append(0)
    return message_bits


def hide_message_LSB_replacement(cover_path, message_bits):
    cover = imageio.imread(cover_path)
    stego = cover.copy()
    flat_stego = stego.flatten()
    
    if len(message_bits) > len(flat_stego):
        raise ValueError("Message too long to hide in the cover image")

    for i in range(len(message_bits)):
        flat_stego[i] = (flat_stego[i] & ~1) | message_bits[i]

    stego = flat_stego.reshape(cover.shape)
    return stego

def hide_message_LSB_matching(cover_path, message_bits):
    cover = imageio.imread(cover_path)
    stego = cover.copy()
    flat_stego = stego.flatten()
    
    if len(message_bits) > len(flat_stego):
        raise ValueError("Message too long to hide in the cover image")

    for i in range(len(message_bits)):
        if cover[i] % 2 != message_bits[i]:
            flat_stego[i] = cover[i] + random.choice([-1, 1])

    stego = flat_stego.reshape(cover.shape)
    return stego

def extract_message(stego):
    stego_flat = stego.flatten()
    message_bits = [s % 2 for s in stego_flat]
    message_ex = []
    value = 0
    for i in range(len(message_bits)):
        if i % 8 == 0 and i != 0:
            message_ex.append(value)
            value = 0
        value |= message_bits[i] << i % 8
    return ''.join([chr(l) for l in message_ex])

