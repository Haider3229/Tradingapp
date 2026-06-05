[app]

title = Trading App
package.name = tradingapp
package.domain = org.test

source.dir = .
source.include_exts = py

version = 1.0

requirements = python3,kivy,requests

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
