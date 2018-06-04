from cx_Freeze import setup, Executable
# run as python setup.py build
setup (name='Photo Dating Tool (CLI)', Version='0.1',
		executables=[Executable('PhotoDatingTool.py')])
		
