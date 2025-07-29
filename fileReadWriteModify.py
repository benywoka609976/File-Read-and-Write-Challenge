def process_file(input_filename, output_filename):
    """
    Reads a file, converts its content to uppercase, and writes to a new file.
    Handles common file-related errors.
    
    Args:
        input_filename (str): Name of the input file
        output_filename (str): Name of the output file
    
    Returns:
        bool: True if processing was successful, False otherwise
    """
    try:
        # Read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify content (convert to uppercase as an example)
        modified_content = content.upper()
        
        # Write to output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}'")
        return True
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}' or '{output_filename}'.")
        return False
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return False

def main():
    """Main function to get user input and process the file."""
    print("File Read & Write Processor")
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")
    
    process_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
