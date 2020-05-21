#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
int seconds = 0;
int minutes = 0;
int hours = 0;

void *h(){
	while(1){
		if (minutes == 60){
			hours++;
			minutes = 0;
		}
	}
}
void *m(){
	while(1){
		if (seconds ==60){
			minutes++;
			seconds = 0;
		}
	}
}

void *s(){
	while(1){
		sleep(1);
		seconds++;
	}
}
void *answer(){
	while(1){
		if(hours>10){
			printf("\r%d:",hours);
		}
		else{
			printf("\r0%d:",hours);
		}
		if(minutes>10){
			printf("%d:",minutes);
		}
		else{
			printf("0%d:",minutes);
		}
		if(seconds>10){
			printf("%d",seconds);
		}
		else{
			printf("0%d",seconds);
		}
	}
}


int main(){
	printf("Starting timer\n");
	pthread_t t1,t2,t3,t4;
	int e1,e2,e3,e4;
	pthread_create(&t1,NULL,s,NULL);
	pthread_create(&t2,NULL,m,NULL);
	pthread_create(&t3,NULL,h,NULL);
	pthread_create(&t4,NULL,answer,NULL);
	e1 = pthread_join(t1,NULL);
	e2 = pthread_join(t2,NULL);
	e3 = pthread_join(t3,NULL);
	e4 = pthread_join(t4,NULL);
	return 0;
}
