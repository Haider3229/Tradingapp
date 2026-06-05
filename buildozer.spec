[app]
title = Trading App
package.name = tradingapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Only include core packages that have fully supported recipes
requirements = python3, kivy, requests, certifi, charset-normalizer, idna, urllib3

orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# Stable SDK and NDK Settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 1
