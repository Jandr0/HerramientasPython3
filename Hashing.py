import hashlib


try:
    ruta = input('Indica la ruta del fichero y su nombre: ' )
    BUFFSIZE = 4096

    sha1_hash = hashlib.sha1()
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()

    with open(ruta, 'rb') as objeto_fichero:
        buff = objeto_fichero.read(BUFFSIZE)
        while buff:
            sha1_hash.update(buff)
            sha256_hash.update(buff)
            md5_hash.update(buff)
            buff = objeto_fichero.read(BUFFSIZE)

    print('sha1-> ', sha1_hash.hexdigest())
    print('sha224->', sha256_hash.hexdigest())
    print('md5->', md5_hash.hexdigest())
except:
    FileNotFoundError: print('No se ha encontrado el archivo o no existe')
