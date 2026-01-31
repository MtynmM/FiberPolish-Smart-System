from gpiozero import PWMOutputDevice

class LightModel:
    def __init__(self, pin_number):
        """
        سازنده کلاس: اتصال مستقیم به پین رزبری پای
        """
        self.pin=pin_number
        self.current_brightness = 0
        
        # اتصال مستقیم به سخت‌افزار (بدون بلوک try/except اضافی)
        # فرکانس 1000 هرتز برای نور ثابت و بدون لرزش
        self.led = PWMOutputDevice(self.pin, frequency=1000)

    def set_brightness(self, value):
        """
        تنظیم شدت نور (0 تا 100)
        """
        # 1. اعتبارسنجی (Validation): جلوگیری از اعداد پرت
        if value < 0: value = 0
        if value > 100: value = 100
        
        self.current_brightness = value

        # 2. اعمال مستقیم به سخت‌افزار
        # تبدیل دامنه 0-100 (کاربر) به 0.0-1.0 (سخت‌افزار)
        self.led.value = float(value / 100.0)

    def get_brightness(self):
        """دریافت مقدار فعلی"""
        return self.current_brightness
    
    def close(self):
        """آزادسازی پین هنگام خروج از برنامه"""
        self.led.close()