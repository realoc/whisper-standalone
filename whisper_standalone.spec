# -*- mode: python ; coding: utf-8 -*-

import whisper
import os

# Find where the assets are stored
whisper_dir = os.path.dirname(whisper.__file__)
assets_dir = os.path.join(whisper_dir, 'assets')


a = Analysis(
    ['whisper_standalone.py'],
    pathex=[],
    binaries=[],
    datas=[(assets_dir, 'whisper/assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='whisper_standalone',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,
)
