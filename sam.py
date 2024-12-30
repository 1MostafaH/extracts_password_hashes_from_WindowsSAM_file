from impacket.examples.secretsdump import LocalOperations, SAMHashes
import io
import sys

# File paths for the uploaded SAM and SYSTEM files
sam_path = r'X:\sam\sam'   # Sam file path    
system_path = r'X:\sam\system'   # System file path  
output_hashes = r'X:\sam\sam_file.txt'   # output file path

# Initialize an empty variable to store output
hashes_output = ""

try:
    # Create LocalOperations and SAMHashes objects for extraction
    local_operations = LocalOperations(system_path)
    bootkey = local_operations.getBootKey()
    print(f"Bootkey: {bootkey}")
    
    sam_hashes = SAMHashes(sam_path, bootkey, isRemote=False)
    
    # Redirect stdout to capture the printed hashes
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    # Extract hashes
    sam_hashes.dump()
    
    # Get the printed hashes from stdout
    hashes_output = sys.stdout.getvalue()
    
    # Restore stdout
    sys.stdout = old_stdout
    
    print(f"Extracted Hashes: {hashes_output}")
    
    if hashes_output:
        # Save the hashes to a file
        with open(output_hashes, 'w') as f:
            f.write(hashes_output)
            print(f"Hashes written to file: {output_hashes}")
            hashes_output = f"Hashes extracted successfully and saved to: {output_hashes}"
    else:
        print("No hashes were extracted.")
    
    sam_hashes.finish()

except Exception as e:
    hashes_output = f"An error occurred: {str(e)}"
    print(hashes_output)

hashes_output
