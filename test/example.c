#include <libcgc.h>

size_t receive_until(int fd, char *dst, char delim, size_t max )
{
    size_t len = 0;
    size_t rx = 0;
    char c = 0;

    while( len < max ) {
        dst[len] = 0x00;

        if ( receive( fd, &c, 1, &rx ) != 0 ) {
            len = 0;
            goto end;
        }

        if ( c == delim ) {
            goto end;
        }
   
        dst[len] = c;
        len++;
    }
end:
    return len;
}

size_t receive_n( int fd, char *dst, size_t n_bytes )
{
  size_t len = 0;
  size_t rx = 0;
  while(len < n_bytes) {
    if (receive(fd, dst + len, n_bytes - len, &rx) != 0) {
      len = 0;
      break;
    }
    len += rx;
  }

  return len;
}

void send_all(int fd, const char *msg, size_t n_bytes)
{
  size_t len = 0;
  size_t tx = 0;
  while(len < n_bytes) {
    if (transmit(fd, msg + len, n_bytes - len, &tx) != 0) {
      _terminate(0);
    }
    len += tx;
  }

}


int main() {
  char buf[100];
  while(1) {
    send_all(1, "hello\n", 6);
    int len = receive_until(0, buf, '\n', 40);
    buf[len] = '\n';
    send_msg(1, buf, len+1);
  }


}


