/*
*Team Id:              eYRCPlus-PS2#41
*Author List:          Gaurav Gupta
*Filename:             turn.h
*Theme:                Puzzle Solver-2
*Functions:            turn(unsigned int , unsigned int )
*Global Variables:     NONE
*
*/

 /*
 * Function Name: turn
 * Input :        a1,a2
 * Output :       NONE
 * Logic:         This function is used to roatate bot whenever required.
 * Example Call:  turn(0,1)
 */
void turn(unsigned int a1, unsigned int a2)
{
	init_devices();
	
	
	while(1)
	{   Left_white_line = adc_conv(3);           //Getting data of Left WL Sensor
		Center_white_line = adc_conv(2);         //getting data of Center WL Sensor
		Right_white_line = adc_conv(1);          //getting data of Right WL Sensor
		
	
		if(STx%2==0 && STy%2==0)
		{
			if (((a1==0) && (a2==1) ) || ((a1==1) && (a2==1)))
			{
				velocity(250,255);
				left();
				angle_rotate(150);
				while (1)
				{
				 Left_white_line = adc_conv(3);         //Getting data of Left WL Sensor
				 Center_white_line = adc_conv(2);       //getting data of Center WL Sensor
				 Right_white_line = adc_conv(1);        //geting data of Right WL Sensor
				 if(Center_white_line>10)
					{
					 stop();
					 break;
					}
				}	
				break;			
			}
			if ((a1==1) && (a2==0) )
			{
				velocity(250,255);
				left();
				angle_rotate(60);
				while (1)
				{   Left_white_line = adc_conv(3);          //Getting data of Left WL Sensor
					Center_white_line = adc_conv(2);       //Getting data of Center WL Sensor
					Right_white_line = adc_conv(1);        //getting data of Right WL Sensor
				
					if(Center_white_line>10)
					 {
						 stop();
					     break;
					 }
				   
				}	
				break;	
			}
			if ((a1==0) && (a2==0) )
			{
				velocity(250,255);
				right();
				angle_rotate(60);
				while (1)
				{
					Left_white_line = adc_conv(3);            //Getting data of Left WL Sensor
					Center_white_line = adc_conv(2);          //etting data of Center WL Sensor
					Right_white_line = adc_conv(1);          //ting data of Right WL Sensor
					if(Center_white_line>10)
					{
						stop();
					    break;
						}
				    }
				    break;				
			    }
			}
		   else
		   {
			velocity(250,255);
			left();
			angle_rotate(150);
			while (1)
			{
					Left_white_line = adc_conv(3);         //Getting data of Left WL Sensor
					Center_white_line = adc_conv(2);       //etting data of Center WL Sensor
					Right_white_line = adc_conv(1);        //ting data of Right WL Sensor
					if(Center_white_line>10)
					{
						stop();
					    break;
					}
					
			}
			break;
		}
	}
}
