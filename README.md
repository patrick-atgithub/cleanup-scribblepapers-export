# exportSP
cleanup scribblepapers (Windows) export to be imported into joplin.  
(python3)

## howto:

### text and rtf export / identify notes containing  images
- in ScribblePapers put all notes and folders in 1 top level folder e.g. `root`
- from ScribblePapers export `root` with all subfolders as  text
- from ScribblePapers export `root` with all subfolders as  rtf
- name these export folders `sp_txt` and `sp_rtf`
- place `cleanupSP.py` into same dir where `sp_txt` is
- run `cleanupSP.py`. converted text files (with export headers from ScribblePapers removed) can be found under `sp_fixed`
- log with missing images can be found in `sp_fixed\___Missing Images___.txt`
- text notes with missing images will contain a message in bold heading
- convert images manually and insert(see below)

### how to extract images and pdfs from rtf files
- make `sp_images` dir  where all saved images will go 
- open rtf files from `___Missing Images___.txt` in OpenOffice (which allows saving images)
- save images (right click on image and save)
- if image is an OLE-Object (frame around it): double click once more and export image
- if OLE object is pdf: open in scribblepapers and save as pdf or save as image with windows snippingtool 
- export fotos as jpg / drawings screenshots as gif or png (try which one is shorter). png is better if image contains gradients I think
 
### final step
- compare and think about size of `sp_fixed` + `sp_images`(now including all images and pdfs etc. of all the rtf files from the log) with the size of the `sp_rtf` (which contains the original data from ScribblePapers
- import all text files from `sp_txt` into Joplin
- drag all the images etc. from `sp_images` into the corresponding notes using `___Missing Images___.txt`
