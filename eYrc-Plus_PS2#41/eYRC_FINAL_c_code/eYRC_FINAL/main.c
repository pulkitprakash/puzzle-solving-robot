/*
 * GccApplication12.cpp
 *
 * Created: 2/25/2016 11:17:27 PM
 *  Author: Pulkit007
 */ 


/*
*Team Id: 41
*Author: Pulkit Prakash
*Filename: main
*Theme: Eyrc-Plus-Ps2
*Functions: Calculate_dx_dy()
			check_head_turn(int a)
			path(int a, int b)
			find_coorD1(int a)
			go_to_N2()
			N2_to_N3()
			find_coorD2(int a)
			N3_to_targetNo()
			dest_to_N3()
			N3_to_N2()
*Global Variables:
					int D1[12];
					int A_Traversed_D1[4][10];
					int D2[10];
					int NOx,NOy,STx=2,STy=0;
					int C_N_D1,C_N_D1_x,C_N_D1_y;
					int ic=0;
					int p=0;
					int dx,dy;
					char head='N';
					int z;
					int Dest_x,Dest_y;
					int aise;
					unsigned char Left_white_line = 0;
					unsigned char Right_white_line = 0;
					unsigned char Center_white_line = 0;
					unsigned char ir = 0;

*
*/
#define F_CPU 14745600
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <math.h>
#include <stdlib.h>
#include<avr/eeprom.h>
unsigned char Left_white_line = 0;
unsigned char Right_white_line = 0;
unsigned char Center_white_line = 0;
unsigned char ir = 0;
/* inputs  */
int D1[12];
int A_Traversed_D1[4][10];
int D2[10];
int NOx,NOy,STx=2,STy=0;
int C_N_D1,C_N_D1_x,C_N_D1_y;
int ic=0;
int p=0;
int dx,dy;
char head='N';
int z;
int Dest_x,Dest_y;
int aise;
#include "header.h"
//int y=5;
/* inputs  */

/*
* Function Name: <Calculate_dx_dy>
* Input : < NONE>
* Output : < NONE>
* Logic: <calculates dx and dy for the current number by finding the appropriate side >
* Example Call: <Calculate_dx_dy();>
*/
/*function define*/
void Calculate_dx_dy()
{
 int side_x=0,side_y=0;
 if(C_N_D1_x==STx && C_N_D1_y-STy==1)
 {
	 side_x=C_N_D1_x;
	 side_y=(C_N_D1_y-1);
 }
 else if(C_N_D1_y==STy && C_N_D1_x-STx==1)
 {
	 side_x=(C_N_D1_x-1);
	 side_y=C_N_D1_y;
 }
 else if (C_N_D1_x<=STx)
 {
	  if (C_N_D1_y>STy)
	  {
	   side_x=(C_N_D1_x+1);
	   side_y=C_N_D1_y;
	  }
	  else
	  {
	   side_x=C_N_D1_x;
	   side_y=(C_N_D1_y)+1;   
	  }
 }
 else
 {
	  if (C_N_D1_x<2)
	  {
	   side_x=(C_N_D1_x+1);
	   side_y=C_N_D1_y;
	  }
	  else if(C_N_D1_y<=STy)
	  {
		  side_x=(C_N_D1_x-1);
		  side_y=C_N_D1_y;
	  }	  
	  else
	  {
	   side_x=C_N_D1_x;
       side_y=(C_N_D1_y)-1;
	  }
 }
 dx=side_x-STx;
 dy=side_y-STy;
}

/*
* Function Name: <check_head_turn(int a)>
* Input : < integer a -> stores the value to be travelled  by the bot >
* Output : < NONE>
* Logic: < find the turn to be taken by the bot by compairing the input value to the dx and dy and also by less or greater than zero and setting the vallue of head accordingly >
* Example Call: <check_head_turn(TF);>
*/
void check_head_turn(int a)
{
char ans;
if(a==dx&&a<0)
 {
	 ans='ndx';
	 
	 if(head=='N')
		 turn(1,0);
	 if(head=='S')
		 turn(0,0);
	 /*if(head=='W')
		 cout<<"no turn\n";*/
     if(head=='E')
		 turn(1,1);
	 head='W';
	 STx=STx+dx;
 }
if(a==dx&&a>0)
 {
	 ans='pdx';
	 
	 if(head=='N')
		 turn(0,0);
	 if(head=='S')
		 turn(1,0);
	 if(head=='W')
		 turn(1,1);
     /*if(head=='E')
		 cout<<"no_turn\n";*/
	 head='E';
	 STx=STx+dx;
 }
if(a==dy&&a<0)
 {
	 ans='ndy';
	 
	 if(head=='N')
		 turn(1,1);
	 /*if(head=='S')
		 cout<<"no_turn\n";*/
	 if(head=='W')
		 turn(1,0);
     if(head=='E')
		 turn(0,0);
	 head='S';
	 STy=STy+dy;
 }
if(a==dy&&a>0)
 {
	 ans='pdy';
	 
	 /*if(head=='N')
		 cout<<"no_turn\n";*/
	 if(head=='S')
		 turn(1,1);
	 if(head=='W')
		 turn(0,0);
     if(head=='E')
		 turn(1,0);
	 head='N';
	 STy=STy+dy;
 }
}

/*
* Function Name: <path(int a, int b)>
* Input : < integer a -> stores the dx value 
*           integer b -> stores the dy value>
* Output : < NONE>
* Logic: < tells the bot where to go by going through series of processe of travelling straight ,turning, travel till block,etc >
* Example Call: <path(dx, dy);>
*/
void path(int a, int b)
{
	int TF=0, TS=0;
	int odd,even;
	if(dx==0 && dy==0)
	{
		//travel(1);
		//key_forward=1;
		//velocity(250,255);
		//forward();
		//forward_mm(120);		
		turn(1,1);//turn 180
		if(head=='S')
		head='N';
		else if (head=='N')
		head='S';
		else if (head=='E')
		head='W';
		else if(head=='W')
		head='E';
		velocity(245,250);
		//travel_till_block(1);
		backward();
		backward_mm(60);

	}	
	else if (dx!=0 && dy!=0)
	{/*both non zero*/
		if(dx%2!=0 && dy%2!=0)
		{
			/*both odd*/
			if (STx%2!=0)
			{
				TF=dx;
				TS=dy;
				aise=dy;
				dy=dx+1;
			}
			else
			{
				TF=dy;
				TS=dx;
				aise=dx;
				dx=dy+1;
			}
			check_head_turn(TF);
			if(TF==dx)
			{
			dy=aise;
			aise=dx;
			dx=dy+1;
			}
			else
			{
				dx=aise;
				aise=dy;
				dy=dx+1;
			}
			travel(abs(TF));
			check_head_turn(TS);
			if(TS==dx)
				dy=aise;
			else
				dx=aise;
				
	        if(z!=0 && z<20)
	        travel_till_block(abs(TS));
	        else if(z==0)
	        travel(abs(TS));
	        else
	        travel_till_bucket(abs(TS));
		}
		else if(dx%2==0 && dy%2==0)
		{
			/*both even*/
			if(STx%2!=0)
			{
				  TF=dx;
				  TS=dy;
				  aise=dy;
				  dy=dx+1;
			}
			else
			{
				  TF=dy;
				  TS=dx;
				  aise=dx;
				  dx=dy+1;
			}
			check_head_turn(TF);
			if(TF==dx)
				STx=STx-dx+1;
			else
			    STy=STy-dy+1;	
			travel(1);
			if(TF==dx){
				  dy=aise;
				  aise=dx;
			      dx=dy+1;}
			else{
				  dx=aise;
				  aise=dy;
			      dy=dx+1;}			
			check_head_turn(TS);
			travel(abs(TS));
			if(TS==dy){
				  dx=aise;
				  aise=dy;
			      dy=dx+1;}
			else{
				  dy=aise;
				  aise=dx;
			      dx=dy+1;}			
			check_head_turn(TF);
			if(TS==dx)
			  dx=aise;
			else
			  dy=aise;			
			if(TF==dx)
				STx=STx-1;
			else
				STy=STy-1;
			if(TF<0){
			  TF=abs(TF)-1;
			  TF=TF*-1;}
			else
			  TF=TF-1;
	        if(z!=0 && z<20)
	        travel_till_block(abs(TF));
	        else if(z==0)
	        travel(abs(TF));
	        else
	        travel_till_bucket(abs(TF));
		}
		else
		{
			/*odd + even */
			if(dx%2!=0 && dy%2==0)
			{
				odd=dx;
				even=dy;
			}
			else
			{
				odd=dy;
				even=dx;
			}
			if (STx%2==0 && STy%2==0)
			{
				TF=even;
				TS=odd;
			}
			else
			{
				TF=odd;
				TS=even;
			}
			check_head_turn(TF);
			travel(abs(TF));
			check_head_turn(TS);
	        if(z!=0 && z<20)
	        travel_till_block(abs(TS));
	        else if(z==0)
	        travel(abs(TS));
	        else
	        travel_till_bucket(abs(TS));
		}


	}
	else
	{/*one is zero*/
		if (dx==0)
		{
			if(STx%2!=0)
			{
				if(head=='E')
					STx=STx+1;
				else if(head=='W')
				    STx=STx-1;
				travel(1);
				check_head_turn(dy);
				travel(abs(dy));
				dx=C_N_D1_x-STx;
				check_head_turn(dx);
	            if(z!=0 && z<20)
				travel_till_block(abs(dx));
				else if(z==0)
				travel(abs(dx));
				else
				travel_till_bucket(abs(dx));
			}
			else
			{
				check_head_turn(dy);
	            if(z!=0 && z<20)
	            travel_till_block(abs(dy));
	            else if(z==0)
	            travel(abs(dy));
	            else
	            travel_till_bucket(abs(dy));
			}
		}
		else
		{
			if(STy%2!=0)
			{
				if (head=='N')
					STy=STy+1;
				else if(head=='S')
					STy=STy-1;
				travel(1);
				check_head_turn(dx);
				travel(abs(dx));
				dy=C_N_D1_y-STy;
				check_head_turn(dy);
	            if(z!=0 && z<20)
	            travel_till_block(abs(dy));
	            else if(z==0)
	            travel(abs(dy));
	            else
	            travel_till_bucket(abs(dy));
			}
			else
			{
				check_head_turn(dx);
	            if(z!=0 && z<20)
	            travel_till_block(abs(dx));
	            else if(z==0)
	            travel(abs(dx));
	            else
	            travel_till_bucket(abs(dx));
			}
		}
	}
}

/*
* Function Name: find_coorD1(int a)>
* Input : < integer a -> stores the cell value for the number whose coordinates have to be find>
* Output : < NONE>
* Logic: < by applying the concept of the number of rows and number of columns in D1>
* Example Call: <find_coorD1(A_Traversed_D1[p][pos_D1-z]);>
*/
void find_coorD1(int a)
{
 //while(ic<(sizeof(D1))/sizeof(D1[0])){
 //if (D1[ic]==a)
 //{
  NOx=(a%3)*2+1;
  NOy=8-(a/3)*2-1;
  //ic++;
  //break;
 //}
 //ic++;
 //}
}


/*
* Function Name: <go_to_N2()>
* Input : < NONE>
* Output : < NONE>
* Logic: < move bot from current location to node N2 by the help of path function >
* Example Call: <go_to_N2();>
*/
void go_to_N2()
{
 dx=6-STx;
 dy=4-STy;
 path(dx,dy);
}

/*
* Function Name: <N2_to_N3()>
* Input : < NONE>
* Output : < NONE>
* Logic: < move bot from node N2 to node N3 by the help of path function >
* Example Call: <N2_to_N3();>
*/
void N2_to_N3()
{
 dx=2;
 dy=0;
 path(dx,dy);
}
/*
* Function Name: <find_coorD2(int a)>
* Input : < integer a -> stores the index value of the cell number of the respective number of the D2>
* Output : < NONE>
* Logic: < find coordinate of the number in D2 by knowing the number of rows and columns in the D2 >
* Example Call: <find_coorD2(2*p);>
*/
void find_coorD2(int a)
{
	//int i3=1;
	//while(1)
	//{
	//if (D2[i3]==a)
	//{
		NOx=(D2[a]%4*2)+1;
		NOy=(((23-D2[a])/4)*2+1);
		//break;
	//}
	//else
		//i3 +=2;
	//}
}
/*
* Function Name: <N3_to_targetNo()>
* Input : < NONE>
* Output : < NONE>
* Logic: < move bot from N3 node to the number in the D2 cell>
* Example Call: <N3_to_targetNo();>
*/
void N3_to_targetNo()
{
	find_coorD2(2*p);
	if(NOy>6)
	{
		Dest_x=NOx-1;
		Dest_y=NOy;
	}
	else
	{
		Dest_x=NOx;
		Dest_y=NOy+1;
	}
	dx=Dest_x-STx;
	dy=Dest_y-STy;
	
	path(dx,dy);
}
/*
* Function Name: <dest_to_N3()>
* Input : < NONE>
* Output : < NONE>
* Logic: < move bot from current position in D2 to node N3>
* Example Call: <dest_to_N3();>
*/
void dest_to_N3()
{
	dx=(0-Dest_x);
	dy=(6-Dest_y);
	path(dx,dy);
}
/*
* Function Name: <N3_to_N2()>
* Input : < NONE>
* Output : < NONE>
* Logic: < move bot from node N3 to N2>
* Example Call: <N3_to_N2();>
*/
void N3_to_N2()
{
	dx=-2;
	dy=0;
	path(dx,dy);
}
/*
* Function Name: main
* Input: None
* Output: None
* Logic: Helps the bot to traverse through the arena 
* Example Call: Called automatically by the Operating System
*
*/
int main(void)
{
  init_devices();
  servo_3(145);
  _delay_ms(500);
  servo_3_free();
  servo_1(22);
  _delay_ms(400);
  servo_1(70);
  _delay_ms(400);
  servo_1_free();
  while(1)
  {
	  if((PINE & 0x80) != 0x80) //switch is  pressed
	  {
		  break;
	  }
  }
  serial_read();

  travel(2);	
  
  while(D2[2*p]!=NULL)
  {
	  int sum_d1=0;
	  z=0;
	  for(int y=0;y<10;y++)
	  {
		sum_d1=sum_d1+D1[A_Traversed_D1[p][y]] ; 
		if(sum_d1==D2[2*p+1])
			{z++;
			break;}
		else
			z++;	
		/*if(A_Traversed_D1[p][y]==NULL && z>0)
			break;
		else
			z++;
		if(A_Traversed_D1[p][y]==-1)
			A_Traversed_D1[p][y]=0;*/
	  }
	  /*calling*/
	  int pos_D1=z;
	  while(z)
	  {
	  // shortest_no_from_ST();
	   find_coorD1(A_Traversed_D1[p][pos_D1-z]);
	   C_N_D1_x=NOx;          //since sum-no's are in the arranged shortest format
	   C_N_D1_y=NOy;	  
	   Calculate_dx_dy();
	   path(dx,dy);
	   pick_block();
	   z--;
	  }

	  go_to_N2();

	  N2_to_N3();
	  STx=0;
	  STy=6;
      z=30;
	  N3_to_targetNo();
      z=0;
	  buzzer_on();
	  _delay_ms(1000);
	  buzzer_off();	  
	  if(D2[2*(p+1)]!=NULL)
	  {
		dest_to_N3();
		N3_to_N2();
	  }
	  else
	  {
		  buzzer_on();
		  _delay_ms(5000);
		  buzzer_off();
	  }
	  STx=6;
	  STy=4;
	  p++;
	
  }  
}  
  