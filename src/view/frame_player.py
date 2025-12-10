import os
import tkinter as tk
from PIL import Image, ImageTk

class AnimatedFrameLabel(tk.Label):
    """
    لیبلی که تصاویر را از یک پوشه می‌خواند و مثل ویدیو پخش می‌کند.
    """
    def __init__(self, master, frame_folder, fps=24, **kwargs):
        super().__init__(master, **kwargs)
        self.frame_folder = frame_folder
        self.delay = int(1000 / fps)  # محاسبه سرعت پخش
        self.frames = []
        self.current_frame = 0
        self.running = False

        try:
            self._load_frames()
            self._start_animation()
        except Exception as e:
            print(f"Error loading frames: {e}")
            self.configure(text="Video Error", bg="black", fg="white")

    def _load_frames(self):
        # لیست کردن تمام فایل‌های عکس و مرتب‌سازی آنها
        valid_exts = {".png", ".jpg", ".jpeg", ".bmp"}
        # لیست فایل‌ها را می‌گیریم و حتما SORT می‌کنیم تا به ترتیب پخش شوند
        files = sorted([
            f for f in os.listdir(self.frame_folder) 
            if os.path.splitext(f)[1].lower() in valid_exts
        ])

        if not files:
            raise FileNotFoundError("No images found!")

        for f in files:
            path = os.path.join(self.frame_folder, f)
            img = Image.open(path)
            # نکته: اگر تصاویر هم‌اندازه صفحه نیستند، اینجا می‌توان resize کرد:
            # img = img.resize((1024, 600)) 
            self.frames.append(ImageTk.PhotoImage(img))

    def _start_animation(self):
        self.running = True
        self._animate()

    def _animate(self):
        if not self.running or not self.frames:
            return

        # نمایش فریم
        self.configure(image=self.frames[self.current_frame])
        
        # رفتن به فریم بعد (چرخشی)
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        
        # تکرار
        if self.winfo_exists():
            self.after(self.delay, self._animate)