# PersianPad

**PersianPad** یک ویرایشگر متن فارسی دسکتاپ است که با زبان Python و کتابخانه PySide6 ساخته شده است.

هدف پروژه ایجاد یک محیط ساده و کاربردی برای نوشتن و ویرایش متن فارسی با پشتیبانی از فونت‌های فارسی و قابلیت‌های متداول ویرایش متن است.

---

## ویژگی‌ها

* پشتیبانی از نوشتار راست‌به‌چپ (RTL)
* استفاده از فونت‌های فارسی
* تغییر نوع فونت
* تغییر اندازه فونت
* Bold کردن متن
* Italic کردن متن
* Underline کردن متن
* باز کردن فایل
* ذخیره فایل
* ذخیره با نام جدید
* جستجو و جایگزینی متن
* معماری جداشده برای UI، Model، Controller و Service

---

## تکنولوژی‌های استفاده‌شده

* Python
* PySide6
* Qt Framework

---

## پیش‌نیازها

قبل از اجرای پروژه مطمئن شوید Python نصب است.

بررسی نسخه Python:

```bash
python --version
```

یا:

```bash
python -V
```

---

## نصب وابستگی‌ها

وابستگی‌های پروژه در فایل `requirements.txt` قرار دارند.

نصب کتابخانه‌ها:

```bash
pip install -r requirements.txt
```

---

## کتابخانه‌ها

### PySide6

کتابخانه رابط کاربری گرافیکی (GUI) بر پایه Qt برای ساخت برنامه‌های دسکتاپ.

نصب مستقیم:

```bash
pip install PySide6
```

بررسی نصب:

```bash
pip show PySide6
```

مشاهده تمام کتابخانه‌های نصب‌شده:

```bash
pip list
```

---

## اجرای برنامه

بعد از نصب وابستگی‌ها:

```bash
python main.py
```

---

## ساختار پروژه

```
PersianPad/
│
├── app/
│   ├── controllers/
│   ├── models/
│   ├── services/
│   ├── widgets/
│   └── windows/
│
├── resources/
│   └── fonts/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## نسخه

Current Version:

```
v1.0.0
```

---

## توسعه‌دهنده

PersianPad Project

```
```
