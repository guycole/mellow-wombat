import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger("wombat")

def main():
    while True:
        logger.info("wombat active")
        time.sleep(15)

if __name__ == "__main__":
    main()
