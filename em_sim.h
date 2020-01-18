#include <math.h>
#include <stdlib.h>

float gaussE(float epsilon, float rho, omega o);

float gaussRho(float epsilon, float E, omega o);

float gaussEpsilon(float E, float rho, omega o);

typedef struct omega {float rho, float theta, float phi} omega;

