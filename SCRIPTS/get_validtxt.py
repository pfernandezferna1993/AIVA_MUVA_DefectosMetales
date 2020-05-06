import glob

out_file = open('./valid.txt', 'w')
path_img = './VALID/images/' +'*.jpg'
for file in glob.glob(path_img):
    filename = file.split('/')[3]
    out_file.write('./data/obj/' + str(filename) + '\n')

