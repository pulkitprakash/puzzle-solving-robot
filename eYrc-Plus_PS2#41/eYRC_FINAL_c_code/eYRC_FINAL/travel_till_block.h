/*
*Team Id:              eYRCPlus-PS2#41
*Author List:          Gaurav Gupta
*Filename:             travel_till_block.h
*Theme:                Puzzle Solver-2
*Functions:            travel_till_block(unsigned int)
*Global Variables:     NONE
*
*/

 /*
 * Function Name: travel_till_block
 * Input :        b
 * Output :       NONE
 * Logic:         This function is used for traversing the bot till it get reached to the position of block which is to be picked.
 * Example Call:  travel_till_block(2)
 */

void travel_till_block(unsigned int b)
{
	if(b>1)
	travel(b-1);
	velocity(250,255);
	forward();
	forward_mm(65); 
	while(1)
	{   Left_white_line = adc_conv(3);        //Getting data of Left WL Sensor
		Center_white_line = adc_conv(2);      //getting data of Center WL Sensor
		Right_white_line = adc_conv(1);       //getting data of Right WL Sensor
		ir=adc_conv(4);                       //getting data of left ir proximity sensor
		
		if (ir<140 )
		{ 
			 if(b==1)
			{
				velocity(250,255);
				forward();
				forward_mm(20);
				backward();
				backward_mm(50);
				break;
			}
			else
			{
			velocity(250,255);
			stop();
		    backward();
			backward_mm(20);
			turn_off_ir_proxi_sensors();
			break;
			}
		}
		
	else if(Center_white_line>10 && (Left_white_line-Right_white_line)<=10 && (Right_white_line-Left_white_line)<=10)
	{  
		velocity(250,255);
		forward();
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