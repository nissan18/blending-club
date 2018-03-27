import time
import logging
import sys


def main():
    print("Begin: " + __file__)

    # stderrHandler = 
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("output.txt")
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    
    sh = logging.StreamHandler(sys.stderr)
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)

    begin = time.time()
    """
    Grand Master Plan
    1. load all data, let's stick to just one dataSet for now
    2. build feature columns for dataSet
    3, build label(s) for dataSet
    4. train model
    5. save model
    """

    logging.info("before sleep")

    time.sleep(2)
    logging.info("after sleep")
    end = time.time()
    logger.debug("Elapsed {0} seconds".format(end - begin))
    print("end pipeline")


if __name__ == "__main__":
    main()
