
#include <stdio.h>
#include <stdbool.h>
struct tree{
    bool isleft,isright;
    struct tree left,right;
}