#include<stdio.h>
int main()
{
    int a[20][20];
    int n;
    int i,j;
    while(~scanf("%d",&n))
    {
        if(n!=0)
        {
            for(i=0;i<n;i++)
            {
                a[i][0]=1;
                a[i][i]=1;
            }
            for(i=2;i<n;i++)
            {
                for(j=1;j<i;j++)
                {
                    a[i][j]=a[i-1][j-1]+a[i-1][j];
                }
            }
            for(i=0;i<n;i++)
            {
                for(j=0;j<=i;j++)
                {
                    printf("%d",a[i][j]);
                    if(j!=i)
                    {
                        printf(" ");
                    }
                }
                printf("\n");
            }
        }
    }
    return 0;
}
