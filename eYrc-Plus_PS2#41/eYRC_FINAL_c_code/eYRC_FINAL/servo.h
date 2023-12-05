/*
*Team Id:              eYRCPlus-PS2#41
*Author List:          Gaurav Gupta
*Filename:             servo.h
*Theme:                Puzzle Solver-2
*Functions:            servo_1(unsigned char),servo_2(unsigned char),servo_3(unsigned char),servo_1_free (),servo_2_free (),servo_3_free (),pick_block (),drop_bucket (),
                       up_bucket(),travel_till_bucket(unsigned int)
*Global Variables:     NONE
*
*/

 /*
 * Function Name: servo_1
 * Input :        degrees
 * Output :       NONE
 * Logic:         Function to rotate Servo 1 by a specified angle in the multiples of 1.86 degrees
 * Example Call:  servo_1(50)
 */

void servo_1(unsigned char degrees)  
{
  float PositionPanServo = 0;
  PositionPanServo = ((float)degrees / 1.86) + 35.0;
  OCR1AH = 0x00;
  OCR1AL = (unsigned char) PositionPanServo;
}

/*
 * Function Name: servo_2
 * Input :        degrees
 * Output :       NONE
 * Logic:         Function to rotate Servo 2 by a specified angle in the multiples of 1.86 degrees
 * Example Call:  servo_2(50)
 */
void servo_2(unsigned char degrees)
{
 float PositionTiltServo = 0;
 PositionTiltServo = ((float)degrees / 1.86) + 35.0;
 OCR1BH = 0x00;
 OCR1BL = (unsigned char) PositionTiltServo;
}

/*
 * Function Name: servo_3
 * Input :        degrees
 * Output :       NONE
 * Logic:         Function to rotate Servo 3 by a specified angle in the multiples of 1.86 degrees
 * Example Call:  servo_3(50)
 */
void servo_3(unsigned char degrees)
{
 float PositionServo = 0;
 PositionServo = ((float)degrees / 1.86) + 35.0;
 OCR1CH = 0x00;
 OCR1CL = (unsigned char) PositionServo;
}

//servo_free functions unlocks the servo motors from the any angle 
//and make them free by giving 100% duty cycle at the PWM. This function can be used to 
//reduce the power consumption of the motor if it is holding load against the gravity.

void servo_1_free (void) //makes servo 1 free rotating
{
 OCR1AH = 0x03; 
 OCR1AL = 0xFF; //Servo 1 off
}

void servo_2_free (void) //makes servo 2 free rotating
{
 OCR1BH = 0x03;
 OCR1BL = 0xFF; //Servo 2 off
}

void servo_3_free (void) //makes servo 3 free rotating
{
 OCR1CH = 0x03;
 OCR1CL = 0xFF; //Servo 3 off
} 
/*
 * Function Name: pick_block 
 * Input :        NONE
 * Output :       NONE
 * Logic:         Function to pick the block & drop it in the bucket 
 * Example Call:  pick_block ()
 */
void pick_block (void)
{
	
	servo_2(200);
	_delay_ms(1000);
	servo_1(25);
	_delay_ms(1000);
	servo_2(0);
	_delay_ms(1000);
	servo_1(70);
	_delay_ms(500);
	servo_1_free();
	servo_2_free();
	velocity(250,255);
	//travel(1);
	//if(dx ==0 && dy ==0)
	forward();
	forward_mm(100);      // bot is moved in forward direction by 10 cm so that it doesn't displace any block while taking a 180 degree turn.
}

/*
 * Function Name: drop_bucket 
 * Input :        NONE
 * Output :       NONE
 * Logic:         Function to open the bucket & to place the blocks in the required D2 cell.
 * Example Call:  drop_bucket ()
 */

void drop_bucket (void)
{ 
	 for (int i=120;i>=0;i-=30)
	{
		servo_3(i);
		_delay_ms(150);
	}
	servo_3(0);
	_delay_ms(1000);
}

/*
 * Function Name: up_bucket 
 * Input :        NONE
 * Output :       NONE
 * Logic:         Function to close the bucket after placing the blocks in the required D2 cell.
 * Example Call:  up_bucket ()
 */
void up_bucket(void)
{    
	servo_3(140);
	_delay_ms(400);
	servo_3_free();
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
	//forward();
	//forward_mm(100);
	if(head=='W')
		head='E';	
	if(head=='E')
		head='W';
	if(head=='S')
		head='N';
	if(head=='N')
		head='S';		
	//backward();
	//backward_mm(100);   // bot is moved in backward direction by 10 cm in order to ensure that all the blocks get out of bucket when it get opened & none of them remain in contact                      with the bucket.
}
/*
 * Function Name: travel_till_bucket
 * Input :        b
 * Output :       NONE
 * Logic:         This function is used for traversing the bot till it get reached to the required node of D2 cell where all the blocks are to be placed.
 * Example Call:  travel_till_bucket(2)
 */
void travel_till_bucket(unsigned int b)
{
	if(b>1)
	travel(b-1);
	velocity(245,250);
	forward();
	forward_mm(140);  // After reaching at the required node of D2 cell in which blocks are to be placed, bot is moved 14cm forward so that when blocks fall out of bucket,it                        doesn't fall out of the respective D2 cell
	stop();
	drop_bucket();
	//forward();
	//forward_mm(170);   // bot is moved in forward direction by 17 cm in order to ensure that when bucket get closed ,it donot take the block again in the bucket & ensures the                       proper placement of blocks
	travel(1);
	forward();
	forward_mm(40);	
	up_bucket();
}