/*
*Team Id:              eYRCPlus-PS2#41
*Author List:          Gaurav Gupta
*Filename:             travel.h
*Theme:                Puzzle Solver-2
*Functions:            travel(unsigned int)
*Global Variables:     NONE
*
*/

 /*
 * Function Name: travel
 * Input :        b
 * Output :       NONE
 * Logic:         This function is used for traversing the bot till it get reached to the required node.
 * Example Call:  travel(2)
 */


void travel(unsigned int b)
{
	int n=0;
	while(1)
	{   Left_white_line = adc_conv(3);            //Getting data of Left WL Sensor
		Center_white_line = adc_conv(2);          //getting data of Center WL Sensor
		Right_white_line = adc_conv(1);           //getting data of Right WL Sensor
		
		if(Center_white_line>10 && (Left_white_line-Right_white_line)<=10 && (Right_white_line-Left_white_line)<=10)
		{  
			velocity(250,255);
			forward();
		}
		if( (Left_white_line>12 && Right_white_line>12 && Center_white_line>12) || (Left_white_line>12 && Center_white_line>12 && Right_white_line<12) || (Right_white_line>12 && Center_white_line>12 && Left_white_line<12))
		{
			n++;
			if(n>=(b+1)/2)
			{   
				velocity(250,255);
				forward();
				forward_mm(80);
				stop();
				break;
			}
			else if (n!=b)
			{
				velocity(250,255);
				forward();
				forward_mm(80);
			}
			else if(Center_white_line<10 && (Right_white_line-Left_white_line)>=10 && (Left_white_line-Right_white_line<=10))
			{
				velocity(225,212);
				soft_right();
				//_delay_ms(20);
			}
			else if(Center_white_line<10 && (Right_white_line-Left_white_line<= 10) && (Left_white_line-Right_white_line>10))
			{
				velocity(225,212);
				soft_left();
				//_delay_ms(20);
			}
			else if(Left_white_line<10 && Right_white_line<10 && Center_white_line<10)
			{
				if (Left_white_line< Right_white_line)
				 {
				   velocity(225,212);
				   soft_right();
				 //_delay_ms(20);
				 }
				 else if (Left_white_line> Right_white_line)
				 {
				   velocity(225,212);	 
				   soft_left() ;
				 //_delay_ms(20);					 
				 }				 
			}				
			
			}
		else if(Center_white_line<10 && (Right_white_line-Left_white_line)>=10 && (Left_white_line-Right_white_line<=10))
		{
			velocity(225,212);
			soft_right();
			//_delay_ms(20);
		}
		else if(Center_white_line<10 && (Right_white_line-Left_white_line<= 10) && (Left_white_line-Right_white_line>10))
		{
			velocity(225,212);
			soft_left();
			//_delay_ms(20);
		}
		else if(Left_white_line<12 && Right_white_line<12 && Center_white_line<12)
			{
				if (Left_white_line< Right_white_line)
				{
					
					velocity(225,212);
					soft_right();
					//_delay_ms(20);
				}
				else if (Left_white_line> Right_white_line)
				{
					velocity(225,212);
					soft_left();
					//_delay_ms(20);
				}
			}		
	}
}
