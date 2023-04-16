from cx_Freeze import setup, Executable

# define your application's setup details here

executables = [
    Executable('temp.py', base='Win32GUI')
]

setup(name='temperatureconverter',
      version='1.0',
      description='My application',
      executables=executables)
