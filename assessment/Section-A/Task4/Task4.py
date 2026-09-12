class DiskWriteError(Exception):
    pass


file = None

try:

    file = open("orders_log.txt", "a")
    file.write("Order completed successfully\n")

except OSError as error:

    raise DiskWriteError(
        "Unable to write order log"
    ) from error

finally:

    if file is not None:
        file.close()