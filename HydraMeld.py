"""
HydraMeld
Original script made by EarthWormsYas on GitHub
https://github.com/EarthWormsYas/HydraMeld
"""

import struct
import os

if __name__ == "__main__":
    import time
    try:
        import pyfiglet
    except ImportError:
        pyfiglet = None

def create_polyglot(base_file_path, zip_path, output_path):

    # Creates a polyglot file by prepending a base file (image, video, audio, exe, pdf, etc.) to a ZIP archive and adjusting the ZIP's internal offsets.

    try:
        if __name__ == "__main__":
            os.system("title Reading files...")

        with open(base_file_path, 'rb') as f:
            base_data = f.read()
        
        with open(zip_path, 'rb') as f:
            zip_data = bytearray(f.read())
        
        offset_inc = len(base_data)

        # Find End of Central Directory Record (EOCD)
        if __name__ == "__main__":
            os.system("title Some nerdy stuff that im not gonna actually type because my stuff is to fast to see it anyways. (Unless you are in which case that's rly awkward...)")
        eocd_pos = zip_data.rfind(b'\x50\x4b\x05\x06')
        if eocd_pos == -1:
            print("Error: Invalid ZIP file (EOCD signature not found).")
            return

        # Get Central Directory size and offset
        cd_size = struct.unpack('<I', zip_data[eocd_pos+12:eocd_pos+16])[0]
        cd_offset = struct.unpack('<I', zip_data[eocd_pos+16:eocd_pos+20])[0]

        # Update Central Directory offset in EOCD
        new_cd_offset = cd_offset + offset_inc
        zip_data[eocd_pos+16:eocd_pos+20] = struct.pack('<I', new_cd_offset)

        # Update offsets in Central Directory headers
        pos = cd_offset
        entries_updated = 0
        while pos < cd_offset + cd_size:
            if zip_data[pos:pos+4] != b'\x50\x4b\x01\x02':
                break
            
            # Local header offset is at offset 42 in the Central Directory entry
            local_header_offset = struct.unpack('<I', zip_data[pos+42:pos+46])[0]
            new_local_header_offset = local_header_offset + offset_inc
            zip_data[pos+42:pos+46] = struct.pack('<I', new_local_header_offset)
            
            # Read lengths of variable fields to skip to the next entry
            n = struct.unpack('<H', zip_data[pos+28:pos+30])[0] # File name length
            m = struct.unpack('<H', zip_data[pos+30:pos+32])[0] # Extra field length
            k = struct.unpack('<H', zip_data[pos+32:pos+34])[0] # File comment length
            pos += 46 + n + m + k
            entries_updated += 1

        # Combine and write the polyglot
        if __name__ == "__main__":
            os.system("title Writing polyglot...")
        with open(output_path, 'wb') as f:
            f.write(base_data)
            f.write(zip_data)

        if __name__ == "__main__":
            os.system("title Polyglot created!")
        print(f"\nSuccess! Polyglot created at: {output_path}")
        print(f"Updated {entries_updated} ZIP internal offsets.")
        if __name__ == "__main__":
            time.sleep(2.5)
            os.system(f"title {header_text}")
            time.sleep(1)


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    header_text = "HydraMeld"
    os.system(f"title {header_text}")
    if pyfiglet:
        title = pyfiglet.figlet_format(header_text, font="larry3d")
        print(title)
    else:
        print(f"\n--- {header_text} ---")

    print("Supported file types can be found at https://github.com/EarthWormsYas/HydraMeld/tree/main#supported-file-types\n\n")
    
    # Manually input source paths
    zp = input("Enter file path to source zip archive: ").strip(' "\'')
    base_file = input("Enter file path to source base file: ").strip(' "\'')
    
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Ask for output filename only
    out_name = input("Enter desired filename for the output polyglot file: ").strip(' "\'')
    
    if not base_file or not zp or not out_name:
        print("Error: All inputs are required.")
    elif not os.path.exists(base_file):
        print(f"Error: Base file not found at {base_file}")
    elif not os.path.exists(zp):
        print(f"Error: ZIP file not found at {zp}")
    else:
        # Construct output path in the script's directory
        output_path = os.path.join(script_dir, os.path.basename(out_name))
        create_polyglot(base_file, zp, output_path)
