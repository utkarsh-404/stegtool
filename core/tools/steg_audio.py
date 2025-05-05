import wave
import os


def encode_audio_lsb(input_audio, secret_message, output_audio):
    """
    Encode a secret message into a WAV audio file using LSB steganography.
    Only works with uncompressed PCM WAV files (mono or stereo).
    """
    if not os.path.exists(input_audio):
        print("[!] Input audio file not found.")
        return

    with wave.open(input_audio, mode='rb') as audio:
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    message = secret_message + '###'  # Delimiter
    bits = ''.join([format(ord(char), '08b') for char in message])

    if len(bits) > len(frame_bytes):
        print("[!] Message too long to hide in this audio.")
        return

    for i in range(len(bits)):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(bits[i])

    with wave.open(output_audio, 'wb') as modified_audio:
        modified_audio.setparams(audio.getparams())
        modified_audio.writeframes(frame_bytes)

    print(f"[+] Message encoded successfully into {output_audio}")


def decode_audio_lsb(stego_audio):
    """
    Decode a hidden message from a WAV audio file.
    """
    if not os.path.exists(stego_audio):
        print("[!] Audio file not found.")
        return

    with wave.open(stego_audio, mode='rb') as audio:
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    bits = [str(byte & 1) for byte in frame_bytes]
    chars = [chr(int(''.join(bits[i:i + 8]), 2)) for i in range(0, len(bits), 8)]
    message = ''.join(chars)

    if '###' in message:
        print(f"[+] Hidden message found:\n{message.split('###')[0]}")
    else:
        print("[!] No hidden message found.")


def main():
    input_audio = 'sample.wav'
    output_audio = 'stego_audio.wav'
    secret = 'This is a hidden message!'

    encode_audio_lsb(input_audio, secret, output_audio)
    decode_audio_lsb(output_audio)


if __name__ == "__main__":
    main()
