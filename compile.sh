# copied from Jacopo's stuff

# Based on https://github.com/CyberGrandChallenge/cb-testing/blob/master/cgc-cb.mk
# '-Wl,-mcgc_i386' is my addition, though, so that 'clang -o exe' works. [J]

if [ "$#" -lt 1 ]; then
    echo "usage $0 <clang commands>";
    exit 1
fi

export CC=./bin/clang
export LD=./bin/ld
export CXX=./bin/clang++
export OBJCOPY=./bin/objcopy

export LDFLAGS="-nostdlib -static -Wl,-mcgc_i386 $LDFLAGS"
export  CFLAGS="-nostdlib -fno-builtin -nostdinc -isystem./include $CFLAGS"
export LDLIBS="-L./lib -lcgc $LDLIBS"

export PATH="./bin:$PATH"

function compile() {
    $CC -Ilib/ \
        -std=gnu99 -Wall -Wextra -Wshadow -Wwrite-strings -Wpointer-arith -Wstrict-overflow=4  \
        $CFLAGS $LDFLAGS $@ $LDLIBS;
}

compile $@
