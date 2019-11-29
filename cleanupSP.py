import os
from os.path import join

path_txt =   'sp_txt\\'     # INSERT PATHS HERE
path_rtf =   'sp_rtf\\'
path_fixed = 'sp_fixed\\'

offset = 7

def listdir(path, wildcard):   #list with subdirs and 1 wildcard
  len_path = len(path)
  dirlist = []
  for root, dirs, files in os.walk(path):
    for f in files: 
      if f.endswith(wildcard):                  # filter wildcard and spare _fixed_
        dirlist.append(join(root[len_path:], f)) # relelativ pathlisting  
  return dirlist

def logit(searchfor, line, msg, log, fname):
  if searchfor in l:
    log.append('{: <18}{}'.format(msg, fname) )
    return True
  return False
    
if not os.path.exists(path_txt):
  print("path not found ...")
  print("place this script into same folder where 'sp_txt' and 'sp_rtf' can be found...\nexiting")
  exit()
    
log = []
files_with_images = []

for fname in  listdir(path_rtf, '.rtf'):  # check all rtf files for images
  with open(join(path_rtf, fname), 'r') as f:
    textlines = f.readlines()
    
    for l in textlines:
      if   logit('\\jpegblip', l, 'found JPG in:', log, fname):
        files_with_images.append(fname)
        break
      elif logit('\\pngblip', l, 'found PNG in:', log, fname):
        files_with_images.append(fname)
        break
      elif logit('\\wmetafile', l, 'WinMetafile in:', log, fname):
        files_with_images.append(fname)
        break
      elif logit('\\blip', l, 'blip in:', log, fname):
        files_with_images.append(fname)
        break

for fname in listdir(path_txt, '.txt'):    # rewrite all txt files without scribblepapers export header
  fname_new = join( path_fixed, fname ) # write everything to '_fixed_' dir
  
  if not os.path.exists(os.path.dirname(fname_new)):
    os.makedirs(os.path.dirname(fname_new))

  with open(join(path_txt, fname), 'r') as f:
    textlines = f.readlines()
  
  with open(fname_new, 'w', encoding='utf-8') as f:
    for i, l in enumerate(textlines):
      if i >= offset:
        f.write(l)
    
    if fname.replace('.txt','.rtf') in files_with_images:
      f.write('\n\n# ADD MISSING IMAGES FROM LOG\n')
      

print('all txt files have been stripped from export headers, marked if missing an image, written to dir: ', path_fixed, '\n')  
print('extract images from following files and insert into Joplin notes:\n')

for l in log:    #print log
  print(l)

with open(join(path_fixed, '___Missing Images___.txt'), 'w', encoding='utf-8') as f: # write log
  for l in log:
    f.write(l+'\n')
  print('\nlog written to ', path_fixed)
  
  
  

        
      
  