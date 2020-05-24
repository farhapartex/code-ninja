#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int cs, test, n, give_treat, given_treat;
    cs = 1;
    while (scanf("%d", &test) == 1)
    {
        give_treat = given_treat = 0;

        if (test == 0)
        {
            break;
        }
        for (int i = 1; i <= test; i++)
        {
            scanf("%d", &n);
            if (n >= 1)
            {
                give_treat++;
            }
            else
            {
                given_treat++;
            }
        }

        printf("Case %d: %d\n", cs++, (give_treat - given_treat));
    }
}
