#ifndef STDIO_H_
#define STDIO_H_

typedef int FILE;

#define stdin  0
#define stdout 1
#define stderr 2

// fprintf will be fdprintf
#define fprintf(stream, format, ...) fdprintf((int)stream, format,__VA_ARGS__) 
#define vfprintf(stream, format, ap) fdprintf((int)stream, format, ap)
#define fputs(string, stream) fdprintf((int)stream, "%s", string)
#define fputc(c, stream) fdputc(c, (int)stream)
#define fflush(x) { }

#endif /* !STDIO_H_ */
