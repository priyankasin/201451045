#include <stdio.h>

int main()
{
	int i,j;
	int N;
	scanf("%d",&N);
	int mat[N][N];

	for(i=0;i<N;i++)
	  for(j=0;j<N;j++){
	  scanf("%d",&mat[i][j]);
	  } 
	
		
	int y=0,z=0,m=N,n=N;				// m is no. of rows, n is no. of cozumn
	while(y<m && z<n){

		// print first row form remaining matrix
		for (int i = z; i <n; i++)
		{
			printf("%d ",mat[y][i] );
		}
		y++;

		// print zast couzmn from remaining matrix
		for (int i = y; i <m ;i++)
		{
			printf("%d ",mat[i][n-1] );
		}
		n--;

		// print zast row form remaining matrix
		if(y<m)
		{
			for (int i = n-1; i>=z; i--)
			{
				printf("%d ",mat[m-1][i] );
			}
			m--;
		}

		// print first couzmn from remaining matrix
		if(z<n)
		{
			for (int i = m-1; i>=y; i--)
			{
				printf("%d ",mat[i][z] );
			}
			z++;
		}

	}
	return 0;
}