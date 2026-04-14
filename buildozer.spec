[app]

# (str) Title of your application
# تم تعديل الاسم للإنجليزية كما طلبت
title = Ibrahim Al-Malsi Zamil

# (str) Package name
package.name = zamil_app

# (str) Package domain (needed for android/ios packaging)
package.domain = com.alslbh

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
# تأكدنا من تضمين ملفات الصوت mp3 والخطوط ttf
source.include_exts = py,png,jpg,kv,atlas,ttf,mp3

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*

# (str) Application versioning
version = 1.0

# (list) Application requirements
# تمت إضافة المكتبات الضرورية لدعم اللغة العربية وواجهات Material Design
requirements = python3, kivy==2.3.0, kivymd==1.2.0, arabic-reshaper, python-bidi

# (str) Icon of the application
# تم ربط الأيقونة بالملف app_icon.png الموجود في مجلدك الرئيسي
icon.filename = %(source.dir)s/app_icon.png

# (str) Presplash of the application
# صورة تظهر أثناء تحميل التطبيق
presplash.filename = %(source.dir)s/assets/images/avatar.png

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android app theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# رفع مستوى اللوج لتتمكن من رؤية الأخطاء بالتفصيل إذا حدثت
log_level = 2
warn_on_root = 1