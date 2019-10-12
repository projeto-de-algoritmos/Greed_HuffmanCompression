import img_process
import huffman
import save_data

def main():
    image = img_process.ImageProcess('assets/tiger.bmp')
    huffman_obj = huffman.Huffman(image.img_array)
    save_data.SaveData('results/', image.img_array, huffman_obj.hist, huffman_obj.codes)

if __name__ == '__main__':
    main()
