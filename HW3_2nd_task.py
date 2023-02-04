from multiprocessing import Pool
import logging


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def factorize(*number):
    result = []
    for i in number:
        count = 1
        res = []
        while count <= i:
            if (i / count).is_integer():
                res.append(count)
            count += 1
        result.append(res)
    return result

if __name__ == "__main__":
    with Pool(processes=2) as pool:
        logger.debug(pool.map(factorize, [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]))

