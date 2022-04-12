#include<stdio.h>
#include<math.h>
/* v=rate at which height is decreasing,s=rate at which distance of foot from wall is increasing
,x is distance of foot from wall at a particular time,l is length of rod,h is height at which rod is 
touching the wall*/
int main(){
float v,s,x,l,h;
scanf("%f", &x);
scanf("%f", &l);
scanf("%f", &s);
//from pythagoreas theorem h=(l^2-x^2)^1/2
h=sqrt((l*l)-(x*x));
//from formula h*v=-x*s
v=-x*s/h;
printf("%f",v);
}
