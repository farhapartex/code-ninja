#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int a, b, c, d;
    int res;

    while (scanf("%d %d %d %d", &a, &b, &c, &d) == 4)
    {
        res = 0;
        if (a == 0 && b == 0 && c == 0 & d == 0)
        {
            break;
        }
        if (a < b)
            res += (40 - (b - a));
        else
            res += (a - b);
        if (b > c)
            res += (40 - (b - c));
        else
            res += (c - b);
        if (c < d)
            res += (40 - (d - c));
        else
            res += (c - d);

        printf("%d\n", 720 + 360 + (res * 9));
    }

    return 0;
}