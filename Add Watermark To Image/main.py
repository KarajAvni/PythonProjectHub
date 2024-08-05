import os
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        self.image_path = None

        self.label = Label(root, text="No image selected")
        self.label.pack(pady=10)

        self.upload_button = Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.watermark_button = Button(root, text="Add Watermark", command=self.add_watermark, state="disabled")
        self.watermark_button.pack(pady=10)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if self.image_path:
            self.label.config(text="Image selected: " + os.path.basename(self.image_path))
            self.watermark_button.config(state="normal")

    def add_watermark(self):
        if self.image_path:
            original_image = Image.open(self.image_path)

            # Your watermark image path
            watermark_path = "path/to/watermark.png"
            watermark = Image.open(watermark_path)

            # You may need to adjust the position based on your requirements
            position = ((original_image.width - watermark.width) // 2, (original_image.height - watermark.height) // 2)

            original_image.paste(watermark, position, watermark)
            output_path = "path/to/output/image_with_watermark.png"
            original_image.save(output_path)

            self.label.config(text="Watermark added. Output saved as " + os.path.basename(output_path))

if __name__ == "__main__":
    root = Tk()
    app = WatermarkApp(root)
    root.mainloop()

