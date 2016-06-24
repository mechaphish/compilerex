
int transmit(int fd, char *buf, int n, int *addr) {
    int ret;

    ret = write(fd, buf, n);

    if (addr) {
        *addr = ret;
    }

    return ret < 0 ? -1 : 0;
}
