
[app]

title = Pocket Notepad
package.name = pocketnotepad
package.domain = org.example

source.dir = .
source.include_exts = py,txt

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 36
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True

p4a.branch = master


[buildozer]

log_level = 2
