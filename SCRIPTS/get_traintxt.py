import glob

out_file = open('./train.txt', 'w')
path_img = './NEU-DET/IMAGES/' +'*.jpg'
for file in glob.glob(path_img):
    filename = file.split('/')[3]
    out_file.write('./data/obj/' + str(filename) + '\n')

