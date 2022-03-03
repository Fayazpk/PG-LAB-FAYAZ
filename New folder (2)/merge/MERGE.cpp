//1.Write a program to merge two sorted arrays

#include<stdio.h>

int main()
{
	int a[20],b[20],c[20],n,m,i,j,k;
	
	printf("Enter the size of first array : ");
	scanf("%d",&n);
	
	printf("Enter the elements of first array :\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}

	printf("Enter the size of second array : ");
	scanf("%d",&m);
	
	printf("Enter the elements of second array :\n");
	for(j=0;j<m;j++)
	{
		scanf("%d",&b[j]);
	}
	
i=0,j=0;

while (i<n && j<m)
{
	if(a[i]<b[j])
	{
		c[k]=a[i];
		i++;
	}
	else if(b[j]<a[i])
	{
		c[k]=b[j];
		j++;
	}
	else if(b[j]==a[i])
	{
		c[k]=a[i];
		i++;
		j++;
	}
	k++;
}

for(;i<n;i++)
{
	c[k]=a[i];
	k++;
}

for(;j<m;j++)
{
	c[k]=b[j];
	k++;
}

printf("Merged array is \n");
for(i=0;i<k;i++)
{
	printf("%d ",c[i]);
}
}
