[app]
title = Trading App
package.name = tradingapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# (list) Application requirements (Ismein trading bot ki saari sahi libraries add hain)
requirements = python3, kivy, requests, uritemplate, pyasn1, pycparser, cryptography, pyopenssl, certifi, idna, charset-normalizer, ccxt

orientation = portrait
fullscreen = 0

# (list) Permissions (Internet enabled for trading bot)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 31

# (int) Minimum API
android.minapi = 21

# (int) Android NDK API to use
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 1
