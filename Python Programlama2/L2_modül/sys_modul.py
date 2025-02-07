import sys

print(sys.argv)
print(sys.executable)
print(sys.platform)
print(sys.version)
sys.stderr.write("hata\n")  # standart hata konumu
sys.exit()
