class Benchmark:
    def __init__(self, image, img_array, codes):
        self.real_image_size = image.img_height*image.img_width*8
        self.total = self.compute_bits_number(img_array, codes)
        self.bits_comprimidos = self.real_image_size-self.total
        self.compute_optimization()

    def compute_optimization(self):
        print('Tamanho em bits da imagem original: {}'.format(self.real_image_size))
        print('Tamanho em bits da imagem comprimida: {}'.format(self.total))
        print('Quantidade de bits comprimidos: {}'.format(self.bits_comprimidos))
        print('Taxa de compressão: {:.6f}'.format(self.bits_comprimidos/self.real_image_size))

    def compute_bits_number(self, img_array, codes):
        total = 0
        for row in img_array:
            for value in row:
                total += len(codes[value])
        return total
                
        
