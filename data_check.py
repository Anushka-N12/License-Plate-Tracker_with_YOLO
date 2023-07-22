import os
def check(path):
    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        fname = os.path.basename(filepath).split('/')[-1]
        name, ext = fname.split('.')[0], fname.split('.')[1]
        newpath = os.path.join(path, name)
        if ext == 'txt':
            if os.path.exists(newpath+'.png') or os.path.exists(newpath+'.jpg') or os.path.exists(newpath+'.jpeg'):
                pass
            else:
                print(f'{name} does not have an image :(')
        elif ext in ['png', 'jpg', 'jpeg']:
            if os.path.exists(newpath+'.txt'):
                pass
            else:
                print(f'{name} does not have an annotation file :(')
    return 'Checked!'

path = r'C:\Users\anush\Downloads\data'
print(check(path))

#I manually deleted the ones found