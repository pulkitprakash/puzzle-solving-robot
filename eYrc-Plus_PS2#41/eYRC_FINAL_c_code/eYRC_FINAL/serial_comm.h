/*
*Team Id:              eYRCPlus-PS2#41
*Author List:          Gaurav Gupta
*Filename:             serial_comm.h
*Theme:                Puzzle Solver-2
*Functions:            serial_read(),SIGNAL(USART2_RX_vect) 
*Global Variables:     volatile unsigned char data; 
                       unsigned char a[100];int i=0;
*
*/

 
volatile unsigned char data; //to store received data from UDR1
unsigned char a[100];int i=0;
/*
 * Function Name: SIGNAL(USART2_RX_vect)
 * Input :        USART2_RX_vect
 * Output :       NONE
 * Logic:         Function to read the data from serial port & get data stored in various locations of EEPROM
 * Example Call:  servo_1(50)
 */
SIGNAL(USART2_RX_vect) 		// ISR for receive complete interrupt
{
	data = UDR2;
	UDR2=data;
	if (data != 0)
	{   
		 if(data == 0x30) //ASCII value of 0
		{
			data=0;
		}
		if(data == 0x31) //ASCII value of 1
		{
			data=1;
		}

		if(data == 0x32) //ASCII value of 2
		{
			data=2;
		}
		if(data == 0x33) //ASCII value of 7
		{
			data=3;
		}

		if(data == 0x34) //ASCII value of 4
		{
			data=4;
		}

		if(data == 0x36) //ASCII value of 6
		{
			data=6;
		}

		if(data == 0x35) //ASCII value of 5
		{
			data=5;
		}

		if(data == 0x37) //ASCII value of 7
		{
			data=7;
		}
		if(data == 0x38) //ASCII value of 8
		{
			data=8;
		}

		if(data == 0x39) //ASCII value of 9
		{
			data=9;
		}
		if(data==0x61)
		{
			data='a';
		}
		if(data==0x62)
		{
			data='b';
		}	
		if(data==0x63)
		{
			data='c';
		}
	if (data=='c')
	{
		   data=0;
	}
		
	eeprom_update_word((uint8_t*)(i+46),data);
	  
	  if(data=='b')
	   {
		buzzer_on();
		_delay_ms(1000);
		buzzer_off();
	   }
	
	   a[i++] = data;
		
		}
	
}
/*
 * Function Name: serial_read
 * Input :        NONE
 * Output :       NONE
 * Logic:         Function to read the stored data from respective location of EEPROM.
 * Example Call:  serial_read()
 */
int serial_read(void)
{
	int z=46;
	int a1,b=0;
	while(1){
		a1=eeprom_read_byte((uint8_t*)z);
		if((eeprom_read_byte((uint8_t*)(z+1)))!='a')
		{b=a1;
		z++;}
		else
		{
			z=z+2;
			break;
		}
	}

	int len_arr=10*b+a1;
	
	a1=0,b=0;
	int x=0;
	int j=0;
	while(j<len_arr)
	{
		int key=0;
		while(1){
			a1=eeprom_read_byte((uint8_t*)z);
			if((eeprom_read_byte((uint8_t*)(z+1)))!='a')
			{b=a1;
			z++;
			key++;}
			else
			{
				z=z+2;
				key++;
				break;
				
			}
			
			
		}
		if(key==1)
		D1[x++]=a1;
		else if(key==2)
		D1[x++]=10*b+a1;
		
		j=j+2;
	}
	int len=x;
////////////////////////////////////////////	
	a1=0,b=0;
	while(1){
		a1=eeprom_read_byte((uint8_t*)z);
		if((eeprom_read_byte((uint8_t*)(z+1)))!='a')
		{b=a1;
		z++;}
		else
		{
			z=z+2;
			break;
		}
	}
	int len_arr1=10*b+a1;
	
	a1=0,b=0;
	x=0;
	j=0;
	while(j<len_arr1)
	{
		int key=0;
		while(1){
			a1=eeprom_read_byte((uint8_t*)z);
			if((eeprom_read_byte((uint8_t*)(z+1)))!='a')
			{b=a1;
			z++;
			key++;}
			else
			{
				z=z+2;
				key++;
				break;
				
			}
			
			
		}
		if(key==1)
		D2[x++]=a1;
		else if(key==2)
		D2[x++]=10*b+a1;
		
		j=j+2;
	}
	int len1=x;
//////////////////////////////
	a1=0,b=0;
	while(1){
		a1=eeprom_read_byte((uint8_t*)z);
		if((eeprom_read_byte((uint8_t*)(z+1)))!='a')
		{b=a1;
		z++;}
		else
		{
			z=z+2;
			break;
		}
	}
	int len_arr2=10*b+a1;
	
	
	x=0;
	j=0;
	int len_arr2_sub;
	int sub=0;
	int row=-1;
	while(j<len_arr2)
	{
	row++;
	x=0;
	a1=0,b=0;
	while(1){
		a1=eeprom_read_byte((uint8_t*)z);
		if((eeprom_read_byte((uint8_t*)(z+1)))!='a')
		{b=a1;
		z++;}
		else
		{
			z=z+2;
			break;
		}
	}
	sub=0;
	len_arr2_sub=10*b+a1;		
	while(sub<len_arr2_sub)
	{
		int key=0;
		while(1){
			a1=eeprom_read_byte((uint8_t*)z);
			if((eeprom_read_byte((uint8_t*)(z+1)))!='a')
			{b=a1;
			z++;
			key++;}
			else
			{
				z=z+2;
				key++;
				break;
				
			}
			
			
		}
		if(key==1)
		A_Traversed_D1[row][x++]=a1;
		else if(key==2)
		A_Traversed_D1[row][x++]=10*b+a1;
		
		sub=sub+2;
	}
	j++;
	}
	int len2=j;
	int sum=0;
	
}	