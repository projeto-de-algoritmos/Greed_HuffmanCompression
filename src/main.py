import img_process
import huffman
import save_data
import benchmark

def main():
    image_path = input('>> Caminho para a imagem com extensão: ')
    image = img_process.ImageProcess(image_path)
    huffman_obj = huffman.Huffman(image.img_array)
    save_data.SaveData('results/', image.img_array, huffman_obj.hist, huffman_obj.codes)
    bench = benchmark.Benchmark(image, image.img_array, huffman_obj.codes)
    print('\nRESULTADOS PODEM SER VISUALIZADOS EM "/results"')

if __name__ == '__main__':
    main()
