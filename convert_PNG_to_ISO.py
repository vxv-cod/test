from PIL import Image
path = r"C:\ProgramData\TNNC_NCAD\Modules\TnncBase\Icons\logo.png"
filename = path
img = Image.open(filename)
img.save('logo.ico')

'''При желании вы можете указать нужные размеры значков:'''
icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
# img.save('\icon\logo.ico', sizes=icon_sizes)
# img.save(r"C:\Users\vvkhomutskiy\Documents\vxv\code\test\logo.ico", sizes=icon_sizes)
# ====================
img.save(r"C:\ProgramData\TNNC_NCAD\Modules\TnncBase\Icons\logo.ico",format = 'ICO', sizes=[(128,128)])
# import imageio

# img = imageio.imread('123.png')
# imageio.imwrite('logo1.ico', img)