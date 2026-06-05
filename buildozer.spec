[app]
title = Trading App
package.name = tradingapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Android par chalne wali 100% stable core requirements
requirements = python3, kivy, requests, certifi, charset-normalizer, idna, urllib3

orientation = portrait
fullscreen = 0

# Internet permission for live tracking data
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# Locked stable SDK and NDK versions
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 1
