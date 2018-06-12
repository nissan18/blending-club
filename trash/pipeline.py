import time
import logging
import sys


def main():
    print("Begin: " + __file__)

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
    - load all data, let's stick to just one dataSet for now
    - build feature columns for dataSet
    - normalize feature columns
    - build label(s) for dataSet
    - take random subest of data to train model (optional)
    - train model
    - save model
    """

    logging.info("before sleep")

    time.sleep(2)
    logging.info("after sleep")
    end = time.time()
    logger.debug("Elapsed {0} seconds".format(end - begin))
    print("end pipeline")


if __name__ == "__main__":
    main()
