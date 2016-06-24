#include <libcgc.h>
#include <mymath.h>
#include <stdint.h>

double floor( double val )
{
    if ( val > 0.0 )
        return rint( val + 0.5 ) - 1.0;
    else if ( val < 0.0 )
        return rint( val - 0.5 ) + 1.0;
    else
        return 0.0;
}

double round_away_from_zero( double val )
{
    if ( val > 0.0 )
        return rint( val + 0.5 );
    else if ( val < 0.0 )
        return rint( val - 0.5 );
    else
        return 0.0;
}

double round( double val, double n )
{
    // Round to n digits
    n = rint( n );

    double high_pow10 = pow( 10, n );
    double low_pow10 = pow( 10, -n );

    return (round_away_from_zero( val * high_pow10 ) * low_pow10);
}
