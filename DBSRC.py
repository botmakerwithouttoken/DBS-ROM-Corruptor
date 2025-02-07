import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import random
from PIL import Image, ImageTk

def corrupt_file():
    original_filepath = file_path_entry.get()
    try:
        start_byte = int(start_byte_entry.get())
        end_byte = int(end_byte_entry.get())
        block_size = int(block_size_entry.get())
        block_space = int(block_space_entry.get())
        add_value = int(add_value_entry.get())
        engine = engine_var.get()

        if not os.path.exists(original_filepath):
            raise FileNotFoundError("Original file not found.")

        if not all(isinstance(x, int) and x >= 0 for x in [start_byte, end_byte, block_size, block_space, add_value]):
            raise ValueError("All values must be non-negative integers.")

        if start_byte >= end_byte:
            raise ValueError("Start byte must be less than end byte.")

        file_size = os.path.getsize(original_filepath)
        if end_byte > file_size:
            raise ValueError("End byte is beyond file size.")

        filename, ext = os.path.splitext(os.path.basename(original_filepath))
        corrupted_filepath = os.path.join(os.path.dirname(original_filepath), f"{filename}_corrupted{ext}")
        shutil.copy2(original_filepath, corrupted_filepath)

        with open(corrupted_filepath, "r+b") as f:
            f.seek(start_byte)
            current_byte = start_byte

            while current_byte < end_byte:
                block_start = current_byte
                block_end = min(current_byte + block_size, end_byte)

                for i in range(block_start, block_end):
                    original_byte = f.read(1)
                    if original_byte:
                        original_byte_int = ord(original_byte)

                        if engine == "Incrementer":
                            new_byte = (original_byte_int + add_value) % 256
                        elif engine == "Scrambler":
                            new_byte = random.randint(0, 255)
                        elif engine == "Smoother":
                            prev_byte = f.read(1)
                            if prev_byte:
                                f.seek(i-1)
                                prev_byte = ord(f.read(1))
                                new_byte = (original_byte_int + prev_byte ) // 2
                            else:
                                new_byte = original_byte_int
                        elif engine == "Blender":
                            new_byte = (original_byte_int + random.randint(-add_value, add_value)) % 256
                        else:
                            new_byte = original_byte_int

                        f.seek(i)
                        f.write(bytes([new_byte]))
                    else:
                        break

                current_byte = block_end + block_space
                f.seek(current_byte)

        messagebox.showinfo("Success", f"File corrupted and saved as: {corrupted_filepath}")

    except FileNotFoundError:
        messagebox.showerror("Error", "Original file not found.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_add_value_label(event=None):
    engine = engine_var.get()
    if engine in ("Scrambler", "Smoother", "Blender"):
        add_value_label.config(text="Shift Right/Blend Range:")
    else:
        add_value_label.config(text="Add Value:")


root = tk.Tk()
root.title("DBS ROM Corruptor")

try:
    image_path = (r("C:\Users\CCE\Pictures\Capture.JPG"))
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.image = photo
    image_label.pack(pady=10)
except FileNotFoundError:
    messagebox.showerror("Error", "Image not found. Make sure 'image.png' is in the same directory.")
except Exception as e:
    messagebox.showerror("Error", f"Error loading image: {e}")

file_path_label = tk.Label(root, text="File Path:")
file_path_label.pack()
file_path_entry = tk.Entry(root, width=50)
file_path_entry.pack()

def browse_file():
    filepath = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, filepath)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

start_byte_label = tk.Label(root, text="Start Byte:")
start_byte_label.pack()
start_byte_entry = tk.Entry(root)
start_byte_entry.pack()
start_byte_entry.insert(0, "0")

end_byte_label = tk.Label(root, text="End Byte:")
end_byte_label.pack()
end_byte_entry = tk.Entry(root)
end_byte_entry.pack()
end_byte_entry.insert(0, "1024")

block_size_label = tk.Label(root, text="Block Size:")
block_size_label.pack()
block_size_entry = tk.Entry(root)
block_size_entry.pack()
block_size_entry.insert(0, "1")

block_space_label = tk.Label(root, text="Block Space:")
block_space_label.pack()
block_space_entry = tk.Entry(root)
block_space_entry.pack()
block_space_entry.insert(0, "0")

add_value_label = tk.Label(root, text="Add Value:")
add_value_label.pack()
add_value_entry = tk.Entry(root)
add_value_entry.pack()
add_value_entry.insert(0, "1")

engine_var = tk.StringVar(value="Incrementer")
engine_label = tk.Label(root, text="Engine:")
engine_label.pack()
engine_menu = tk.OptionMenu(root, engine_var, "Incrementer", "Scrambler", "Smoother", "Blender", command=update_add_value_label)
engine_menu.pack(pady=5)

corrupt_button = tk.Button(root, text="Corrupt", command=corrupt_file)
corrupt_button.pack(pady=10)

root.mainloop()