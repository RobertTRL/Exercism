#include "grains.h"

uint64_t square(uint8_t index) {
    // Geometric progression -> ar^n-1, a = 1st term (1), r = Ratio (2)
    if (index < 1 || index > 64) {
        return 0;
    }

    uint64_t grains = 1;

    for (uint8_t i = 1; i < index; ++i) {
        grains *= 2;
    }

    return grains;
}    

uint64_t total(void) {
    //  Geometric series = a(r^n - 1)/1
    uint64_t grains = 1;

    for (uint8_t i = 1; i <= 64; ++i) {
        grains *= 2; 
    }

    return grains - 1;
}