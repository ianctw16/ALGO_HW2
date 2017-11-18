# -*- mode: python -*-

block_cipher = None


a = Analysis(['algorithm_HW2_b.py'],
             pathex=['/home/ian/文件/GitHub/ALGO_HW2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='algorithm_HW2_b',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
