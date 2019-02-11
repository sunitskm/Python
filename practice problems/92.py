import glob
python_files = glob.glob1(r"C:\Users\Lenovo\Downloads\SELT\Project\Files","*.py")
print(len(python_files))
recursive_python_files = glob.glob(r"C:\Users\Lenovo\Downloads\SELT\Project\subdirs\**\*py",recursive=True)
print(len(recursive_python_files))
