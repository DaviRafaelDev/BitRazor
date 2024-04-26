import os
import imageio
from lsb_steganography import hide_message_LSB_replacement, hide_message_LSB_matching, extract_message

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def message_to_bits(message):
    """Convert a message to a list of bits."""
    message_bits = []
    for m in message:
        message_bits += [(ord(m) >> i) & 1 for i in range(8)]
    return message_bits

def hide_message_cli():
    clear_screen()
    print("HIDE MESSAGE\n")
    cover_image_path = input("Enter the path to the cover image: ")
    message = input("Enter the message to hide: ")
    technique = input("Choose a technique (replacement/matching): ")
    output_image_path = input("Enter the full path to save the stego image (including filename and extension): ")

    message_bits = message_to_bits(message)

    if technique.lower() == "replacement":
        stego_image = hide_message_LSB_replacement(cover_image_path, message_bits)
    elif technique.lower() == "matching":
        stego_image = hide_message_LSB_matching(cover_image_path, message_bits)
    else:
        print("Invalid technique selected. Please choose 'replacement' or 'matching'.")
        return

    imageio.imwrite(output_image_path, stego_image)
    print(f"Message hidden successfully in {output_image_path}")

def extract_message_cli():
    clear_screen()
    print("EXTRACT MESSAGE\n")
    stego_image_path = input("Enter the path to the stego image: ").strip()
    if not os.path.exists(stego_image_path):
        print("Error: Stego image not found.")
        return

    stego_image = imageio.imread(stego_image_path)

    stego_image_flat = stego_image.flatten()

    extracted_message = extract_message(stego_image_flat)
    if extracted_message:
        print("\nExtracted message:", extracted_message)
    else:
        print("\nError: No message found in the stego image.")


def main():
    while True:
        clear_screen()
        print("Welcome to the LSB Steganography Tool!\n")
        print("1. Hide a message")
        print("2. Extract a message")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            hide_message_cli()
            input("\nPress Enter to continue...")
        elif choice == '2':
            extract_message_cli()
            input("\nPress Enter to continue...")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
